from abc import ABC, abstractmethod

# Abstract classes in Python
# Abstract classes are classes that contain one or more abstract methods.
# An abstract method is a method that is declared, but contains no implementation.
# Abstract classes cannot be instantiated and require subclasses to provide implementations for the abstract methods.


# Define an abstract class using ABC (Abstract Base Class)
class Animal(ABC):
    # Define an abstract method
    @abstractmethod
    def make_sound(self):
        pass

# Define a subclass that inherits from the abstract class
class Dog(Animal):
    # Provide implementation for the abstract method
    def make_sound(self):
        return "Bark"

# Define another subclass that inherits from the abstract class
class Cat(Animal):
    # Provide implementation for the abstract method
    def make_sound(self):
        return "Meow"

# Instantiate the subclasses
dog = Dog()
cat = Cat()

# Call the implemented methods
print(dog.make_sound())  # Output: Bark
print(cat.make_sound())  # Output: Meow