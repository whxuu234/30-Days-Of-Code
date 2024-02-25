# Day8 - Modules
[<< Day 7](../Day7/Day7.md)  |  [Day 9 >>](../Day9/Day9.md)

### Agenda
- [Modules](#modules)
    - [Module Creation](#module-creation)
    - [Module Importing](#module-importing)
    - [Built-in Modules](#built-in-modules)
- [Packages]
- [Reference](#reference)


## Modules
A module is a Python file that contains a collection of definitions and statements, which can be incorporated into an application.

### Module Creation
To create a module, programmers should begin by writing their code in a Python script, saving it as a .py file. The module name matches the file name.

```python
# calculator.py file
def plus(first_num, second_num):
    return first_num + second_num

def multiply(first_num, second_num):
    return first_num * second_num
```

Now we get a calculator module.

### Module Importing
Programmers have the option to import either the entire module or specific functions from it.

- import module calculator
```python
# Programmers must use module name to access the functions
import calculator
print(calculator.plus(3, 5))    # 8
```

- import specific functions from module calculator
```python
# Since we are importing specific functions, we don't need to use the module name
from calculator import multiply
print(multiply(3, 7))   # 21

# It will raise NameError as we only import specific functions instead of whole module
print(calculator.plus(3, 5)) # NameError: name 'calculator' is not defined
```

- import functions from module and rename them
```python
from calculator import plus as plus_two_num, multiply as get_product
print(plus_two_num(9, 10))  # 19
print(get_product(13, 5))   # 65
```

### Built-in Modules

Python provides numerous useful built-in modules. Programmers can import these modules by using the "import" keyword followed by the file or function they need.

- [OS Module](https://docs.python.org/3/library/os.html)
```python
# The Python OS module offers functions to perform various operating system tasks automatically. 
# These tasks include creating and deleting directories, changing the working directory, fetching directory contents, and identifying the current directory.

import os
# Creating and removing a directory
os.mkdir('directory name')
os.rmdir('directory name')

# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()

# Getting the directory of a file
# __file__ is a built-in variable that contains the absolute path of the file currently being executed.
print(os.path.dirname(__file__)) # prints the absolute path of the file directory

# os.path.join combines several path togeteher
print(os.path.join(os.path.dirname(__file__), "..", "..")) 
```

- [Sys Module](https://docs.python.org/3/library/sys.html)
```python
# The Python sys module provides functions for interacting with different aspects of the Python runtime environment.

import sys
# sys.argv is a list containing command-line arguments passed to the script, which formatted as follows: 
# filename argument1 argument2 
# sys.argv[0] refers to the name of the script itself.
print(f'file name: {sys.argv[0]}, argument1: {sys.argv[1]}, argument2: {sys.argv[2]}')

# Exit the program with a specific return code ranging from 0 to 255. 
# Programmers can assign different codes to various meanings and identify the program's state.
# By default, 0 is returned if no error occurs.
sys.exit()

# The maximum size of integer in Python
sys.maxsize

# Environmental path
sys.path
```

- [Argparse module](https://docs.python.org/3/howto/argparse.html)
```python
# The Python argparse module provides functions for parsing the input arguments passed to the script.

import argparse

# Add parser
parser = argparse.ArgumentParser(description = 'Demo of argparse')
# Add arguments
parser.add_argument("Demo Parser", help="display a demo parser")
# return parse result from input arguments
args = parser.parse_args()

# run with python3 demo_argparse.py -h
# it will show the help message
```

- [Collections module](https://docs.python.org/3/library/collections.html)
```python
# The Python collections module offers specialized container datatypes as alternatives to Python's general-purpose built-in containers such as dict, list, set, and tuple.

from collections import *
# Queue data type
# Queue is a linear data structure that stores items in a first-in-first-out (FIFO) manner.
# deque can be used to add or remove elements from either end.
queue = deque()
queue.append('right')
queue.appendleft('left')
print(queue)    # deque(['left', 'right'])


# namedtuple creates tuple subclasses with named fields
Drink = namedtuple('Drink', 'product, ice, sugar')  # declare a namedtuple with name Drink and fields product, ice, sugar
order = Drink('Milk Tea', 'ice free', 'regular')    # create a drink object
# programmers can use field name or index to get value in the tuple
print(order.product)    # Milk Tea
print(order[1]) # ice free 


# ChainMap groups multiple dictionaries or other mappings together to create a single, updatable view.
# It also support regular dictionary operations like get, set, keys, items, pop, popitem etc.
# However, it differs from the typical dictionary update() method in that it does not merge the original dictionaries.
milk_tea = {
    'ice': 'ice free',
    'sugar':'regular'
}
soda = {
    'ice': 'regular',
    'flavour': 'lemon'
}
drinks = ChainMap(milk_tea, soda)
print(drinks)   # ChainMap({'ice': 'ice free','sugar':'regular'}, {'ice':'regular', 'flavour': 'lemon'})

# By default, any operation is operated on the first dictionary in the ChainMap.
drinks['ice'] = 'cold'
print(milk_tea) # {'ice': 'cold','sugar':'regular'}
# To operate different dictionaries, programmers can use the maps(index) method to specify the dictionary to be operated on.
drinks.maps[1]['ice'] = 'ice free'
print(soda) # {'ice': 'ice free', 'flavour': 'lemon'}


# defaultdict is a dictionary subclass that provides a default value for missing keys.
original = dict()
# defaultdict(object)
default = defaultdict(int)
print(default['a']) # 0
print(original['a']) # Raise KeyError: 'a'
```

- [Datetime module](https://docs.python.org/3/library/datetime.html)
```python
# The Python datetime module provides functions for manipulating dates and times.
import datetime

print(datetime.datetime.now())  # prints current date and time
# strptime(time, format) converts string to datetime object
# strftime(format) converts datetime object to string
time = '2024-02-18 23:31:21'
print(datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %I:%M:%S %p'))   # 2024-02-18 11:31:21 PM
```

- [Functools module](https://docs.python.org/3/library/functools.html)
```python
# The Python functools module is for higher-order functions which acts on or return other functions.
from functools import *

def demo(func):
    @wraps(func)
    def wrapper():
        func()
        print(func.__name__, 'is in wrapper')
    return wrapper

@demo
def test():
    """Demo purpose"""
    print('Hey')
    return None

# The wraps() decorator is employed to preserve the original function's name and docstring when the wrapper function is invoked. 
# Without the @wraps decorator, the __name__ would be "wrapper" and __doc__ would be None.
print(test.__name__)    # test
print(test.__doc__) # Demo purpose
```

- [Math Module](https://docs.python.org/3/library/math.html)
```python
# The Python math module contains numerous mathematical operations and constants.
import math
print(math.pi)           # 3.1415926, constant pi
print(math.sqrt(2))      # 1.41421, square root of 2
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base
```

- [Re Module](https://docs.python.org/3/library/re.html)
```python
# The Python re module provides regular expression for matching operations.
import re

# Define a pattern for searching
# Search for the characters that are not a-z
pattern = r'[^a-z]'
text = 'hello World!'

# search() will return the first match of the pattern in the text
print(re.search(pattern, text)) # <re.Match object; span=(5, 6), match=' '>
# The match() function searches from the beginning of the text and returns None as no match is found.
print(re.match(pattern, text))  # None
```

## Packages

In Python, modules can be grouped together into packages. A package is simply a directory of Python module files with an **\_\_init\_\_.py** file.

The folder structure of packages are as followings:

```sh
─ customized
    ├── __init__.py
    ├── demo.py
    └── test.py
```

**Example of \_\_init\_\_.py**
```python
# The __init__.py file allows the folder to be considered as a Python package

# To define the behavior of import all modules from packages
# In this case, the module not_included_module will not import if programmers write:
#   from customized import *
__all__ = ['calculator']


# In the following case, programmers can simplify the import statements to import all 
#   methods and classes from calculator.py in in their files
# Original: from customized.calculator import *
# Simplified: from customized import *
from customized.calculator import *
```

## Reference
- [30 Built-In Python Modules You Should Be Using](https://sunscrapers.com/blog/30-built-in-python-modules-you-should-be-using-now/)
