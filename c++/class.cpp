/*
C++ is an object-oriented programming language. 
Everything in C++ is associated with classes and objects, along with its attributes and methods. 
Refer this doc for more reference: https://www.w3schools.com/cpp/cpp_classes.asp

In C++, it is possible to inherit attributes and methods from one class to another. 
We group the "inheritance concept" into two categories:
- derived class
- base class
*/

#include <iostream>
using namespace std;

// Base class
class Animal {
public:
    void eat() {
        cout << "This animal eats food." << endl;
    }
};

// Derived class inheriting from Animal (Single Inheritance)
class Dog : public Animal {
public:
    void bark() {
        cout << "The dog barks." << endl;
    }
};

// Another base class
class Bird {
public:
    void fly() {
        cout << "This bird can fly." << endl;
    }
};

// Derived class inheriting from both Animal and Bird (Multiple Inheritance)
class Bat : public Animal, public Bird {
public:
    void useEcholocation() {
        cout << "The bat uses echolocation." << endl;
    }
};

// Intermediate class for multilevel inheritance
class Mammal : public Animal {
public:
    void giveBirth() {
        cout << "This mammal gives birth to live young." << endl;
    }
};

// Derived class inheriting from Mammal (Multilevel Inheritance)
class Human : public Mammal {
public:
    void speak() {
        cout << "The human speaks." << endl;
    }
};

// Base class for hierarchical inheritance
class Vehicle {
public:
    void start() {
        cout << "The vehicle starts." << endl;
    }
};

// Derived class inheriting from Vehicle (Hierarchical Inheritance)
class Car : public Vehicle {
public:
    void drive() {
        cout << "The car drives." << endl;
    }
};

// Another derived class inheriting from Vehicle (Hierarchical Inheritance)
class Bike : public Vehicle {
public:
    void ride() {
        cout << "The bike rides." << endl;
    }
};

int main() {
    // Single Inheritance
    Dog dog;
    dog.eat();
    dog.bark();

    // Multiple Inheritance
    Bat bat;
    bat.eat();
    bat.fly();
    bat.useEcholocation();

    // Multilevel Inheritance
    Human human;
    human.eat();
    human.giveBirth();
    human.speak();

    // Hierarchical Inheritance
    Car car;
    car.start();
    car.drive();

    Bike bike;
    bike.start();
    bike.ride();

    return 0;
}