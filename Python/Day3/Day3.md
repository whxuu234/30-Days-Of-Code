# Day3 - Mutable Data Types
[<< Day2](../Day2/Day2.md)  |  [Day 4 >>](../Day4/Day4.md)

### Agenda
- [List](#List)
    - [List Creation](#list-creation)
    - [List Accessing](#list-accessing)
    - [List Unpacking](#list-unpacking)
    - [List Slicing](#list-slicing)
    - [List Checking](#list-checking)
    - [List Assignment](#list-assignment)
    - [List Adding](#list-adding)
    - [List Removing](#list-removing)
    - [List Information](#list-information)
    - [List Copying](#list-copying)
    - [List Joining](#list-joining)
    - [List Sorting](#list-sorting)
- [Set](#Set)
    - [Set Creation](#set-creation)
    - [Set Accessing](#set-accessing)
    - [Set Checking](#set-checking)
    - [Set Updating](#set-updating)
    - [Set Removing](#set-removing)
    - [Set Joining](#set-joining)
- [Dictionary](#Data-types)
    - [Dictionary Creation](#dictionary-creation)
    - [Dictionary Accessing](#dictionary-accessing)
    - [Dictionary Updating](#dictionary-updating)
    - [Dictionary Removing](#dictionary-removing)
    - [Dictionary Copying](#dictionary-copying)
    - [Dictionary Checking](#dictionary-checking)


## List
A collection which is **mutable** and can store different data types in the same list.

### List Creation

- Creating list by built-in function
```python
# built-in function list(iterable)
# Empty list
empty = list()
# List with elements from 0 to 9
numbers = list(range(10))
```

- Creating list by square brackets, []
```python
# Empty list
empty = []
# List with initial values
numbers = [1, 2]
```

- List can have items of different data types
```python
lst = [1, "Hey", True]
```

### List Accessing
Python support positive and negative index to visit list elements

- Positive index
```python
names = ['David', 'Melody', 'Jonas', 'Jane']
# Index is equivalent to the order minus one.
# First element
print(names[0])     # David
# Second element
print(names[1])     # Melody

# Last element
print(names[3])     # Jane
```

- Negative index
```python
names = ['David', 'Melody', 'Jonas', 'Jane']
# The index equals to the reverse counting order.
# First element
print(names[-4])     # David
# Second element
print(names[-3])     # Melody

# Last element
print(names[-1])     # Jane
```

### List Unpacking
List is a iterable object and python supports unpacking iterable object 

```python
names = ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz']
# * can be used as unpacking operator in python
bf, gf, *others, friend = names 
print(bf)    # David
print(gf)    # Melody
print(others)     # ['Jonas', 'Jane', 'Chien']
print(friend)     # Liz
```

### List Slicing
Lists can be sliced by specifying the index range, accepting both positive and negative numbers.

- Positive index
```python
names = ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz']
# Format: list[start_index:start_index + length]
# All elements
print(names[0:6]) # ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz']

# Certain range
print(names[1:4])  # ['Melody', 'Jonas', 'Jane']

# If the second number is empty, it means start from the first number to the end
print(names[0:])   # ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz']

# The third argument indicates that the index will verify by its specified number
print(names[0:4:2])    # ['David', 'Jonas']
```

- Negative index
```python
names = ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz']
# Format: list[start_index:start_index + length]
# All elements
print(names[-6:]) # ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz']

# Certain range
print(names[-5:-2])  # ['Melody', 'Jonas', 'Jane']

# The third argument indicates that the index will verify by its specified number
print(names[::-1])  # ['Liz', 'Chien', 'Jane', 'Jonas', 'Melody', 'David']
print(names[4:0:-1])    # ['Chien', 'Jane', 'Jonas', 'Melody']
```

### List Checking
python can simply use **in** to check whether an item in an iterable object or not
```python
names = ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz']
print('David' in names) # True
print('Jack' in names) # False
```

### List Assignment
Since list is **mutable** object, it accepts item assignment

```python
names = ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz']

names[3] = 'Alex'
print(names) # ['David', 'Melody', 'Jonas', 'Alex', 'Chien', 'Liz']

names[-2] = 'Shu'
print(names) # ['David', 'Melody', 'Jonas', 'Alex', 'Shu', 'Liz']
```

### List Adding
List support three methods to add elements
- append()
```python
# append(item)
# append method will add element to the end of list, return None
names = ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz']
names.append('Jack')
print(namex) # ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz', 'Jack']
```

- insert()
```python
# insert(index, item)
# insert method can insert element to specific index, return None
names = ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz']
names.insert(2, 'Agnes')
print(names) # ['David', 'Melody', 'Agnes', 'Jonas', 'Jane', 'Chien', 'Liz']
```

- extend()
```python
# extend(iterable)
# extend method can extend an iterable object to the end of the list, return None
names = ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz']
new = ['Alex', 'Una']
names.extend(new)
print(names) # ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz', 'Alex', 'Una']
names.extend('Wu')
print(names) # ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz', 'Alex', 'Una', 'W', 'u']
# Only iterable object can be extended, otherwise it will raise TypeError
names.extend(100) # Raise TypeError since integer is not an iterable object
```

### List Removing
List support three methods to remove elements

- pop()
```python
# pop(index)
# pop method will remove index element from the list(remove the last one by default) and return the popped element
names = ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz']
print(names.pop()) # Liz
```

- remove()
```python
# remove(item)
# remove method removes the first occurance of a specified item from a list
names = ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz', 'Jonas']
names.remove('Jonas')
print(names) # ['David', 'Melody', 'Jane', 'Chien', 'Liz', 'Jonas']
```

- clear()
```python
# clear method delete all items in list, return None
names = ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz']
names.clear()
print(names) # []
```

### List Information
Python provides two method for getting items information

- index()
```python
# index(x) method returns the index of the first occurance of x in the list
names = ['David', 'Melody', 'Jonas', 'Liz', 'Jane', 'Chien', 'Liz']
print(names.index('Liz')) # 3

# When using slicing, the index will be the first occurance of x in the slice
print(names[1:6].index('Liz')) # 2
```

- count()
```python
# count(x) method returns the times of occurance of x in the list
names = ['David', 'Melody', 'Melody', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz']
print(names.count('Melody')) # 3
```

### List Copying
In Python, assigning **mutable object** to another variable assigns the reference of it. Consequently, modifications made to the new variable will affect the original one. To mitigate this, Python offers a copy() method. Nevertheless, if item within the list is also a mutable object, modification to it will also impact the item in original list.
```python
names = ['David', 'Melody', 'Jonas', 'Jane', 'Chien', ['Liz']]

new = names.copy()
new.append('Alex')
print(names) # ['David', 'Melody', 'Jonas', 'Jane', 'Chien', ['Liz']]
print(new) # ['David', 'Melody', 'Jonas', 'Jane', 'Chien', ['Liz'], 'Alex']

# Since the item ['Liz'] is a mutable object, modification to it will also impact the item in original list
new[-2].append('Una')
print(names) # ['David', 'Melody', 'Jonas', 'Jane', 'Chien', ['Liz', 'Una']]
print(new) # ['David', 'Melody', 'Jonas', 'Jane', 'Chien', ['Liz', 'Una'], 'Alex']
```

### List Joining
Python supports joining lists by `+, *` operator and list comprehension

```python
names = ['David', 'Melody']
friends = ['Alex', 'Una']

names += friends
print(names)    # ['David', 'Melody', 'Alex', 'Una']

names *= 2
print(names)    # ['David', 'Melody', 'Alex', 'Una', 'David', 'Melody', 'Alex', 'Una']

nums = [num for num in range(10)]
print(nums) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### List Sorting
In Python, programmers can sort the elements or reverse the list by the following methods

- sort()
```python
# sort(key = None, reverse=False)
# By default, sort method will sort the list in ascending order with items first element, return None
nums = [20, 8, 12, 5, 13]
nums.sort()
print(nums) # [5, 8, 12, 13, 20]

# Based on the first element of items, therefore, Chien will be the first whereas Melody will be the last
names = ['David', 'Melody', 'Jonas', 'Jane', 'Chien', 'Liz']
names.sort()
print(names)    # ['Chien', 'David', 'Jane', 'Jonas', 'Liz', 'Melody']

# Use lambda to define the sort behavior, sort method will based on the generated key to sort the list
nums = [20, -24, -9, 5, 13]
nums.sort(key= lambda x: x**2)
print(nums) # [5, -9, 13, 20, -24]

# Or programmers can reverse the sorted list
nums = [20, -24, -9, 5, 13]
nums.sort(reverse=True)
print(nums) # [20, 13, 5, -9, -24]
```

## Set
A **mutable** collection that stores data uniquely, a set ensures that each element is stored only once in it.

### Set Creation

- Creating set by built-in function
```python
# set(iterable)
# set method will create a set from an iterable object, return a set
empty = set() # empty set
countries = set(['Taiwan', 'USA', 'Japan', 'Taiwan', 'USA'])
print(countries)    # {'USA', 'Taiwan', 'Japan'}
```

- Creating set by curly brackets
```python
# {} represents empty dictionary in Python
countries = {'Taiwan', 'USA', 'Japan', 'Taiwan', 'USA'}
print(countries)    # {'USA', 'Taiwan', 'Japan'}
```

### Set Accessing
Set does not support access value by index, programmers can only acccess value with loop
```python
countries = {'Taiwan', 'USA', 'Japan'}
# The following code will access one item from left to right from the set
for country in countries:
    print(country)

# set also accept unpacking to access multiple items, the unpacked one will be a list
Tai, *others = countries
print(Tai)  # Taiwan
print(others)   # ['Japan', 'USA']
print(type(others)) # list
```

### Set Checking
Except from **in** to check whether an item in an iterable object or not, there are several built-in functions to check items in a set

- using **in**
```python
countries = {'Taiwan', 'USA', 'Japan'}
print('Taiwan' in countries) # True
print('China' not in countries) # True
```

- isdisjoint()
```python
# isdisjoint(iterable object)
# isdisjoint method check whether set is disjoint with another iterable object, if so, return True
countries = {'Taiwan', 'USA', 'Japan'}
names = {'David', 'Melody'}
print(countries.isdisjoint(names)) # True
```

- issubset
```python
# issubset(iterable object)
# issubset method check whether one set is subset of another iterable object, if so, return True
countries = {'Taiwan', 'USA', 'Japan', 'France', 'Netherland'}
asia = {'Taiwan', 'Japan', 'Korean'}
europe = {'France', 'Netherland'}
print(asia.issubset(countries)) # False
print(europe.issubset(countries)) # True

# Or programmers can simply use <= and < to check, but operators can only use between two set
countries = {'Taiwan', 'USA', 'Japan', 'France', 'Netherland'}
countries_2 = {'Taiwan', 'USA', 'Japan', 'France', 'Netherland'}
europe = {'France', 'Netherland'}
# Note that <= equals to issubset, including cases where two sets are identical
# Whereas < not includes cases that two sets are identical
print(europe <= countries) # True
print(countries_2 < countries) # False
```

- issuperset
```python
# issuperset(other set)
# issuperset method check whether one set is superset of another, if so, return True
countries = {'Taiwan', 'USA', 'Japan', 'France', 'Netherland'}
asia = {'Taiwan', 'Japan', 'Korean'}
europe = {'France', 'Netherland'}
print(countries.issuperset(asia)) # False
print(countries.issuperset(europe)) # True

# Or programmers can simply use >= and > to check, but operators can only use between two set
countries = {'Taiwan', 'USA', 'Japan', 'France', 'Netherland'}
countries_2 = {'Taiwan', 'USA', 'Japan', 'France', 'Netherland'}
europe = {'France', 'Netherland'}
# Note that >= equals to issuperset, including cases where two sets are identical
# Whereas > not includes cases that two sets are identical
print(countries >= europe) # True
print(countries < countries_2) # False
print(countries < ['Taiwan']) # raise TypeError
```

### Set Updating
Items in set can not be modified, but uses can updates items from set

- add()
```python
# add(item)
# add method will add one item into set
countries = {'Taiwan', 'USA', 'Japan'}
countries.add('France')
print(countries)    # {'USA', 'Taiwan', 'Japan', 'France'}
```

- update()
```python
# update(iterable object)
# update method can add several items into set
countries = {'Taiwan', 'USA', 'Japan'}
europe = {'France', 'Netherland'}
countries.update(europe)
print(countries)    # {'USA', 'Taiwan', 'Japan', 'France', 'Netherland'}

# Or programmers can simply use |= to add items, but operators can only use between two set
countries = {'Taiwan', 'USA', 'Japan'}
europe = {'France', 'Netherland'}
countries |= europe
print(countries)    # {'USA', 'Taiwan', 'Japan', 'France', 'Netherland'}
list_europe = ['France', 'Netherland']
countries |= europe # raise TypeError
```

- difference_update()
```python
# difference_update(iterable object)
# difference_update method will remove items which are in the iterable object from set
countries = {'Taiwan', 'USA', 'Japan'}
asia = {'Taiwan', 'Japan', 'Korean'}
countries.difference_update(asia)
print(countries)    # {'USA'}

# Or programmers can simply use -= to add items, but operators can only use between two set
countries = {'Taiwan', 'USA', 'Japan'}
asia = {'Taiwan', 'Japan', 'Korean'}
countries -= asia
print(countries)    # {'USA'}
list_asia = ['Taiwan', 'Japan', 'Korean']
countries -= list_asia # raise TypeError
```

- intersection_update()
```python
# intersection_update(iterable object)
# intersection_update method will keep items which are both in the iterable object and set, and it will return a new set
countries = {'Taiwan', 'USA', 'Japan'}
asia = {'Taiwan', 'Japan', 'Korean'}
countries.intersection_update(asia)
print(countries)    # {'Taiwan', 'Japan'}

# Or programmers can simply use &= to operate, but operators can only use between two set
countries = {'Taiwan', 'USA', 'Japan'}
asia = {'Taiwan', 'Japan', 'Korean'}
countries &= asia
print(countries)    # {'Taiwan', 'Japan'}
list_asia = ['Taiwan', 'Japan', 'Korean']
countries &= list_asia # raise TypeError
```

- symmetric_difference_update()
```python
# symmetric_difference_update(iterable object)
# symmetric_difference_update method will update set with items which are in set or iterable object but not in both
countries = {'Taiwan', 'USA', 'Japan'}
asia = {'Taiwan', 'Japan', 'Korean'}
countries.symmetric_difference_update(asia)
print(countries)    # {'USA', 'Korean'}

# Or programmers can simply use ^= to operate, but operators can only use between two set
countries = {'Taiwan', 'USA', 'Japan'}
asia = {'Taiwan', 'Japan', 'Korean'}
countries ^= asia
print(countries)    # {'USA', 'Korean'}
list_asia = ['Taiwan', 'Japan', 'Korean']
countries ^= list_asia # raise TypeError
```

### Set Removing
Items in set can not be modified, but uses can remove items from set

- remove()
```python
# remove(item)
# remove method will remove item from set, raising KeyError if item is not in set
countries = {'Taiwan', 'USA', 'Japan'}
countries.remove('France') # Raise KeyError
```

- pop()
```python
# pop method will remove random item from set and return it
countries = {'Taiwan', 'USA', 'Japan'}
print(countries.pop()) # Randomly return and remove one item from set
```

- discard()
```python
# discard(item)
# discard method will remove item from set, will not raise KeyError even though item is not in set
countries = {'Taiwan', 'USA', 'Japan'}
countries.discard('France') # Nothing will happen
print(countries)    # {'USA', 'Taiwan', 'Japan'}
```

- clear()
```python
# clear method will remove all elements in set
countries = {'Taiwan', 'USA', 'Japan'}
countries.clear()   # Remove all elements in set
print(countries)    # set()
```

### Set Joining
Programmers can join two set with different methods

- union()
```python
# union(iterable object)
# union method will return a new set which contains all items in set and iterable object
countries = {'Taiwan', 'USA', 'Japan'}
europe = {'France', 'Netherland'}
print(countries.union(europe)) # {'USA', 'Taiwan', 'Japan', 'France', 'Netherland'}

# Or programmers can simply use | to join, but operators can only use between two set
countries = {'Taiwan', 'USA', 'Japan'}
europe = {'France', 'Netherland'}
print(countries | europe) # {'USA', 'Taiwan', 'Japan', 'France', 'Netherland'}
list_europe = ['France', 'Netherland']
print(countries | list_europe) # Raise TypeError
```

- intersection()
```python
# intersection(iterable object)
# intersection method will return a new set which contains all items in set and iterable object
countries = {'Taiwan', 'USA', 'Japan'}
asia = {'Taiwan', 'Japan', 'Korean'}
print(countries.intersection(asia)) # {'Taiwan', 'Japan'}

# Or programmers can simply use & to join, but operators can only use between two set
countries = {'Taiwan', 'USA', 'Japan'}
asia = {'Taiwan', 'Japan', 'Korean'}
print(countries & asia) # {'Taiwan', 'Japan'}
list_asia = ['Taiwan', 'Japan', 'Korean']
print(countries & list_asia) # Raise TypeError
```

- difference()
```python
# difference(iterable object)
# difference method will return a new set which contains items that in set but not in iterable object
countries = {'Taiwan', 'USA', 'Japan'}
asia = {'Taiwan', 'Japan', 'Korean'}
print(countries.difference(asia)) # {'USA'}

# Or programmers can simply use - to join, but operators can only use between two set
countries = {'Taiwan', 'USA', 'Japan'}
asia = {'Taiwan', 'Japan', 'Korean'}
print(countries - asia) # {'USA'}
list_asia = ['Taiwan', 'Japan', 'Korean']
print(countries - list_asia) # Raise TypeError
```

- symmetric_difference()
```python
# symmetric_difference(iterable object)
# symmetric_difference method will return a new set which contains items that in set or iterable object but not in both
countries = {'Taiwan', 'USA', 'Japan'}
asia = {'Taiwan', 'Japan', 'Korean'}
print(countries.symmetric_difference(asia)) # {'USA', 'Korean'}

# Or programmers can simply use ^ to join, but operators can only use between two set
countries = {'Taiwan', 'USA', 'Japan'}
asia = {'Taiwan', 'Japan', 'Korean'}
print(countries ^ asia) # {'USA', 'Korean'}
list_asia = ['Taiwan', 'Japan', 'Korean']
print(countries ^ list_asia) # Raise TypeError
```

## Dictionary
A **mutable** collection that stores key-value pairs, allowing only unique keys.

### Dictionary Creation

- Creating dictionary by built-in function
```python
# built-in function dict(iterable object)
# Empty dictionary
empty = dict()
# dict() will unpack iterable object to key-value pairs
dct = dict([["k1", "v1"], ["k2", "v2"]])    
print(dct)  # {"k1": "v1", "k2": "v2"}
```

- Creating dictionary by curly brackets, {}
```python
# Empty dictionary
empty = {}
# Dictionary with initial values
dct = {
    "k1": "v1", 
    "k2": "v2"
    }
```

### Dictionary Accessing

- simply use d[key]
```python
dct = {
    'k1':'v1',
    'k2':'v2',
    'k3':'v3',
    'k4':'v4'
    }
print(dct['k1']) # v1
print(dct['k4']) # v4
print(dct['k5']) # KeyError
```

If the key is not stored in the dictionary, a KeyError will be raised. To avoid such situation, programmers can utilize the get() method to retrieve the value associated with the key without application crash.
- get()
```python
# get(key, default = None)
# get() function will access the value associated with the key, if the key is not in the dictionary, it will return default value
Engineer = {
    'name': 'David',
    'age': 100,
    'is_single': False,
    'interest': ['Singing', 'Workout'],
    }

print(Engineer.get('name'))    # David
print(Engineer.get('age'))    # 100
print(Engineer.get('is_single'))    # False
print(Engineer.get('address'))  # None
```
- Get Dictionary length by len() function
```python
Engineer = {
    'name': 'David',
    'age': 100,
    'is_single': False,
    'interest': ['Singing', 'Workout'],
    }
print(len(Engineer)) # 4
```

- values()
```python
# values method return a iterable object of dictionary's values
Engineer = {
    'name': 'David',
    'age': 100,
    'is_single': False,
    'interest': ['Singing', 'Workout'],
    }
# print all values in Engineer
for value in Engineer.values():
    print(value)
```

- keys()
```python
# keys method return a iterable object of dictionary's keys
Engineer = {
    'name': 'David',
    'age': 100,
    'is_single': False,
    'interest': ['Singing', 'Workout'],
    }
# print all keys in Engineer
for key in Engineer.keys():
    print(key)
```

- items()
```python
# items method return a iterable object of dictionary's key-value pairs
Engineer = {
    'name': 'David',
    'age': 100,
    'is_single': False,
    'interest': ['Singing', 'Workout'],
    }
# print all key and value in Engineer
for key, value in Engineer.items():
    print(key)
```

### Dictionary Updating

- Simply use dictionary[key] to update add or update key-value pair in a Dictionary
```python
Engineer = {
    'name': 'David',
    'age': 100,
    'is_single': False,
    'interest': ['Singing', 'Workout']
    }
print(Engineer.get('address')) # None
Engineer['address'] = 'Earth'
print(Engineer.get('address')) # Earth

Engineer['interest'].append('Filming')
print(Engineer.get('interest')) # ['Singing', 'Workout', 'Filming']
```

- update()
```python
# update method accept other dictionary or key=value format to add multiple key-value pairs in a Dictionary
Engineer = {
    'name': 'David',
    'age': 100,
    'is_single': False,
    'interest': ['Singing', 'Workout']
    }
personal_info = {
    'height': 200,
    'weight': 500
}
Engineer.update(personal_info)
print(Engineer.get('height'))   # 200

# Note that key will automatically be parsed as a string and doesn't accept variable, only value can accept variable
Engineer.update(love_color='blue')
print(Engineer.get('love_color')) # blue
```

### Dictionary Removing

- clear()
```python
# clear method will empty the dictionary
Engineer = {
    'name': 'David',
    'age': 100,
    'is_single': False,
    'interest': ['Singing', 'Workout']
    }
Engineer.clear()
print(Engineer) # {}
```

- del
```python
# del will delete key-value pair in Dictionary
Engineer = {
    'name': 'David',
    'age': 100,
    'is_single': False,
    'interest': ['Singing', 'Workout']
    }
del Engineer['age']
print(Engineer.get('age')) # None
```

- pop()
```python
# pop(key, default)
# The pop method removes the key-value pair from the dictionary and returns the value associated with the key.
# If the key was not present in the dictionary, it returns a default value; otherwise, it raises a KeyError.
Engineer = {
    'name': 'David',
    'age': 100,
    'is_single': False,
    'interest': ['Singing', 'Workout']
    }
print(Engineer.pop('age')) # 100
print(Engineer.pop('address', 'secret')) # secret
print(Engineer) # {'name': 'David', 'is_single': False, 'interest': ['Singing', 'Workout']}
```

- popitem()
```python
# The popitem method reutrn a key-value pair from the dictionary, which follows the lIFO order.
# If Dictionary is empty, it raises a KeyError.
Engineer = {
    'name': 'David',
    'age': 100,
    'is_single': False,
    'interest': ['Singing', 'Workout']
    }
print(Engineer.popitem())   # ('interest', ['Singing', 'Workout'])
Engineer['address'] = 'secret'
print(Engineer.popitem())   # ('address','secret')
```

### Dictionary Copying

- copy()
```python
# To avoid accidentally change the original value, programmers can use the copy() method to get the shallow copy of the dictionary.
Engineer = {
    'name': 'David',
    'age': 100,
    'is_single': False,
    'interest': ['Singing', 'Workout']
    }
Engineer_2 = Engineer.copy()
Engineer_2['name'] = 'Melody'
print(Engineer.get('name')) # David
print(Engineer_2.get('name')) # Melody
```

### Dictionary Checking
```python
# To check if a key is in the dictionary, programmers can use the in keyword to check if the key is in the dictionary
Engineer = {
    'name': 'David',
    'age': 100,
    'is_single': False,
    'interest': ['Singing', 'Workout']
    }
print('name' in Engineer) # True
print('address' not in Engineer) # True
```