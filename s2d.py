import numpy as np
from scipy.special import erfc, erfcx
from scipy.integrate import quad
import mpmath

# Set mpmath precision lower for speed
mpmath.mp.dps = 15  # Reduced from 30 for speed

# Precompute constants to avoid repeated calculations
PI = np.pi
TWO_PI = 2.0 * np.pi
SQRT_PI = np.sqrt(np.pi)

def fast_jtheta3(z, q):
    """
    Fast approximation of Jacobi theta function theta_3(z, q) for the integration range.
    Optimized with early termination and minimal function calls.
    """
    if abs(q) >= 0.99:  
        n_terms = 3
    elif abs(q) >= 0.9:
        n_terms = 5
    else:
        n_terms = 10
    
    # Series expansion: theta_3(z,q) = 1 + 2*sum(q^(n^2)*cos(2*n*z), n=1,inf)
    result = 1.0
    two_z = 2.0 * z
    
    for n in range(1, n_terms + 1):
        q_power = q**(n*n)
        if abs(q_power) < 1e-12:  # Early termination for convergence
            break
        result += 2.0 * q_power * np.cos(n * two_z)
    
    return result 

def s2d(alpha, beta1, beta2, eps=1e-6):
    """
    Calculates the 2D lattice sum by combining three components. This is the
    main function that calls the helper functions _s12d, _s22d, and _s32d.

    Parameters
    ----------
    alpha : complex
        A complex parameter.
    beta1 : float
        A real parameter.
    beta2 : float
        A real parameter.
    eps : float, optional
        A small positive real number for regularization. Defaults to 1e-6.

    Returns
    -------
    complex
        The result of the 2D lattice sum.
    """
    # --- Ensure correct data types ---
    alpha = np.complex128(alpha)
    beta1 = float(beta1)
    beta2 = float(beta2)
    eps = float(eps)
    
    # --- Function Calls ---
    # The result is the sum of the three components.
    # Note: This code requires the 'mpmath' library for the Jacobi theta function.
    # You can install it using: pip install mpmath
    try:
        result = _s12d(beta1, beta2) + _s22d(alpha, beta1, beta2) + _s32d(alpha, beta1, beta2, eps)
    except ImportError:
        print("Error: The 'mpmath' library is required.")
        print("Please install it using: pip install mpmath")
        return None
        
    return result

# =========================================================================
# HELPER FUNCTIONS
# These functions are called by the main s2d function.
# =========================================================================

def _s12d(beta1, beta2):
    """First component of the 2D lattice sum - optimized."""
    
    # Precompute constants
    pi_beta1 = PI * beta1
    pi_beta2 = PI * beta2
    coeff = 1.0 / (2.0 * PI * PI)
    
    def integrand(t):
        theta1 = fast_jtheta3(pi_beta1, t)
        theta2 = fast_jtheta3(pi_beta2, t)
        return (theta1 * theta2 - 1.0) / t

    # Use relaxed tolerances for speed
    integral_val, _ = quad(integrand, 1e-12, 1.0, epsabs=1e-8, epsrel=1e-8, limit=30)
    return coeff * integral_val

def _s22d(alpha, beta1, beta2):
    """Second component of the 2D lattice sum - highly optimized."""
    
    # Precompute constants
    pi_alpha = PI * alpha
    pi_beta1 = PI * beta1
    pi_beta2 = PI * beta2
    neg_alpha_over_2sqrt_pi = -alpha / (2 * SQRT_PI)
    
    # Use local cache for this function call only
    cache = {}
    
    def complex_integrand(t):
        if t <= 0:
            return 0.0 + 0.0j
        
        # Round t to reduce cache misses while maintaining accuracy
        t_key = round(t, 12)
        if t_key in cache:
            return cache[t_key]
        
        # Optimized calculations - minimize function calls
        log_t = np.log(t)
        sqrt_neg_log_t = np.sqrt(-log_t)
        
        # Calculate all terms efficiently
        term1 = erfcx(pi_alpha / sqrt_neg_log_t)
        term2 = 1.0 / (t * sqrt_neg_log_t)
        
        # Fast theta calculations
        theta1 = fast_jtheta3(pi_beta1, t)
        theta2 = fast_jtheta3(pi_beta2, t)
        
        result = complex(term1) * term2 * (theta1 * theta2 - 1.0)
        cache[t_key] = result
        return result

    # Optimized integration with looser tolerances for speed
    def real_integrand(t):
        return complex_integrand(t).real
    
    def imag_integrand(t):
        return complex_integrand(t).imag

    # Use lower precision for speed while maintaining reasonable accuracy
    real_integral, _ = quad(real_integrand, 1e-10, 1 - 1e-10, 
                           epsabs=1e-8, epsrel=1e-8, limit=30)
    imag_integral, _ = quad(imag_integrand, 1e-10, 1 - 1e-10,
                           epsabs=1e-8, epsrel=1e-8, limit=30)
    
    integral_val = real_integral + 1j * imag_integral
    return neg_alpha_over_2sqrt_pi * integral_val

