# 1. Basic Lambda Function
# A lambda function that adds 10 to a given number
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15

# 2. Lambda with Multiple Arguments
# A lambda function that multiplies two numbers
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12

# 3. Lambda with Conditional Logic
# A lambda function that checks if a number is even or odd
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(7))  # Output: Odd
print(is_even(10))  # Output: Even

# 4. Using Lambda with Built-in Functions
# Lambda with the map function to square each element in a list
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

# 5. Using Lambda with filter
# Lambda with the filter function to get only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# 6. Lambda within sorted for Custom Sorting
# Sort a list of tuples by the second element using a lambda function
pairs = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(2, 'a'), (1, 'b'), (3, 'c')]

# 7. Lambda with Reduce (from functools)
# Lambda with reduce to calculate the product of all numbers in a list
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24 (1 * 2 * 3 * 4)

# 8. Lambda as an Anonymous Function
# Using lambda directly without assigning it to a variable
print((lambda x, y: x + y)(3, 5))  # Output: 8
