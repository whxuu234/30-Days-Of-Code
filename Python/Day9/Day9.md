# Day9 - Higher Order Functions
[<< Day 8](../Day8/Day8.md)  |  [Day 10 >>](../Day10/Day10.md)

### Agenda
- [Higher Order Functions](#higher-order-functions)
    - [Closures](#closures)
    - [Decorators](#decorators)

## Higher Order Functions
In Python, everything is an _object_, and an _object_ is a [first-class citizen](https://en.wikipedia.org/wiki/First-class_citizen). Consequently, functions can perform the following four operations:

- A function can take other functions as parameters
- A function can be returned by another function
- A function can be modified
- A function can be assigned to a variable

Higher order functions are those that can handle other functions as both parameters and return values.

- Take Functions as Parameters

```python
def square(num):    # regular function
    return num ** 2

def demo(func, number):  # function as a parameter
    ans = func(number)
    return ans
print(demo(square, 5))       # 25
```

- Take Functions as Return Values

```python
import math

def cuboid_volume(length, width, height):
    return length * width * height

def cylinder_volume(radius, height):
    return math.pi * radius * radius * height

def cube_volume(width):
    return width ** 3

def volume_type(type):
    types = {
        'cuboid': cuboid_volume,
        'cube': cube_volume,
        'cylinder': cylinder_volume
    }

    return types.get(type)

formula = volume_type('cuboid')
if formula:
    print(formula(10, 5, 3))  # 150
else:
    print('Invalid volume type')
```

### Closures

To discuss closures, we must first understand scope. In Python, it follows the LEGB rules to look up variables. The LEGB rules are:

- L: Local
- E: Enclosing
- G: Global
- B: Builtins

In Python, a closure is created by nesting a function inside another enclosing function and then returning the inner function. The enclosing scope refers to the outer function of the inner one. When the inner function cannot find variables in its own scope, it will look up the parameters of the outer function's scope.

```python
def multiply_by_ten():
    ten = 10
    def multiply(num):
        return num * ten
    return multiply

closure_func = multiply_by_ten()
print(closure_func(13))  # 130
```

### Decorators

A decorator is a design pattern that enables programmers to add new functionality to an existing object without modifying its original structure.

- Creating Decorators
```python
from functools import *
# A decorator function has the same structure as closures
# It takes a function as a parameter and returns a function
def square_minus_five(func):
    # Using wraps to keep the original function's name and docstring
    @wraps(func)
    def minus(num):
        ans = func(num)
        ans -= 5
        return ans
    return minus

@square_minus_five
def square(num):
    ''' Get square of a num'''
    return num ** 2

print(square(5))   # 20
```

- Multiple Decorators

```python

def capitalize_the_last_letter(func):
    def wrapper():
        string = func()
        capital_string = string[::-1].capitalize()
        return capital_string[::-1]
    return wrapper

def replace_space_with_dash(func):
    def wrapper():
        string = func()
        connected_string = string.replace(' ', '-')
        return connected_string
    return wrapper

# Decorators execute from the one closest to the original function to the farthest.
@replace_space_with_dash
@capitalize_the_last_letter
def greeting():
    return 'hey this is Day nine'
print(greeting())   # hey-this-is-day-ninE
```
