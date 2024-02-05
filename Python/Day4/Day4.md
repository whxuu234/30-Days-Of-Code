# Day3 - Mutable Data Types
[<< Day 3](../Day3/Day3.md)  |  [Day 5 >>](../Day5/Day5.md)

### Agenda
- [String](#string)
    - [String Creation](#string-creation)
    - [String Accessing](#string-accessing)
    - [String Joining](#string-joining)
    - [Escape Sequence](#escape-sequence)
    - [String Formatting](#string-formatting)
    - [String Unpacking](#string-unpacking)
    - [String Slicing](#string-slicing)
    - [String Reversing](#string-reversing)
    - [String Methods](#string-methods)

- [Tuple](#tuple)
    - [Tuple Creation](#tuple-creation)
    - [Tuple Accessing](#tuple-accessing)
    - [Tuple Slicing](#tuple-slicing)
    - [Tuple Joining](#tuple-joining)
    - [Tuple Methods](#tuple-methods)

## String
String is a collection of letters and is **immutable** object in python. Any data under single, double or triple quote are strings.

### String Creation

- Creating string with quote
```python
greeting = 'Nice to meet you!'  # single or double quote is ok
print(greeting)             # Nice to meet you!

# Using triple quote(''' or """) to create multiple line string

multi_string = '''I love Autumn.
I have a great family.
'''
print(multi_string)
```

### String Accessing
Same as list, string can be accessed by index.

- Positive index
```python
names = 'David Melody Jonas Jane Chien Liz'
# Format: string[index]
print(names[0])    # D
print(names[4])  # d
```

- Negative index
```python
names = 'David Melody Jonas Jane Chien Liz'
# The last element
print(names[-1])    # z

# The first element
print(names[-len(names)])   # D
```

### String Joining

- Concatenating string with "+"
```python
boy = 'David'
girl = 'Melody'
sep = ' '
print(boy + sep + girl) # David Melody
```

- Concatenating string with "*"
```python
repeated = 'David' * 5
print(repeated) # DavidDavidDavidDavidDavid
```

### Escape Sequence
In programming languages '\' followed by a character is an escape sequence. 

- Some common escape sequences
```python
# Printing new line
print('I am sleepy!\nI am tired!')

# Printing tab(8 spaces)
print('I am exciting\twhat about you?') # I am exciting       what about you?

# Printing back slash
print('Demonstration of back slash! (\\)')  # Demonstration of back slash! (\)

# Printing single quote
print('His name is \'David\'') # His name is 'David'

# Printing double quote
print('Her name is \"Melody\"') # Her name is "Melody"
```


### String Formatting
There are several ways to format string in python.

- '%' operator
```python
# %s - String 
boy = 'David'
girl = 'Melody'
print('Boy %s and girl %s are dating.' %(boy, girl))    # Boy David and girl Melody are dating.
# %s can accept not only strings but also other data types that can be converted to strings.
countries = ['Taiwan', 'Janpan', 'France']
print('List of countries:%s' % (countries)) # List of countries:['Taiwan', 'Janpan', 'France']

# %d - Integers
# %f - Floating numbers
radius = 5
pi = 3.14159
area = pi * pow(radius, 2)
# %.(digit)f" means number of digits decimal precision
print('The area of circle with a radius %d is %.2f.' %(radius, area)) # The area of circle with a radius 5 is 78.54.
```

- format()
```python
# After python3, programmers can use format method to format string
boy = 'David'
girl = 'Melody'
print('Boy {} and girl {} are dating.'.format(boy, girl))    # Boy David and girl Melody are dating.

radius = 5
pi = 3.14159
area = pi * pow(radius, 2)
# :.(digit)f" means number of digits decimal precision
print('The area of circle with a radius {} is {:.2f}.'.format(radius, area)) # The area of circle with a radius 5 is 78.54.
```

- format_map()
```python
# After python3, programmers can use format_map method to format string
mappings = {
    'boy': 'David',
    'girl': 'Melody'
}

print('Boy {boy} and girl {girl} are dating.'.format_map(mappings))    # Boy David and girl Melody are dating.
```

- f-strings
```python
# After python3.6, programmers can use f-strings to format string
boy = 'David'
girl = 'Melody'
print(f'Boy {boy} and girl {girl} are dating.')    # Boy David and girl Melody are dating.

radius = 5
pi = 3.14159
area = pi * pow(radius, 2)
# (variable):.(digit)f" means number of digits decimal precision
print(f'The area of circle with a radius {radius} is {area:.2f}.') # The area of circle with a radius 5 is 78.54.
```

### String Unpacking
String can be unpacked into different variables.

```python
language = 'English'
a, b, c, *remain = language
print(a) # E
print(b) # n
print(c) # g
print(remain) # ['l', 'i', 's', 'h']
```

### String Slicing
String can be sliced by index.

- Positive index
```python
names = 'David Melody Jonas Jane Chien Liz'
# Format: string[start_index:start_index + length], empty means from the start or to the end
# All elements
print(names[0:]) # David Melody Jonas Jane Chien Liz

# Certain range
print(names[0:5])  # David

# The third argument indicates that the index will verify by its specified number
print(names[0:8:2])    # DvdM
```

- Negative index
```python
names = 'David Melody Jonas Jane Chien Liz'
# -1 means the last element
# All elements
print(names[-len(names):]) # David Melody Jonas Jane Chien Liz

# Certain range
print(names[-len(names): -len(names) + 5])  # David

# The third argument indicates that the index will verify by its specified number
print(names[-len(names):10:3])    # DiMo
```

### String Reversing
We can reverse string simply by slicing method

```python
names = 'David Melody Jonas Jane Chien Liz'
print(names[::-1])  # ziL neihC enaJ sanoJ ydoleM divaD
```

### String Methods
There are many useful methods to handle strings in python. 

- capitalize()
```python
# Converts the first letter of the string to capital
greetings = 'hello, world!'
print(greetings.capitalize()) # Hello, world!
```

- casefold()
```python
# Just like lower(), which converts string to lowercase. 
# However, casefold support non-ascii to regularize the string, whereas lower only support ascii
greetings = 'HELLO, world!'
print(greetings.casefold()) # hello, world!

german_letter = "ß"
print(german_letter.casefold()) # ss
print(german_letter.lower())    # ß
```

- center()
```python
# center(width, fillchar), put the original string in the center, if the length of the string is less than the width, fillchar will be used to fill the string to the width.
weather = 'It is windy day.'
print(weather.center(40, '*'))  # ***************It is windy day.***************
```

- count()
```python
# count(substring, start, end) returns occurrences of substring in string between starting index and ending index.
description = 'Taiwan is a beautiful country'
print(description.count('i', 0, 6)) # 1
print(description.count('ful')) # 1
```

- encode()
    [Codec registry and base classes](https://docs.python.org/3/library/codecs.html#standard-encodings)
```python
# encode(encoding='utf-8', errors='strict') returns the string encoded to bytes.
# It is used to transmit textual data and can prevent loss of data.
description = 'Taiwan is a beautiful country'
print(description.encode()) # b'taiwan is a beautiful country'
```

- endswith()
```python 
#  endswith(suffix, start, end) checks if a string ends with a specified string
description = 'Taiwan is a beautiful country'
print(description.endswith('ry'))   # True
print(description.endswith('ful', 0, 6)) # False
```

- startswith()
```python
#  startswith(suffix, start, end) checks if a string starts with a specified string
description = 'Taiwan is a beautiful country'
print(description.startswith('Taiwan'))   # True
print(description.startswith('ful', 0, 6)) # False
```

- expandtabs()
```python
#  expandtabs(tabsize=8) replaces tab character with spaces, default tab size is 8.
description = 'Taiwan\tis\ta\tbeautiful\tcountry'
print(description.expandtabs()) # Taiwan   is    a    beautiful    country
print(description.expandtabs(10))   # Taiwan       is        a        beautiful        country
```

- find()
```python
# find(sub, start, end) returns the index of the first occurrence of a substring, if not found returns -1
description = 'Taiwan is a beautiful country'
print(description.find('i'))  # 2
print(description.find('i', 3, 10)) # 7   
```

- rfind()
```python
# rfind(sub, start, end) returns the index of the last occurrence of a substring, if not found returns -1
description = 'Taiwan is a beautiful country'
print(description.find('i'))  # 17
print(description.find('i', 0, 10)) # 7   
```

- index()
```python
# index(sub, start, end) just like find() method, but if the substring is not found it raises a valueError. 
description = 'Taiwan is a beautiful country'
print(description.index('i'))  # 2
print(description.index('g', 0, 10)) # Raise ValueError
```

- rindex()
```python
# rindex(sub, start, end) just like rfind() method, but if the substring is not found it raises a valueError.
description = 'Taiwan is a beautiful country'
print(description.rindex('a'))  # 14
print(description.rindex('uti', 0, 10)) # Raise ValueError
```

- isalnum()
```python
# isalnum() checks whether all character in string are alphanumeric character or not
# alphanumeric character: 0-9, A-Z, a-z
description = 'Thisisalphanumeric'
print(description.isalnum()) # True

description = 'Itis2024'
print(description.isalnum()) # True

description = 'This is not alphanumeric'
print(description.isalnum()) # False, space is not an alphanumeric character
```

- isalpha()
```python
# isalpha() checks if all string elements are alphabet characters
# alphabet characters: A-Z, a-z
description = 'Thisisalphanumeric'
print(description.isalpha()) # True

description = 'Itis2024'
print(description.isalpha()) # False, 2024 is not an alphabet character

description = 'This is not alphanumeric'
print(description.isalpha()) # False, space is not an alphanumeric character
```

- isdecimal()
```python
#  isdecimal() checks if all characters in a string are decimal (0-9)
description = 'Thisisalphanumeric'
print(description.isdecimal()) # False

description = '2024'
print(description.isdecimal()) # True

description = '\u00B2'
print(description.isdecimal()) # False, unicode character is not a decimal character
```

- isdigit()
```python
# isdigit() checks if all characters in a string are numbers (0-9 and some unicode characters for numbers)
description = 'Thisisalphanumeric'
print(description.isdigit()) # False
description = '2024'
print(description.isdigit())   # True
description = '\u00B2'
print(description.isdigit())   # True
```

- isnumeric()
```python
# isnumeric() checks if all characters in a string are numbers or number related (0-9 and more unicode characters than isdigit like ½)
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False
```

- isascii()
```python
# isascii() checks if all characters in a string are ASCII
num = '10'
print(num.isascii()) # True
num = '\u00BD' # ½
print(num.isascii()) # False
num = '!'
print(num.isascii()) # True
```

- isidentifier()
```python
# isidentifier() checks whether a string is valid variable name
# Valid variable name: only contain (a-z) and (0-9), or underscores (_) and can not start with number
description = 'height_of_student'
print(description.isidentifier()) # True
description = '15_height_of_student'
print(description.isidentifier()) # False, because it starts with number
```

- islower()
```python
# islower() checks if all alphabet characters in the string are lowercase
description = 'it is all lower case'
print(description.islower()) # True
description = 'It is capitalize'
print(description.islower()) # False
```

- isprintable()
```python
# islower() checks if all characters in the string are printable
description = 'Everything is printable'
print(description.isprintable()) # True
description = 'Special\tsymbol\tis\tnot\tprintable'
print(description.isprintable()) # False
```

- isupper()
```python
# isupper() checks if all alphabet characters in the string are uppercase
description = 'it is all lower case'
print(description.isupper()) # False
description = 'IT IS ALL UPPER CASE'
print(description.isupper()) # True
```

- isspace()
```python
# isspace() checks if all characters in the string are space
description = 'There are some characters'
print(description.isspace()) # False
description = '\t\t'
print(description.isspace()) # True
```

- istitle()
```python
# istitle() checks if all space seperated word in the string are capitalize
description = 'A Title'
print(description.istitle()) # True
description = 'It is not a title'
print(description.istitle()) # False
```

- join()
```python
# join(iterable) returns a string which is concatenated by the given string or space
countries = ['Taiwan', 'America', 'France']
print('-'.join(countries))  # Taiwan-America-France
```

- ljust()
```python
# ljust(width, fillchar) is similar to center(), but instead places the original string to the left, filling the remaining length of the string with fillchar, with the default fillchar being a space.
weather = 'It is windy day.'
print(weather.ljust(40, '*'))  # It is windy day.************************
```

- strip()
```python
# strip() returns a copy string which removes given characters in the string.
# Remove from the starting and ending of the string until mismatch occurred.
weather = 'It is windy day.'
print(weather.strip('Iday.')) #  t is windy
```

- lstrip()
```python
# lstrip() returns a copy string which removes given characters in the string.
# Remove from the starting of the string until mismatch occurred.
weather = 'It is windy day.'
print(weather.lstrip('Iday.')) #  i is windy day.
```

- rstrip()
```python
# rstrip() returns a copy string which removes given characters in the string.
# Remove from the ending of the string until mismatch occurred.
weather = 'It is windy day.'
print(weather.rstrip('Iday.')) #  It is winday
```

- replace()
```python
# replace() replaces substring with a given string
weather = 'It is windy day.'
print(weather.replace('windy', 'shinny')) # It is shinny day.
```

- lower()
```python
# lower() returns a copy string which transfer all alphabet characters to lowercase
weather = 'IT IS WINDY DAY.'
print(weather.lower())  # it is windy day.
```

- upper()
```python
# upper() returns a copy string which transfer all alphabet characters to uppercase
weather = 'it is windy day.'
print(weather.upper())  # IT IS WINDY DAY.
```

- split()
```python
# split(sep=' ') returns a list of string, which use sep as a separator and space by default
weather = 'it is windy day.'
print(weather.split())  # ['it', 'is', 'windy', 'day.']
print(weather.split('is')) # ['it ', 'windy day.']
```

- partition()
```python
# partition(sep) separates the string into three parts: the part before the separator, the separator itself, and the part after the separator.returns a tuple of string,
weather = 'it is windy day.'
print(weather.partition(' '))  # ('it', ' ', 'is windy day.')
print(weather.partition('is')) # ('it ', 'is', ' windy day.')
```

- title()
```python
# title() returns a title format string
weather = 'it is windy day.'
print(weather.title())  # It Is Windy Day.
```

- swapcase()
```python
# swapcase() converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
weather = 'It Is Windy day.'
print(weather.swapcase())   # iT iS wINDY dAY.
```






## Tuple
Tuple is a collection of items and is **immutable** object in python and it can store different type of data.

### Tuple Creation

- Creating tuple with round brackets, (). 
```python
# Empty tuples
empty = ()
empty = tuple()

# With initial values
countries = ('Taiwan', 'France', 'Japan')
```

### Tuple Accessing
Same as string, tuple can be accessed by index.

- Positive index
```python
names = ('David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz')
# Format: string[index]
print(names[0])    # David
```

- Negative index
```python
names = ('David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz')
# The last element
print(names[-1])    # Liz

# The first element
print(names[-len(names)])   # David
```

### Tuple Slicing
Tuple can be sliced by specifying a range of indexes

- Positive index
```python
names = ('David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz')
# Format: string[start_index:start_index + length], empty means from the start or to the end
# All elements
print(names[0:]) # ('David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz')

# Certain range
print(names[0:2])  # ('David', 'Melody')

# The third argument indicates that the index will verify by its specified number
print(names[0:6:2]) # ('David', 'Jonas', 'Chien')
```

- Negative index
```python
names = ('David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz')
# -1 means the last element
# All elements
print(names[-len(names):]) # ('David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz')

# Certain range
print(names[-len(names): -len(names) + 2])  # ('David', 'Melody')

# The third argument indicates that the index will verify by its specified number
print(names[-len(names):-1:3])    # ('David', 'Jane')
```

### Tuple Joining 

- Concatenating string with "+"
```python
friends = ('David', 'Melody', 'Chien')
classmates = ('Jonas', 'Jane', 'Liz')
print(friends + classmates) # ('David', 'Melody', 'Chien', 'Jonas', 'Jane', 'Liz')
```

- Concatenating string with "*"
```python
repeated = ('David') * 5
print(repeated) # ('David', 'David', 'David', 'David', 'David')
```

### Tuple Methods
Tuple has few methods.

- count()
```python
# count(item) counts the number of a specified item in a tuple
names = ('David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz')
print(names.count('David'))
```

- index()
```python
# index(item, sta, end) returns the first occurrence index of a specified item between start and end index in a tuple
names = ('David', 'Melody', 'David', 'Jane', 'Chien', 'Liz')
print(names.index('David', 1, 5)) # 2
```
