# Day7 - Functions
[<< Day 6](../Day6/Day6.md)  |  [Day 8 >>](../Day8/Day8.md)

### Agenda
- [Functions](#functions)
    - [Function Declaring and Calling](#function-declaring-and-calling)
    - [Function with Default Parameters](#function-with-default-parameters)
    - [Function Passing Arguments](#function-passing-arguments)
    - [Arbitrary Number of Arguments](#arbitrary-number-of-arguments)
    - [Type Hint](#type-hint)
    - [Function as a parameter](#function-as-a-parameter)
    - [Lambdas](#lambdas)


## Functions
To avoid repeatedly use of the same code in a project, it is necessary to design a block of code to perform a certain task, which is the so-called 'function'. In python, programmers can use 'def' to create a custom function.

### Function Declaring and Calling 

- Function without return values
```python
# In Python, if programmers do not want to return any value, they can simply omit the return statement or explicitly return None.

# Function without parameters
def demonstrate_names():
    students = ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz']
    for student in students:
        print(student)
    # Although the return statement is omitted, this function will return None.
    # Whether to write 'return None' or not depends on the coding style of the project.

# calling a function
demonstrate_names ()

# Function with parameters
# The parameters are the variables that we pass to the function.
def multiply (num_1, num_2):
    print(num_1 * num_2)

multiply(3, 5) # 15
```

- Function with return values
```python
# In Python, programmers can return any type of value without defining a return type.

# Function without parameters
def demonstrate_names():
    students = ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz']
    return students.pop() if students else None

print(demonstrate_names()) # Liz

# Function with parameters
def multiply (num_1, num_2):
    return num_1 * num_2

print(multiply(3, 5)) # 15
```

### Function with Default Parameters
In some situations, programmers may want parameters to have default values when they invoke the function. These default values will be used if programmers do not pass any arguments when calling the function.

**Example:**

```python
def demonstrate_names (names = ['David', 'Melody']):
    for name in names:
        print(name)

demonstrate_names() # David Melody
```

### Function Passing Arguments
By default, passing arguments is done in the order from left to right. However, programmers can use keyword arguments to pass arguments in any order.

```python

def demonstrate_names(first_name, sur_name):
    print(f'{first_name} {sur_name}')

# Correct Name: David Lin
# If we pass the arguments in the wrong order, we will get an unexpected result.
demonstrate_names('Lin', 'David') # Lin David

# With keyword arguments, the order becomes irrelevant.
demonstrate_names(sur_name='Lin', first_name='David') # David Lin
```

### Arbitrary Number of Arguments
Programmers can pass an arbitrary number of arguments by prefixing '*' before the parameter name; the type of this parameter will be a tuple. Alternatively, programmers can use '**' before the parameter name to pass a dictionary of arguments.

- With prefix '*'
```python
# With the prefix '*', the parameters being passed into the function will not have any associated keywords.
# Programmers can only access the parameters by their index or iterate through the entire object.
def multiply_nums(*nums):
    total = 1

    for num in nums:
        total *= num
    return total if nums else 0

# Programmers can use unpacking operator '*' to pass an iterable object or simply pass a sequence of parameters
print(multiply_nums(2, 3, 5)) # 30
print(multiply_nums(*[2, 3, 5])) # 30
```

- With prefix '**'
```python
# With the prefix '**', the parameters being passed into the function will have associated keywords.
# But programmers can not diretly access the implicit keyword.
mappings = {
    'name': 'David',
    'interest': 'Workout'
}
def demonstrate_person(**mappings):

    for key, value in mappings.items():
        if key == 'name':
            print(f'Name is {value}')
        elif key == 'interest':
            print(f'Hobby is {value}')

# Programmers can use unpacking operator '**' to pass a dictionary object or simply pass a sequence of key-value parameters
demonstrate_person(**mappings)
demonstrate_person(name='David', interest='Workout')
```

### Type Hint
Starting from Python 3.5, programmers can use type hints to specify the data types for parameters and return values.
- For more information, please refer to [Support for type hints](https://docs.python.org/3/library/typing.html)

```python
# Type hints with default values
def multiply(num_1: int = 0, num_2: int = 0) -> int:
    return num_1 * num_2
print(multiply())   # 0
```

Starting from Python 3.12, programmers can use type aliases to define a type for parameters and return values.

```python
# type aliases is only available in Python 3.12 and above.
# For backwards compatibility, type aliases can also be created through simple assignment:
# Vector = list[int]
type Vector = list[int]

def demonstrate_names(names: Vector = ['David', 'Melody']) -> Vector:
    names.append('Chien')
    return names
print(demonstrate_names())   # ['David', 'Melody', 'Chien']
```

### Function as a parameter

```python
def square (n):
    return n ** 2
def root (n):
    return n ** 0.5
def calculate(func, num):
    return func(num)
print(calculate(square, 5)) # 25
print(calculate(root, 5)) # 2.236
```

### Lambdas
Lambda expressions are used to create anonymous functions, which yields an anonymous function object.

```python
# syntax
# lambda parameters: expression
# It is equivalent to the following:
def <lambda>(parameters):
    return expression


# Example

nums = [10, -19, 3, -9, 7]

# In Day 3, we had learnt a list method sort(key = None, reverse=False)
# By default, sort() method will sort the list in ascending order based on the elements' values.
nums.sort()
print(nums) # [-19, -9, 3, 7, 10]

# However if we want to sort the list based on the elements' square values, we can use the key parameter.
nums.sort(key= lambda num: num ** 2)
print(nums) # [3, 7, -9, 10, -19]
```
