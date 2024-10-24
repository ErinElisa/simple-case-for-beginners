# Arithmetic Operators
a = 10
b = 3

# Addition
add = a + b  # 10 + 3 = 13
print("Addition:", add)

# Subtraction
sub = a - b  # 10 - 3 = 7
print("Subtraction:", sub)

# Multiplication
mul = a * b  # 10 * 3 = 30
print("Multiplication:", mul)

# Division
div = a / b  # 10 / 3 = 3.3333...
print("Division:", div)

# Modulus
mod = a % b  # 10 % 3 = 1
print("Modulus:", mod)

# Exponentiation
exp = a ** b  # 10^3 = 1000
print("Exponentiation:", exp)

# Floor Division
floor_div = a // b  # 10 // 3 = 3
print("Floor Division:", floor_div)


# Comparison Operators
x = 5
y = 8

print("Equal:", x == y)          # False
print("Not Equal:", x != y)      # True
print("Greater Than:", x > y)    # False
print("Less Than:", x < y)       # True
print("Greater or Equal:", x >= y)  # False
print("Less or Equal:", x <= y)     # True


# Assignment Operators
c = 10
c += 2  # Equivalent to c = c + 2
print("c after += 2:", c)

c -= 2  # Equivalent to c = c - 2
print("c after -= 2:", c)

c *= 2  # Equivalent to c = c * 2
print("c after *= 2:", c)

c /= 2  # Equivalent to c = c / 2
print("c after /= 2:", c)


# Logical Operators
x = True
y = False

print("Logical AND:", x and y)  # False
print("Logical OR:", x or y)    # True
print("Logical NOT:", not x)    # False


# Bitwise Operators
p = 6  # 110 in binary
q = 2  # 010 in binary

# Bitwise AND
print("Bitwise AND:", p & q)  # 010 -> 2

# Bitwise OR
print("Bitwise OR:", p | q)  # 110 -> 6

# Bitwise XOR
print("Bitwise XOR:", p ^ q)  # 100 -> 4

# Bitwise NOT
print("Bitwise NOT:", ~p)  # -(p+1) -> -7


# Identity Operators
a = 10
b = 10
c = [1, 2, 3]
d = [1, 2, 3]

print("a is b:", a is b)  # True (both have the same identity)
print("c is d:", c is d)  # False (different objects)


# Membership Operators
nums = [1, 2, 3, 4, 5]

# in operator
print("3 in nums:", 3 in nums)  # True

# not in operator
print("6 not in nums:", 6 not in nums)  # True
