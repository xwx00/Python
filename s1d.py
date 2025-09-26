import numpy as np
from scipy.special import loggamma

def s1d(alpha, beta, eps=1e-6):
    """
    Calculates a closed-form expression for a 1D lattice sum.

    This function is a Python translation of a vectorized MATLAB function,
    designed to compute a specific 1D lattice sum using special functions
    from the SciPy library. It is fully vectorized to handle array-like inputs
    for the 'alpha' parameter.

    Parameters
    ----------
    alpha : complex or array_like of complex
        A complex scalar or an array of complex numbers.
    beta : complex
        A complex scalar. The calculation uses its absolute value.
    eps : float, optional
        A small positive real number for regularization. Defaults to 1e-6.

    Returns
    -------
    numpy.ndarray
        The calculated value(s), matching the shape of alpha.
    """
    # --- Ensure Inputs are NumPy arrays with complex dtype for calculations ---
    # np.asarray is used for efficiency as it avoids making a copy if the
    # input is already a suitable NumPy array.
    alpha = np.asarray(alpha, dtype=np.complex128)
    beta = np.complex128(beta) # Beta is treated as a scalar

    # --- Calculation Steps ---
    
    # 1. Calculate the term related to the Bernoulli number B2.
    # The formula used is B2(|beta|) = |beta|^2 - |beta| + 1/6.
    abs_beta = np.abs(beta)
    term1 = abs_beta**2 - abs_beta + 1/6

    # 2. Calculate terms involving alpha and logarithms.
    term2 = -2 * alpha**2
    term3 = 2 * alpha**2 * np.log(alpha)
    term4 = alpha * np.log(2 * np.pi)

    # 3. Calculate terms involving the log-gamma function from SciPy.
    # scipy.special.loggamma is the complex-compatible equivalent of MATLAB's gammaln.
    term5 = -alpha * loggamma(alpha + abs_beta)
    term6 = -alpha * loggamma(1 + alpha - abs_beta)

    # 4. Calculate the regularized complex logarithm terms.
    # A small 'eps' is added to avoid poles in the exponential. Note that
    # '1j' is the notation for the imaginary unit in Python.
    regularized_alpha = alpha * (1 + 1j * eps)
    z1 = 1 - np.exp(1j * 2 * np.pi * (regularized_alpha + beta))
    z2 = 1 - np.exp(1j * 2 * np.pi * (regularized_alpha - beta))
    term7 = -alpha * (np.log(z1) + np.log(z2))

    # 5. Sum all terms to get the final result.
    result = term1 + term2 + term3 + term4 + term5 + term6 + term7

    return result

if __name__ == '__main__':
    # This block allows the file to be run directly to see example usage.
    
    # --- Example 1: Scalar inputs ---
    alpha_scalar = 0.5 + 0.2j
    beta_scalar = 0.3 
    result_scalar = s1d(alpha_scalar, beta_scalar)
    print("--- Scalar Input Example ---")
    print(f"alpha = {alpha_scalar}")
    print(f"beta  = {beta_scalar}")
    print(f"Result: {result_scalar}\n")

    # --- Example 2: Array input for alpha ---
    alpha_array = np.array([0.5 + 0.2j, 1.2 - 0.5j, 2.0])
    # beta remains a scalar as per the original function's design
    result_array = s1d(alpha_array, beta_scalar)
    print("--- Array Input Example (for alpha) ---")
    print(f"alpha = {alpha_array}")
    print(f"beta  = {beta_scalar}")
    print(f"Result: {result_array}")
