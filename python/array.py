# Creating an array (list) in Python
fruits = ["apple", "banana", "cherry", "date"]

# 1. Getting the length of the array
# len() returns the number of items in the array
length = len(fruits)
print("Length of the array:", length)  # Output: 4

# 2. Accessing array elements by index
# Indexes start at 0, so the first element is at index 0
print("First element:", fruits[0])     # Output: apple
print("Second element:", fruits[1])    # Output: banana
print("Third element:", fruits[2])     # Output: cherry

# 3. Accessing the last element
# Use -1 to access the last element in the array
print("Last element:", fruits[-1])     # Output: date

# 4. Modifying an element in the array
# Replace "banana" with "blueberry"
fruits[1] = "blueberry"
print("Modified array:", fruits)       # Output: ['apple', 'blueberry', 'cherry', 'date']

# 5. Accessing a range of elements (slicing)
# This will get elements from index 1 to 2 (end index is not included)
print("Slice of array:", fruits[1:3])  # Output: ['blueberry', 'cherry']

# 6. Looping through array elements
# Using a for loop to print each fruit
print("Array elements:")
for fruit in fruits:
    print(fruit)

# 7. Using enumerate to get index and value together
# This can be helpful for getting both the index and value of each element
print("Index and value:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
