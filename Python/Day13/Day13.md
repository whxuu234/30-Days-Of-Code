# Day13 - Regular Expressions
[<< Day 12](../Day12/Day12.md)  |  [Day 14 >>](../Day14/Day14.md)

### Agenda
- [Regular Expressions](#regular-expressions)
    - [Function in Module *re*](#function-in-module-re)
    - [Pattern in Regular Expressions](#pattern-in-regular-expressions)
    - [Regular Expressions Flags](#regular-expressions-flags)

## Regular Expressions

In many situations, programmers often need to locate a specific context within a string and take action accordingly. Regular expressions, special text strings, assist programmers to search for matches within strings efficiently.

### Function in Module *re* 

Programmers must first import the [*re* module](https://docs.python.org/3/library/re.html) to utilize regular expressions. This module offers a powerful regular expression engine designed for searching text within strings.

- compile()
```python
import re
# The re.compile(pattern, flags=0) function compiles a regular expression pattern into a regular expression object. This object can be employed for operations utilizing methods such as match(), search(), and others.
# It is recommended to use the compile function when a expression is used repeatedly.

context = 'It is raining today in Taiwan'

match_result = re.match('It is raining', context) # <re.Match object; span=(0, 13), match='It is raining'>
# The above code is equivalent to the following
re_object = re.compile('It is raining')
match_result = re_object.match(context) # <re.Match object; span=(0, 13), match='It is raining'>
```

- search()
```python
import re
# The re.search(pattern, string, flags=0) function scans through the provided string, seeking the initial occurrence where the regular expression pattern generates a match and return a match object if found.

txt = 'I really love to eat french fries'

# It returns an object with span and match
match_result = re.search('love', txt)
print(match_result) # <re.Match object; span=(9, 13), match='love'>

# Programmers can get the start and end position tuple of the match from span() method
print(match_result.span())  # (9, 13)

# Or simply getting the start and end position by start() and end()
print(match_result.start())  # 9
print(match_result.end())    # 13

# The match object also has a group method which returns the substring that matches the pattern.
print(match_result.group()) # love
```


- match()
```python
import re
# The re.match(pattern, string, flags=0) function returns a match object if the provided string matches the regular expression pattern at the beginning.

txt = 'I really love to eat french fries'

# It returns None as 'love' is not at the begining in the string
match_result = re.match('love', txt)
print(match_result) # None

# In this situation, it returns a match object as 'I really love' matches at the beginning of the string
match_result = re.match('I really love', txt)
print(match_result) # <re.Match object; span=(0, 13), match='I really love'>
```

- fullmatch()
```python
import re
# The re.full(pattern, string, flags=0) function returns a match object if the whole provided string matches the regular expression pattern.

txt = 'I really love to eat french fries'

# In this situation, it returns None as 'I really love' doesnot match the whole string
match_result = re.fullmatch('I really love', txt)
print(match_result) # None

match_result = re.fullmatch('I really love to eat french fries', txt)
print(match_result) # <re.Match object; span=(0, 32), match='I really love to eat french fries'>
```

- split()
```py
import re
# The re.split(pattern, string, maxsplit=0, flags=0) function divides the string based on occurrences of the specified pattern. If the pattern is enclosed within parentheses, it will also appear in the resulting list. When maxsplit is non-zero, the splitting occurs at most maxsplit times, with any remaining elements placed at the end of the list.

txt = '''Taiwan is a country in East Asia.
Taipei is the capital of Taiwan.
Taiwanese food is delicious.'''
print(re.split('(\n)', txt, maxsplit = 1)) # ['Taiwan is a country in East Asia.', '\n', 'Taipei is the capital of Taiwan.\nTaiwanese food is delicious.']
```

- findall()
```python
import re
# The re.findall(pattern, string, flags=0) function returns a list of all non-overlapping matches of the pattern in the string

txt = 'Taiwan is a country in East Asia. Taipei is the capital of Taiwan. Taiwanese food is delicious.'

# It return a list
match_results = re.findall('Taiwan', txt)
print(match_results)  # ['Taiwan', 'Taiwan', 'Taiwan']
```

- finditer()
```python
import re
# The re.finditer(pattern, string, flags=0) function returns an iterator of all non-overlapping matches object of the pattern in the string

txt = 'Taiwan is a country in East Asia. Taipei is the capital of Taiwan. Taiwanese food is delicious.'

# It return a list
match_results = re.finditer('Taiwan', txt)
print(match_results)  # iterator object
for match in match_results:
    print(match) # match object from left to right
```

- sub()
```python
import re
# re.sub(pattern, repl, string, count=0, flags=0) replace the occurrences of pattern in string with repl. The parameter 'count' is the maximum number of pattern occurrences to be replaced if count was not zero.

txt = 'Taiwan is a country in East Asia. Taipei is the capital of Taiwan. Taiwanese food is delicious.'

match_replaced = re.sub('Taiwan', 'France', txt)
print(match_replaced)  # France is a country in East Asia. Taipei is the capital of France. Franceese food is delicious.

# with count = 1
match_replaced = re.sub('Taiwan', 'France', txt, count = 1)
print(match_replaced)  # France is a country in East Asia. Taipei is the capital of Taiwan. Taiwanese food is delicious.
```

- subn()
```python
import re
# re.subn(pattern, repl, string, count=0, flags=0) performs the same operation as the sub() but return a tuple of (new string, number of replacements)

txt = 'Taiwan is a country in East Asia. Taipei is the capital of Taiwan. Taiwanese food is delicious.'

match_replaced = re.subn('Taiwan', 'France', txt)
print(match_replaced)  # ('France is a country in East Asia. Taipei is the capital of France. Franceese food is delicious.', 3)

# with count = 1
match_replaced = re.subn('Taiwan', 'France', txt, count = 1)
print(match_replaced)  # ('France is a country in East Asia. Taipei is the capital of Taiwan. Taiwanese food is delicious.', 1)
```

- excape()
```python
import re
# re.escape(pattern) automatically escapes all regular expression special characters in the provided pattern string.
pattern = 'I,am,happy.'
# '.' is special character in regex to match any single character; therefore, re.escape() will add back slash to escape it
print(re.escape(pattern))   # 'I,am,happy\.'
```

- purge()
The re.purge() method clears the regular expression cache, freeing up memory resources.

### Pattern in Regular Expressions

The following are some common special characters used in regular expressions:

* [] :  A set of characters
  - [a-z]: It means any letter from a to z
  - [A-Z]: It means any character from A to Z
  - [0-9]: It means any number from 0 to 9
  - [A-Za-z0-9]: It means any single character in (a to z, A to Z and 0 to 9)
- . : Any character except for the new line character(\n)
- \ :  uses to escape special characters
  - \d: It means match the digit in string (from 0 to 9)
  - \D: It means match any non digit character in string
  - \s: It means match space in string
  - \S: It means match non space character in string
  - \w: It means match (a to z, A to Z, 0 to 9 and '_') character in string
  - \W: It means match non (a to z, A to Z, 0 to 9 and '_') character in string
  - \b: It means match the word boundary
  - \B: It means match not a word boundary
  - \A: Matches only at the start of string
  - \Z: Matches only at the end of string
- ^: starts with
  - r'^Hey' means a sentence that starts with a word Hey
  - r'[^a-z] means not a to z.
- $: ends with
  - r'Hey$' means a sentence that ends with a word Hey
- *: zero or more times
  - r'[a-c]*' means a optional or it can occur many times for a, b or c.
- +: one or more times
  - r'[a-c]+' means at least once or more for a, b or c.
- ?: zero or one time
  - r'[a-c]?' means zero times or once for a, b or c.
- {n}: Matches a character exactly n times
- {n,}: Matches a character at least n times
- {n,m}: Matches a character n to m times
- |: Either or
  - r'Taiwan|France' means either Taiwan or France
- (): Group a set of character as one unit
  - r'(123){3}' means match '123' three times
- (?:): Non capturing group. Any substring that matches the (?:) will not be catched.
- (?#): Use as comment
- (?=): the remaining characters must follows the rule in it will be a match
- (?!): the remaining characters must not follows the rule in it will be a match
- (?<=): the former characters must follows the rule in it will be a match
- (?<!): the former characters must not follows the rule in it will be a match

**Example**

```python
import re
# square bracket
txt = 'I like guava and cherry. Guava is delicious and healthy.'
print(re.findall(r'[Gg]uava', txt)) # ['guava', 'Guava']


# escape character
txt = 'He is 35 years old and 185 cm height.'
print(re.findall(r'\d', txt))  # ['3', '5', '1', '8', '5']


# Match one or more times
txt = 'He is 35 years old and 185 cm height.'
print(re.findall(r'\d+', txt))  # ['35', '185']


# Match any character
txt = 'Apple and banana are delicious'
print(re.findall(r'[ab].', txt))  # ['an', 'ba', 'an', 'a ', 'ar']

# Match zero or more times(\*)
txt = 'Apple and banana are delicious'
print(re.findall(r'[ab].*', txt))  # ['and banana are delicious']


# Match zero or one time(?)
txt = '''Some people write years-old while the others use years old'''
print(re.findall(r'years[-\s]?old', txt))   # ['years-old', 'years old']


# Match exactly n times
txt = 'He is 35 years old and 185 cm height.'
print(re.findall(r'\d{2}', txt))  # ['35', '18']


# Match from m to n times
txt = 'He is 35 years old and 185 cm height.'
print(re.findall(r'\d{2,3}', txt))  # ['35', '185']


# Starts with
txt = 'He is 35 years old and 185 cm height.'
# ^
print(re.findall(r'^He', txt))  # ['He']
# \A
print(re.findall(r'\AHe', txt))  # ['He']


# word boundary
boundary_txt = 'word with bounary'
non_boundary_txt = 'wordwithoutboundary'
# Only matches the word 'with' that is not connected to other character(except for space)
print(re.findall(r'\bwith\b', boundary_txt))  # ['with']
print(re.findall(r'\bwith\b', non_boundary_txt))  # None
# Only matches the word 'with' that is connected to other character(except for space)
print(re.findall(r'\Bwith\B', non_boundary_txt))  # ['with']
print(re.findall(r'\Bwith\B', boundary_txt))  # None


# Not
txt = 'He is 35 years old and 185 cm height.'
print(re.findall(r'^[a-z\s]+', txt))  # ['H', '35', '185', '.']


# Non capturing group
txt = 'Hey, the string in the (not be captured) will not be captured'
print(re.findall(r'(.*)(?:\(.*\))(.*)', txt))  # [('Hey, the string in the ', ' will not be captured')]


# Matches the former part if the reaming followed the rules in parentheses
txt = 'apple app123'
print(re.search(r'app(?=\d)',txt))   # <re.Match object; span=(6, 9), match='app'>


# Matches if the former string does not followed the rules in parentheses
txt = 'apple banana cherry 123'
print(re.search(r'app(?!\d)',txt))   # <re.Match object; span=(0, 3), match='app'>
```

### Regular Expressions Flags

In Python, there are different flags to operate regular expressions:

- re.A - re.ASCII: ASCII-only matching
- re.DEBUG: Display debug information about compiled expression
- re.I - re.IGNORECASE: Ignore case
- re.L - re.LOCALE: Locale dependent
- re.M - re.MULTILINE: Matches multi-line context
- re.NOFLAG: Default value. Indicates no flag being applied
- re.S - re.DOTALL: Making dot matches any character, without using this, dot will not match newline
- re.U - re.UNICODE: Unicode matching
- re.X - re.VERBOSE: Allowing programmers to visually separate logical sections of the pattern and add comments.
