# Day10 - Error Types
[<< Day 9](../Day9/Day9.md)  |  [Day 11 >>](../Day11/Day11.md)

### Agenda
- [Python Error Types](#python-error-types)
  - [SyntaxError](#syntaxerror)
  - [NameError](#nameerror)
  - [IndexError](#indexerror)
  - [ModuleNotFoundError](#modulenotfounderror)
  - [AttributeError](#attributeerror)
  - [KeyError](#keyerror)
  - [TypeError](#typeerror)
  - [ImportError](#importerror)
  - [ValueError](#valueerror)
  - [ZeroDivisionError](#zerodivisionerror)

## Python Error Types

It is common for programmers to make typos or other common errors. When code fails to execute, the Python interpreter will show a message containing information on where the problem occurred and the type of error. In this section, we will look at the most common error types occurring in Python.

### SyntaxError
A SyntaxError occurs when programmers make a mistake in the structure of their code. For example, they may forget to close a parenthesis.

```python
Python 3.12.1 (main, Dec  7 2023, 20:45:44) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'Demonstrate SyntaxError'
  File "<stdin>", line 1
    print 'Demonstrate SyntaxError'
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>>
```

### NameError
A NameError occurs when a variable or function is not defined. For example, if we try to print a variable that has not been defined, we will get a _NameError_.

```python
Python 3.12.1 (main, Dec  7 2023, 20:45:44) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(HI)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'HI' is not defined
>>>
```

### IndexError
An IndexError occurs when we try to access an element in a sequence by an index that is out of range.

```py
Python 3.12.1 (main, Dec  7 2023, 20:45:44) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> nums = [2, 9, 12, 3, 45]
>>> print(nums[9])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```

### ModuleNotFoundError
ModuleNotFoundError is a subclass of ImportError and is introduced after Python 3.6. It occurs when we attempt to import a module that cannot be found.

```python
Python 3.12.1 (main, Dec  7 2023, 20:45:44) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import collection
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'collection'
>>>
```

### AttributeError
An AttributeError occurs when we try to access a method or attribute that does not exist.

```python
Python 3.12.1 (main, Dec  7 2023, 20:45:44) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import math
>>> print(math.PI)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
>>>
```

### KeyError
A KeyError occurs when we try to access a key in a dictionary that does not exist.

```py
Python 3.12.1 (main, Dec  7 2023, 20:45:44) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> countries = {
... 'Taiwan': 'Asia',
... 'France': 'Europe'
... }
>>> print(countries['USA'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'USA'
>>>
```

### TypeError
A TypeError occurs when we try to perform an operation or a function on an object of an incorrect type.

```py
Python 3.12.1 (main, Dec  7 2023, 20:45:44) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num = 5
>>> string = '12'
>>> print(num + string)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

### ImportError
An ImportError is raised for millions reason. The following shows an example.

```py
Python 3.12.1 (main, Dec  7 2023, 20:45:44) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from collections import functool
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'functool' from 'collections' (/opt/homebrew/Cellar/python@3.12/3.12.1_1/Frameworks/Python.framework/Versions/3.12/lib/python3.12/collections/__init__.py)
>>>
```

### ValueError
A ValueError occurs when we try to pass an invalid value to a function.

```py
Python 3.12.1 (main, Dec  7 2023, 20:45:44) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> int('Demo ValueError')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'Demo ValueError'
>>>
```

### ZeroDivisionError
A ZeroDivisionError occurs when we try to divide by zero.

```python
Python 3.12.1 (main, Dec  7 2023, 20:45:44) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
```
