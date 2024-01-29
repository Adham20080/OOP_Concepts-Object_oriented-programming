"""
Object-Oriented Programming (OOP) is a programming paradigm that uses objects, which are instances of classes, to organize code. In Python, everything is an object, and the language supports OOP principles. Let's go through the key concepts of OOP in Python.

1. Class:
A class is a blueprint for creating objects. It defines a data structure and behavior that the objects of the class will have. To create a class in Python, you use the class keyword.
"""


class MyClass:
    # Class attributes (shared by all instances)
    class_attribute = "I am a class attribute"

    # Constructor method (called when an object is created)
    def __init__(self, parameter1, parameter2):
        self.parameter1 = parameter1  # Instance attribute
        self.parameter2 = parameter2

    # Instance method
    def display_parameters(self):
        print(f"Parameter 1: {self.parameter1}, Parameter 2: {self.parameter2}")


"""
2. Object:
An object is an instance of a class. You create objects based on the blueprint (class) and can have different values for their attributes.
"""

# Creating an object of MyClass
obj = MyClass("Value 1", "Value 2")

# Accessing attributes and calling methods
print(obj.parameter1)  # Accessing instance attribute
obj.display_parameters()  # Calling instance method

"""
3. Inheritance:
Inheritance allows a class to inherit the properties and methods of another class. The class that is inherited from is called the base class, and the class that inherits is called the derived class.
"""


class MyDerivedClass(MyClass):
    def __init__(self, parameter1, parameter2, additional_parameter):
        # Call the constructor of the base class
        super().__init__(parameter1, parameter2)
        self.additional_parameter = additional_parameter

    # Override a method from the base class
    def display_parameters(self):
        print(
            f"Parameter 1: {self.parameter1}, Parameter 2: {self.parameter2}, Additional Parameter: {self.additional_parameter}")


"""
4. Encapsulation:
Encapsulation is the bundling of data (attributes) and methods that operate on the data into a single unit (class). It helps in hiding the implementation details and exposing only what is necessary.
"""


class EncapsulatedClass:
    def __init__(self):
        # Private attribute (encapsulation)
        self.__private_attribute = "I am private"

    # Public method to access private attribute
    def get_private_attribute(self):
        return self.__private_attribute


"""
5. Polymorphism:
Polymorphism allows objects of different classes to be treated as objects of a common base class. It enables a single interface to represent different types of objects.
"""


# Polymorphic function
def polymorphic_function(obj):
    obj.display_parameters()


# Using objects of different classes with a common base class
obj1 = MyClass("Value 1", "Value 2")
obj2 = MyDerivedClass("Value 1", "Value 2", "Additional Value")

polymorphic_function(obj1)
polymorphic_function(obj2)

"""
6. Abstraction:
Abstraction involves hiding the complex reality while exposing only the essential parts. It allows you to focus on what an object does rather than how it achieves what it does.
"""

from abc import ABC, abstractmethod


# Abstract base class
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass


# Concrete class implementing the abstract method
class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("Implementation of abstract_method")


"""
In this example, AbstractClass is an abstract base class with an abstract method. ConcreteClass then inherits from AbstractClass and provides an implementation for the abstract method.

These concepts form the foundation of OOP in Python. You can use them to structure your code in a more organized and reusable way. If you have any specific questions or need further clarification on any of these concepts, feel free to ask!
"""
