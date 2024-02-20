# Day12 - Iterator
[<< Day 11](../Day11/Day11.md)  |  [Day 13 >>](../Day13/Day13.md)

### Agenda
- [Iterator](#iterator)
    - [Iterator Functions](#iterator-functions)
- [Generator](#generator)
    - [Generationg Generator](#generationg-generator)
    - [Yield From](#yield-from)

## Iterator

An iterator is an interface that enables programmers to iterate through an iterable object, retrieving elements one by one without needing to know the details of the iterable object. Iterators use lazy evaluation, also known as call by need, which means that elements are only retrieved when they are needed; otherwise, they remain inactive. This property has benefits for space complexity.

- **Example**
```python
# Generate a list with huge number takes lots of memory space
nums_list = [i for i in range(100000000000000)]
print(nums_list) # Prints entire list 
# Generate a huge number with iterator saves memory space
nums_iterator = (i for i in range(100000000000000))
print(nums_iterator) # return an generator object
```

In Python, containers are iterable objects, including lists, tuples, and dictionaries, etc.

### Iterator Functions
There are two functions used to convert an iterable object into an iterator and traverse through it one by one respectively: iter() to convert the iterable object into an iterator, and next() to retrieve the elements of the iterator sequentially.

**Example**

```python
# Basically, a loop function will convert an iterable object into an iterator and traverse through it. 
# Every iterable object contain the __iter__ function and can be converted to an iterator by using it.
nums = [num for num in range(5)]
print(dir(nums)) # __iter__ function is present in the list
print(iter(nums))   # return an iterator object

for num in nums:
    print(num)
# The above loop is equivalent to the below code
nums_iterator = iter(nums)
print(next(nums_iterator)) # 0
print(next(nums_iterator)) # 1
print(next(nums_iterator)) # 2
print(next(nums_iterator)) # 3
print(next(nums_iterator)) # 4

# While the iterator is exhausted, it will raise a StopIteration exception
# Loop will automatically break when StopIteration exception is raised
print(next(nums_iterator)) # Raise StopIteration
```

Or programmers can customize there own iterators by implementing the `__iter__` and `__next__` functions.

```python
# Re-implementing itertools.count
class Count:
    """Iterator that counts upward forever."""
    def __init__(self, start=0):
        self.num = start
    
    # The __iter__ function should return an iterator, but in this case, we make this class act as its own iterator, so we simply return itself.
    def __iter__(self):
        return self

    def __next__(self):
        # To prevent infinite loop, we raise StopIteration exception when the number is greater than 1000
        if self.num > 1000:
            raise StopIteration
        num = self.num
        self.num += 1
        return num

count_iterator = Count()
print(next(count_iterator)) # 0
# Print from 1 to 1000 because we use next one time in the above
for num in count_iterator:
    print(num)

# If we delete the __iter__ attribute, loop will not work with it since its not an iterable object anymore
del Count.__iter__
count_iterator = Count()
for num in count_iterator:
    # Raise TypeError exception since __iter__ function is not present anymore, so Count is not an iterable object
    print(num)
# But __next__ function is still working as expected
print(next(count_iterator)) # 0
print(next(count_iterator)) # 1
print(next(count_iterator)) # 2
```

## Generator

A generator is one type of iterator and is the easiest way to implement an iterator. It is defined using the yield keyword. The yield keyword can be treated similarly to return, but it exhibits lazy evaluation characteristics.

### Generationg Generator

- generator expression
```python
# This is a generator expression
nums = (num ** 2 for num in range(1000000000))
print(next(nums))   # 0
print(next(nums))   # 1
print(next(nums))   # 4
print(nums) # generator object
for num in nums:
    print(num)
```

- generator function
```python
# Re-implementing itertools.count with generator
def count(start=0):
    num = start
    while True:
        # When encounter the yield keyword, the function will return the value and stop execution here
        # Next time the function is called by next(), it will continue from the next line after yield statement
        yield num
        num += 1

count_generator = count()
print(next(count_generator)) # 0
print(next(count_generator)) # 1
```

- combining them

```python
def count(start=0, end = 100):
    num = start
    return (
        num
        for num in range(start, end)
        if num % 2 == 0
    )
count_generator = count(10)
print(next(count_generator))    # 10
print(next(count_generator))    # 12
```

### Yield From
The `yield from` keyword was introduced after Python 3.3. It allows the current generator to yield values which is yielded by another generator.

**Example**
```python
def show_every_two_number(start=6, end = 24):
    num = start
    while num <= end:
        yield num
        num += 2
        if 15 > num > 10:
            yield from between_ten_and_twenty()
            num = 15

def between_ten_and_twenty():
    num = 11
    while num < 15:
        yield num
        num += 1

demo = show_every_two_number()
for num in demo:
    print(num, end=' ')
# 6 8 10 11 12 13 14 15 17 19 21 23
```

The keyword `yield from` can also be used to replace the recursive function.

**Example**
```python
# Binary tree traversal
class Node:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
    
    def in_order_traversal(self):
        if self.left != None:
            yield from self.left.in_order_traversal()

        yield self.val

        if self.right != None:
            yield from self.right.in_order_traversal()

root = Node(12)
cur = root
# Generate a binary tree
for value in range(11):
    if value % 2 == 0:
        cur.left = Node(value)
        cur = cur.left
    else:
        cur.right = Node(value)
        cur = cur.right
# In-order traversal
for num in root.in_order_traversal():
    print(num)
```
