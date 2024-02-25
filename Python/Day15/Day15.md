# Day15 - Class
[<< Day 14](../Day14/Day14.md)  |  [Day 16 >>](../Day16/Day16.md)

### Agenda
- [Class](#class)
    - [Class Creating](#class-creating)
    - [Object Creating](#object-creating)
    - [Constructor](#constructor)
    - [Object Methods](#object-creating)
    - [Inheritance](#inheritance)

## Class

In Python, everything is an object, including its attributes and methods. Programmers create class to create an object. 

As an object-oriented programming language, everything in python is treated as an object with its own attributes and methods. Objects are instances of corresponding built-in or customized classes, and classes serve as blueprints for creating objects. 
By instantiating a class, programmers can create an object, which inherits the attributes and behavior defined by the class.

### Class Creating

In Python, when creating a class using the keyword **class**, it is customary for the class name to adhere to the **CamelCase** convention.

**Example:**

```python
class PersonalInformation:
    pass
print(PersonalInformation)  # class PersonalInformation info
```

### Object Creating

To instantiate an object, programmers need to invoke the class along with any required parameters.

```py
class PersonalInformation:
    pass
perinfo = PersonalInformation()
print(perinfo)  # PersonalInformation object
```

### Constructor

The constructor is a special method that gets invoked during the initialization of a new object. In Python, this method is named **\_\_init\_\_()**. The **self** parameter within the constructor serves as a reference to the current instance of the class, although it can be assigned any other name if desired.

**Examples:**

```python
class PersonalInformation:
    def __init__(self, firstname, surname, age, country):
        self.firstname = firstname
        self.surname = surname
        self.age = age
        self.country = country

perinfo = PersonalInformation('David', 'Lin', 35, 'Taiwan')
print(perinfo.firstname) # David
print(perinfo.surname) # Lin
print(perinfo.age) # 35
print(perinfo.country)  # Taiwan
```

### Object Methods

Objects can have methods. The methods are functions which belong to the object.

**Example:**

```python
# Methods in a class is working the same as the normal functions, it can have default parameters, arguments, return value etc.
# In regular case, it should have a self parameter as the first parameter to reference instance itself
class PersonalInformation:
    def __init__(self, firstname = 'David', surname = 'Lin', age = 35, country = 'Taiwan'):
        self.firstname = firstname
        self.surname = surname
        self.age = age
        self.country = country
    def show_info(self):
        return f'{self.firstname} {self.surname} is {self.age} years old. He lives in {self.country}.'

perinfo = PersonalInformation()
print(perinfo.show_info())  # David Lin is 35 years old. He lives in Taiwan
```

- classmethod() and staticmethod()
```python
# classmethods is a built-in function, which can be use as a decorator to transform a method into a class method
# A class method can be called without creating instance. The first parameter 'cls' is the reference to class itself
# Therefore, a class method can access the members in class itself
class PersonalInformation:
    demo_string = 'Hey, I can be access by a class method!'
    def __init__(self, firstname = 'David', surname = 'Lin', age = 35, country = 'Taiwan'):
        self.firstname = firstname
        self.surname = surname
        self.age = age
        self.country = country

    def show_info(self):
        return f'{self.firstname} {self.surname} is {self.age} years old. He lives in {self.country}.'
    
    @classmethod
    def demo_class_method(cls):
        return cls.demo_string

print(PersonalInformation.demo_class_method())  # Hey, I can be access by a class method!
print(PersonalInformation.show_info()) # raise TypeError as missing instance memory location


# staticmethod is a built-in function, which can be use as a decorator to transform a method into a static method
# A class method can be called without creating instance.
# But it doesn't have direct access to members in the class. It can only use class name to access the corresponding attribute
class PersonalInformation:
    demo_string = 'Hey, I can be access by a calling class attribute!'
    def __init__(self, firstname = 'David', surname = 'Lin', age = 35, country = 'Taiwan'):
        self.firstname = firstname
        self.surname = surname
        self.age = age
        self.country = country

    def show_info(self):
        return f'{self.firstname} {self.surname} is {self.age} years old. He lives in {self.country}.'
    
    @staticmethod
    def demo_static_method():
        return PersonalInformation.demo_string

print(PersonalInformation.demo_static_method())  # Hey, I can be access by a calling class attribute!
```

### Inheritance

By utilizing inheritance, programmers can effectively reuse code from a parent class. This technique enables the creation of a subclass that inherits all the methods and properties of its parent class, thereby minimizing the need to duplicate code.

```python
# Inheritance example
from abc import ABC, abstractmethod
class Volume(ABC):
    def __init__(self):
        self.demo_string = 'It is inherited from parent class'

    # In certain cases, programmers may wish to define an empty function that will be implemented by a child class later on.
    # The use of **@abstractmethod** can assist in ensuring that such methods are implemented, preventing unintended omissions.
    # If programmers didnot implement the abstract method in child class, it will raise a TypeError
    @abstractmethod
    def calculate_volume(self):
        pass

class Cube(Volume):
    def __init__(self, length):
        # Programmers can use super() to call the parent's method
        super().__init__()
        self.length = length

    def calculate_volume(self):
        return self.length ** 3

cube_A = Cube(5)
print(cube_A.calculate_volume()) # 125
```

- multi inheritance
```python
# In Python, a child class can inherite from multiple parent classes
# But if the parent classes contain the same method name, it will follow the Method Resolution Order like following:
#   childclass, parentclass one, parent class two
class Volume:
    def cal_vol(self):
        return self.length ** 3
    def cal_area(self):
        return f'The area is {self.length ** 2}'

class Flat:
    def cal_area(self):
        return self.length ** 2

class CubeOne(Volume, Flat):
    def __init__(self, length):
        self.length = length

class CubeTwo(Flat, Volume):
    def __init__(self, length):
        self.length = length

cube_A = CubeOne(5)
cube_B = CubeTwo(5)
# In CubeOne, the Method Resolution Order is CubeOne, Volume, Flat
# So the cal_area() method will be called from CubeOne first, followed by Volume and Flat
print(cube_A.cal_area()) # The area is 25
# In CubeTwo, the cal_area() method will be called from CubeOne first, followed by Flat and Volume
print(cube_B.cal_area()) # 25
```
