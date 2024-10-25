# Casting to Integer (int)
# Convert from string to integer
num_str = "100"
num_int = int(num_str)
print(num_int)  # Output: 100

# Convert from float to integer
num_float = 20.75
num_int = int(num_float)
print(num_int)  # Output: 20 (rounded down)

# Casting to Float (float)
# Convert from string to float
num_str = "123.45"
num_float = float(num_str)
print(num_float)  # Output: 123.45

# Convert from integer to float
num_int = 50
num_float = float(num_int)
print(num_float)  # Output: 50.0

# Casting to String (str)
# Convert from integer to string
num_int = 75
num_str = str(num_int)
print(num_str)  # Output: "75"

# Convert from float to string
num_float = 88.99
num_str = str(num_float)
print(num_str)  # Output: "88.99"

# Casting to Boolean (bool)
# Convert from integer to boolean
num_int = 0
num_bool = bool(num_int)
print(num_bool)  # Output: False (0 is False)

num_int = 5
num_bool = bool(num_int)
print(num_bool)  # Output: True (non-zero is True)

# Convert from string to boolean
text = ""
text_bool = bool(text)
print(text_bool)  # Output: False (empty string is False)

text = "Hello"
text_bool = bool(text)
print(text_bool)  # Output: True (non-empty string is True)

# Casting to List (list)
# Convert from string to list
text = "Hello"
text_list = list(text)
print(text_list)  # Output: ['H', 'e', 'l', 'l', 'o']

# Convert from tuple to list
num_tuple = (1, 2, 3)
num_list = list(num_tuple)
print(num_list)  # Output: [1, 2, 3]

# Casting to Tuple (tuple)
# Convert from list to tuple
num_list = [4, 5, 6]
num_tuple = tuple(num_list)
print(num_tuple)  # Output: (4, 5, 6)