def _s32d(alpha, beta1, beta2, epsilon):
    """Third component of the 2D lattice sum using the Ewald method."""
    
    # --- Parameters ---
    nmax = 10       # Maximum index for real space sum
    nmax1 = 10      # Maximum index for momentum space sum
    eta = 1 / np.sqrt(np.pi)  # Ewald parameter
    aa = alpha * (1 + 1j * epsilon)

    # --- Real Sum Components ---
    ra1 = 2 * np.pi * aa
    ra2 = 1 / eta
    ra3 = np.pi * aa * eta
    
    realSum1 = 0
    for n1 in range(1, nmax + 1):
        for n2 in range(1, nmax + 1):
            norm_val = np.sqrt(n1**2 + n2**2)
            term = (1 / norm_val) * \
                   (np.exp(1j * ra1 * norm_val) * erfc(ra2 * norm_val + 1j * ra3) +
                    np.exp(-1j * ra1 * norm_val) * erfc(ra2 * norm_val - 1j * ra3)) * \
                   np.cos(2 * np.pi * beta1 * n1) * np.cos(2 * np.pi * beta2 * n2)
            realSum1 += term
    realSum1 *= 2 * alpha

    realSum2 = 0
    for n in range(1, nmax + 1):
        norm_val = float(n)
        term = (1 / norm_val) * \
               (np.exp(1j * ra1 * norm_val) * erfc(ra2 * norm_val + 1j * ra3) +
                np.exp(-1j * ra1 * norm_val) * erfc(ra2 * norm_val - 1j * ra3)) * \
               (np.cos(2 * np.pi * beta1 * n) + np.cos(2 * np.pi * beta2 * n))
        realSum2 += term
    realSum2 *= alpha

    realSum = realSum1 + realSum2

    # --- Momentum Sum Components ---
    ma1 = np.pi * eta
    momentumSum1 = 0
    for h1 in range(-nmax1, nmax1 + 1):
        for h2 in range(-nmax1, nmax1 + 1):
            if h1 == 0 and h2 == 0 and beta1 == 0 and beta2 == 0:
                continue
            
            sqTerm_arg = (beta1 + h1)**2 + (beta2 + h2)**2 - aa**2
            # Use np.sqrt on a complex number to handle negative arguments correctly
            sqTerm = np.sqrt(np.complex128(sqTerm_arg))
            
            momentumSum1 += erfc(ma1 * sqTerm) / sqTerm
            
    momentumSum1 *= alpha

    momentumSum2 = alpha * (-2 / (eta * np.sqrt(np.pi)) * np.exp(np.pi**2 * aa**2 * eta**2) + \
                       2 * np.pi * np.sqrt(np.complex128(-aa**2)) * erfc(np.pi * eta * np.sqrt(np.complex128(-aa**2))))
    
    momentumSum = momentumSum1 + momentumSum2
    
    return realSum + momentumSum


if __name__ == '__main__':
    # This block allows the file to be run directly to see example usage.
    # --- Example Usage ---
    alpha_val = 0.32
    beta1_val = 0.1
    beta2_val = 0.3
    
    print("--- 2D Lattice Sum Example ---")
    print(f"alpha = {alpha_val}")
    print(f"beta1 = {beta1_val}")
    print(f"beta2 = {beta2_val}")
    print()
    
    # Calculate each component independently
    try:
        s12d_val = _s12d(beta1_val, beta2_val)
        s22d_val = _s22d(alpha_val, beta1_val, beta2_val)
        s32d_val = _s32d(alpha_val, beta1_val, beta2_val, 1e-6)
        
        print("--- Individual Components ---")
        print(f"s12d = {s12d_val}")
        print(f"s22d = {s22d_val}")
        print(f"s32d = {s32d_val}")
        print()
        
        # Calculate total result
        result_val = s12d_val + s22d_val + s32d_val
        print(f"Total Result (s12d + s22d + s32d) = {result_val}")
        
        # Verify with main function
        result_main = s2d(alpha_val, beta1_val, beta2_val)
        print(f"Main function result = {result_main}")
        
    except Exception as e:
        print(f"Error calculating components: {e}")
        print("Trying main function...")
        result_val = s2d(alpha_val, beta1_val, beta2_val)
        if result_val is not None:
            print(f"Result: {result_val}")
