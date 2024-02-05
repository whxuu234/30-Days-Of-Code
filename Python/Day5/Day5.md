# Day5 - Conditionals
[<< Day 4](../Day4/Day4.md)  |  [Day 6 >>](../Day6/Day6.md)

### Agenda
- [String](#List)
    - [String Creation](#string-creation)
    - [String Accessing](#string-accessing)
    - [String Joining](#string-joining)
    - [Escape Sequence](#escape-sequence)
    - [String Formatting](#string-formatting)
    - [String Unpacking](#string-unpacking)
    - [String Slicing](#string-slicing)
    - [String Reversing](#string-reversing)
    - [String Methods](#string-methods)

- [Tuple](#Set)
    - [Tuple Creation](#tuple-creation)
    - [Tuple Accessing](#tuple-accessing)
    - [Tuple Slicing](#tuple-slicing)
    - [Tuple Joining](#tuple-joining)
    - [Tuple Methods](#tuple-methods)

## Conditionals
Conditional statement is the very crucial part of any programming language. It allows us to execute a block of code only if a condition is true.

### If Condition
In the following example, the condition was true and the block code was executed.

```python
num = 10
if type(num) == int:
    print(f'Number {num} is an integer.')
```

### If Else
If condition is false in the first block, the code block in else block will be executed.

```python
name = 'David'
if type(name) == int:
    print(f'Variable {name} is an integer.')
else:
    print(f'Variable {name} is an string.')
```

### If Elif Else
In case of multiple conditions, we can use if-elif-else condition.

```python
num = 62
if num > 100:
    print(f'Number {num} is greater than 100.')
elif num < 50:
    print(f'Number {num} is lower than 50.')
else:
    print(f'Number {num} is between 50 and 100.')
```

### Short Hand
Python does not support the Ternary operation, but it provides Short Hand instead.

```python
num = 62
print('num is greater than 50') if num > 50 else print('num is smaller than 50') # num is greater than 50
```

### Nested Conditions
Although we can use nested conditions, it is not recommended. We can avoid writing nested condition by using logical operator and.

```python
num = 63
if num > 0:
    if num % 2 == 0:
        print('num is a positive and even number.')
    else:
        print('num is a positive and odd number.')
elif num == 0:
    print('num is zero')
else:
    print('num is a negative number')
```

### If Condition and Logical Operators

- 'and' operator
```python
num = 63
if num > 0 and num % 2 == 0:
    print('num is a positive and even number.')
elif num > 0 and num % 2 != 0:
    print('num is a positive and odd number.')
elif num == 0:
    print('num is zero')
else:
    print('num is a negative number')
```

- 'or' operator
```py
name = 'David'
age = 100
if name == 'John' or age >= 50:
    print('This guy is old.')
else:
    print('This guy is young.')
```

🌕 You are doing great.Never give up because great things take time. You have just completed day 9 challenges and you are 9 steps a head in to your way to greatness. Now do some exercises for your brain and muscles.

### Switch Case
Python supports switch-case after python 3.10 to avoid lengthy if-elif-else statements

```python
option = 4
match option:
    case 1:
        print('Option 1: Turn right')
    case 2:
        print('Option 2: Turn left')
    case 3:
        print('Option 3: Turn around')
    case 4:
        print('Option 4: Go straight')
    case _:
        print('Not supported option')
```

Before python 3.10, programmers can use the following most common ways to implement switch case

- Table-Driven Approach
```python
seasons = {
    1: "Spring",
    2: "Summer",
    3: "Autumn",
    4: "Winter"
}
season = 3
print(seasons.get(season, "Invalid option"))
```

- Table-Driven Approach plus Function definition
```python
def spring():
    print('String')
def summer():
    print('Summer')
def autumn():
    print('Autumn')
def winter():
    print('Winter')
def default():
    print('Invalid Season')
# Remember not to add '()' after function, otherwise it will be executed
seasons = {
    1: spring,
    2: summer,
    3: autumn,
    4: winter
}
season = 3
func = seasons.get(season, default)
func()  # Autumn
```