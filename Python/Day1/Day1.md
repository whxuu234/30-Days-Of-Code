# Day1 - Basic
### Agenda
- [Indentation](#Indentation)
- [Comment](#Comment)
- [Data types](#Data-types)
    - [Number](#Number)
    - [String](#String)
    - [Bytes](#Bytes)
    - [Boolean](#Boolean)
    - [List](#List)
    - [Set](#Set)
    - [Tuple](#Tuple)
    - [Dictionary](#Dictionary)



## Indentation
There are two ways of indentation, including "Tab" and "4 spaces". Remember to keep indentation the same since the mixture might cause **Indentation Error**

```python
# Indentation demonstration
if True:
    print("Hey, remember to indent")
    # Comment is recommended to indent in the same order with code
```

## Comment
Example: Single Line Comment
```python
    # Life is tough
    # Python is cool
```

Example: Multiline Comment
```python
"""
Life is tough
Python is cool
"""
```

## Data types
There is a fairly important concept in Python variable. It is called **Mutable** and **Immutable**.
- Mutable
    - If an object's value can be changed after it has been created, we would say it is **mutable**.
    - Including: *List, Set, Dictionary, Bytearray, Array*
- Immutable
    -  If an object's value cannot be changed after it has been created, we would say it is **immutable**.
    - Including: *Integers, Floating point numbers, Complex, Boolean, Strings, Tuples, Frozenset, Bytes*

### Number
All data types in number are **immutable**, which means if a variable is assigned with a number data type, it cannot be changed after it has been created. If programmers assigned a new value to it, it will have different identification value  in python.

```python
# Integer
#   Including negative, zero and positive numbers
#   Example: ... -1, 0, 1, ...

# Float
#   Example: ... -2.1, 0.1, 1.5, 3.0 ...

# Complex
#   Example: 1 + j, 2 + 4j

int_num = 5
float_num = 5.5
complex_num = 1 + j

# id() function return the unique identification value of a variable
print("Initial identification values")
print(id(int_num))
print(id(float_num))
print(id(complex_num))

# Changing the value of a variable and the identification value will change too
int_num = 10
float_num = 7.5
complex_num = 2 + 4j

print("Identification values after assigining new values")
print(id(int_num))
print(id(float_num))
print(id(complex_num))
```

### String
A combination of a sequence of characters included in single or double quote, which is **immutable**. Using triple quotes to cover a string which is more than one sentence.

```python
single_quote = 'Hey, this is single-quote string'
double_quote = "Hey, this is single-quote string"
multi_line_sentence = """Hey, this is a multi line sentence.
We use triple double quotes here"""
multi_line_sentence_2 = '''Hey, this is also a multi line sentence.
But we use triple single quotes here.'''

# Immutable demonstration
#   Changing the value of a string variable will change the identification value
#   Since string is immutable, it doesn't support item assignment, e.g. string[0] = "A" will cause error

dem_str = "Hey, I'm an example"
print(id(dem_str))
dem_str = "Hey, I'm an example - Changed"
print(id(dem_str))
# This will cause error
dem_str[0] = "A" 
```

### Bytes
Bytes is a sequence of binary data. It can save storage and prevent data lost during the transportaion. Bytes is an **immutable** object.

```python
# Bytes is used to represent information in binary form, which is a machine readable data
bytes_str = b"Hey, Python is great"
# If we print the particular value in a bytes string, we will see the ASCII value of that character
print(bytes_str[0])
# It can be transferred back to the human readable form by using decode() function
print(bytes_str.decode("utf-8"))

```
### Boolean
If a boolean situation is **True**, which means the situation is logically valid. If a boolean situation is **False**, which means the situation is logically invalid. Boolean is an **immutable** object.
```python
# Boolean is either True or False.
# Note: T and F should be always uppercase.
bool_true = True
bool_false = False

# A condition is True, so the program will execute the code inside the if statement
if bool_true:
    print("This is a valid situation")
# A condition is False, so the program will execute the code inside the else statement instead
if bool_false:
    print("This code won't be executed")
else:
    print("This is a invalid situation")
```
### List
The concept of list is similar to array in C, but Python list allows to store different data type items. List is a **mutable** object.

```python
# List supports item assignment. Since List is mutable, its identification value remains the same after assigning
dem_list = [0, 1, 2, 3, 4 ,5]
print(id(dem_list))
dem_list[0] = 100
print(id(dem_list))

# If we assign a list variable to a new variable, the new variable will have the same identification value.
# Therefore, the new variable will be a reference to the same list object
dem_list_2 = dem_list
dem_list_2[0] = 1000
# We modify the value of dem_list_2 also modify the value of dem_list
print(dem_list_2)
print(dem_list)
```

### Dictionary
Dictionary is a collection of data in a key value pair format. Dictionary is a **mutable** object.
```python
# Dictionary supports item assignment. Dictionary is mutable, so its identification value remains the same after assigning
dem_dict = {
"Day":1,
"Language": "Python",
"Single": True
}
print(id(dem_dict))
dem_dict["Day"] = 100
print(id(dem_dict))

# Additionally, the new variable will be a reference to the same dictionary object
dem_dict_2 = dem_dict
dem_dict_2["Day"] = 1000
# We modify the value of dem_dict_2 also modify the value of dem_dict
print(dem_dict_2)
print(dem_dict)
```

### Tuple
Tuple has very similar characteristics like list, but Tuple is an **immutable** object.

```python
dem_tuple = ("David", "Melody", "John")
# Immutable demonstration
#   Changing the value of a tuple variable will change the identification value
#   Since tuple is immutable, it doesn't support item assignment, e.g. tuple[0] = "A" will cause error
print(id(dem_tuple))
dem_tuple = ("Overcast", "Sunny", "Rainy")
print(id(dem_tuple))
# We cannot change the value of a tuple, this will cause error
dem_tuple[0] = "Luke" 
```

### Set
In Python, Set is similar totuple and list, but it only stores unique items. Set is a **mutable** object.
```python
dem_set = {2, "Hey", 3.5, "Hey"}
# Although we have two string "Hey" in the set, the set only stores unique items, so dem_set only has one "Hey"
print(dem_set)
# Set doesn't supports item assignment. Since Set is mutable, its identification value remains the same after add() or remove() operation
print(id(dem_set))
dem_set.add(4)
print(id(dem_set))

# Additionally, the new variable will be a reference to the same set object
dem_set_2 = dem_set
dem_set_2.add("Hi")
# We modify the value of dem_set_2 also modify the value of dem_set
print(dem_set)
print(dem_set_2)
```

### frozenset
Just like Set, Frozenset only stores unique items. But FrozenSet is a **immutable** object since it's "frozen", it cannot change its values once it is created.
```python
dem_frset = frozenset({"apple", "banana", "cherry", "cherry"})
# Just like set, it only stores unique values so dem_frset only has one "cherry"
print(dem_frset)
# Frozenset is immutable, so its value cannot be modified.
# This operation will cause error
dem_frset.add("Oops!")
```