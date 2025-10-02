'''
JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. It is commonly used for transmitting data in web applications between a server and a client.
'''

import json

# Convert a Python object (dictionary) to a JSON string
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
json_string = json.dumps(data)
print(json_string)

# Convert a JSON string back to a Python object
parsed_data = json.loads(json_string)
print(parsed_data)
print(parsed_data['name'])  # Accessing a value from the parsed data