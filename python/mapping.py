# Creating a dictionary (mapping keys to values)
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values by their keys
print(person["name"])  # Output: Alice
print(person["age"])   # Output: 30

# Adding a new key-value pair
person["job"] = "Engineer"
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

# Modifying an existing key's value
person["age"] = 31
print(person["age"])  # Output: 31

# Removing a key-value pair using pop()
person.pop("city")
print(person)  # Output: {'name': 'Alice', 'age': 31, 'job': 'Engineer'}

# Looping through dictionary keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# Output:
# name: Alice
# age: 31
# job: Engineer

# Checking if a key exists in the dictionary
if "name" in person:
    print("Name exists in the dictionary.")  # Output: Name exists in the dictionary.

# Getting a value for a key, with a default value if the key is not found
salary = person.get("salary", "Not available")
print(salary)  # Output: Not available

# Example of a nested dictionary (a dictionary inside another dictionary)
employee = {
    "id": 1001,
    "details": {
        "name": "Bob",
        "department": "HR",
        "salary": 5000
    }
}

# Accessing nested dictionary values
print(employee["details"]["name"])  # Output: Bob
print(employee["details"]["salary"])  # Output: 5000
