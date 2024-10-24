# 1. For loop (iterating over a list)
fruits = ["apple", "banana", "cherry"]
print("Example 1: For loop over a list")
for fruit in fruits:
    print(fruit)
print()  # Blank line for better output formatting

# 2. For loop with range() (looping through numbers)
print("Example 2: For loop with range()")
for i in range(5):  # Will iterate from 0 to 4
    print(i)
print()

# 3. While loop (running a loop as long as a condition is true)
x = 0
print("Example 3: While loop")
while x < 5:
    print(x)
    x += 1  # Increment x by 1 each time
print()

# 4. For loop with break (stopping the loop when a condition is met)
print("Example 4: For loop with break")
for i in range(10):
    if i == 5:
        break  # Exit the loop when i equals 5
    print(i)
print()

# 5. For loop with continue (skipping the current iteration)
print("Example 5: For loop with continue")
for i in range(7):
    if i == 3:
        continue  # Skip when i equals 3
    print(i)
print()

# 6. While loop with else block (executing code after the loop finishes)
x = 0
print("Example 6: While loop with else block")
while x < 5:
    print(x)
    x += 1
else:
    print("Loop is finished!")  # Executes after the while loop completes
print()

# 7. Nested loops (loop inside another loop)
print("Example 7: Nested loops")
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
print()

# 8. Looping through a dictionary
person = {"name": "John", "age": 25, "city": "New York"}
print("Example 8: Looping through a dictionary")
for key, value in person.items():
    print(f"{key}: {value}")
print()

# 9. List comprehension (a compact form of loop to create lists)
print("Example 9: List comprehension")
squares = [x**2 for x in range(5)]  # Creates a list of squares [0, 1, 4, 9, 16]
print(squares)
