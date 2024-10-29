# Classes in Python
# A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.

# Defining a simple class
class Animal:
    # Constructor method to initialize the object
    def __init__(self, name):
        self.name = name  # Attribute of the class

    # Method of the class
    def speak(self):
        return f"{self.name} makes a sound"

# Single Inheritance
# A class inherits from one base class
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

# Multiple Inheritance
# A class inherits from more than one base class
class Canine:
    def run(self):
        return "Runs fast"

class Wolf(Animal, Canine):
    def speak(self):
        return f"{self.name} howls"

# Multilevel Inheritance
# A class inherits from a derived class, forming a chain
class Puppy(Dog):
    def speak(self):
        return f"{self.name} yips"

# Hierarchical Inheritance
# Multiple classes inherit from a single base class
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

class Bird(Animal):
    def speak(self):
        return f"{self.name} chirps"

# Hybrid Inheritance
# A combination of two or more types of inheritance
class Pet(Animal):
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner

class PetDog(Pet, Dog):
    def speak(self):
        return f"{self.name} barks and is owned by {self.owner}"

# Example usage
if __name__ == "__main__":
    dog = Dog("Buddy")
    print(dog.speak())  # Output: Buddy barks

    wolf = Wolf("Ghost")
    print(wolf.speak())  # Output: Ghost howls
    print(wolf.run())    # Output: Runs fast

    puppy = Puppy("Max")
    print(puppy.speak())  # Output: Max yips

    cat = Cat("Whiskers")
    print(cat.speak())  # Output: Whiskers meows

    bird = Bird("Tweety")
    print(bird.speak())  # Output: Tweety chirps

    pet_dog = PetDog("Rex", "John")
    print(pet_dog.speak())  # Output: Rex barks and is owned by John
