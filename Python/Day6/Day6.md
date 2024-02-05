# Day6 - Loops
[<< Day 5](../Day5/Day5.md)  |  [Day 7 >>](../Day7/Day7.md)

### Agenda
- [Loops](#loops)
    - [While Loop](#while-loop)
    - [While Else](#while-else)
    - [For Loop](#for-loop)
    - [For Else](#for-else)
    - [Nested Loop](#nested-loop)
    - [Break, Continue and Pass](#break-continue-and-pass)

## Loops
Python offers two types of loops to handle repetitive tasks.

- while loop
- for loop

### While Loop
When the condition is true, the code block in the loop will be executed continually until the condition become false.

```python
count = 0
while count <= 5:
    print(count)
    count += 1
#prints from 0 to 5
```

### While Else
If the condition becomes false, that is when the loop stops. Programmers can use 'else' to run block of code once the condition is no longer true.

```python
count = 0
while count <= 5:
    print(count)
    count += 1
# Executing else code block once when the condition become false
else:
    print(count)
#print from 0 to 6
```

### For Loop
Loop is used for iterating over a iterable object (that is either a list, a tuple, a dictionary, a set, or a string, etc.)

```python
# list
nums = [0, 1, 2, 3, 4, 5]
for number in nums:
    print(number)   # print from 0 to 6

for ind, num in enumerate(nums):
    print(ind, num)  # prints index and number

# string
country = 'Taiwan'
for letter in country:
    print(letter)   # prints each letter

for ind in range(len(country)):
    print(country[i])   # prints each letter

# tuple
names = ('David', 'Melody')
for name in names:
    print(number)   # prints each name

# dictionary
Engineer = {
    'name': 'David',
    'age': 100,
    'is_single': False,
    'interest': ['Singing', 'Workout'],
    }
# By default, iterate dictionary will get keys
for key in Engineer:
    print(key) # prints each key

for key, value in person.items():
    print(key, value)

# set
countries = {'Taiwan', 'France', 'Netherland'}
for country in countries:
    print(country)
```

### For Else
Programmers can use else to execute once more after for loop, 

```python
for number in range(5):
    print(number)   # prints 0 to 4
else:
    print(f'The loop stops at {number}')
```

### Nested Loop

```python
Engineer = {
    'name': 'David',
    'age': 100,
    'is_single': False,
    'interest': ['Singing', 'Workout'],
    }
for key in Engineer:
    if key == 'interest':
        for interest in Engineer['interest']:
            print(interest)
```

### Break, Continue and Pass
There are several ways to stop or skip the current code block of the loop.

- break
```python
# break is used for leave the loop
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break
# Since it leaves the loop when count equals to 3, the above while loop only prints 0, 1, 2 
```

- continue
```python
# continue will skip the remaining code block and start the next iteration

for count in range(10):
    if count == 4:
        continue
    print(count)
# This code will print 0, 1, 2, 3, 5, 6, 7, 8, 9
```

- pass
```python
# pass means do nothing, it is usually used for keep the structure of the code
string = 'Hey, bro!'
for letter in string:
    pass
# prints nothing
```
