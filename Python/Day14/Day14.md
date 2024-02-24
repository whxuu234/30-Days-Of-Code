# Day14 - File Handling
[<< Day 13](../Day13/Day13.md)  |  [Day 15 >>](../Day15/Day15.md)

### Agenda
- [File Handling](#file-handling)
  - [Reading Files](#reading-files)
  - [Writing and Updating Files](#writing-and-updating-files)
- [Different File Types](#different-file-types)
  - [Txt File](#txt-file)
  - [JSON File](#json-file)
  - [JSON & Dictionary Transformatting](#json--dictionary-transformatting)
  - [Saving as JSON File](#saving-as-json-file)
  - [CSV File](#csv-file)
  - [XML File](#xml-file)

## File Handling

File handling is an important part of programming, enabling programmers to create, read, update, and delete files. In Python, programmers can utilize the built-in function open() to manage file operations.

- File handling modes
  - "r" - Read : Default value. Opens a file and read from it, raises an error if the file does not exist
  - "a" - Append : Opens a file to write from the end, creates the file if it does not exist
  - "w" - Write : Opens a file ,clear all data, and write from the start, creates the file if it does not exist
  - "x" - Create : Creates the specified file name, raises an error if the file already exists
  - "t" - Text : Default value. Text mode
  - "b" - Binary : Binary mode (e.g. images)

### Reading Files

Python will return a file object to avoid frequently FILE I/O. By default, Python will use _read_ mode to open files. 

- _read()_: 
```python
# read(size) read the text as string. By default, it will read the whole context as a string. Programmers can use size parameter to limit the number of characters.
import os
# handling file path
file_path = os.path.join(os.path.dirname(__file__), '../Files/demo.txt')
f = open(file_path)
print(f.read()) # read the whole context
# Remember to close the file to release the resource and prevent from operating errors
f.close()

# Reading 3 letters with read()
f = open(file_path)
print(f.read(3)) # Hey
f.close()
```

- _readline()_
```python
# The readline() read the first line of the file each time and returns it as a string.
import os
# handling file path
file_path = os.path.join(os.path.dirname(__file__), '../Files/demo.txt')
f = open(file_path)
# rstrip() is used to remove any trailing newline chars from the end of the string
print(f.readline().rstrip()) # Hey, it is a demo txt file
print(f.readline()) # Goodbye!
f.close()
```

- _readlines()_
```python
# readlines() method reads all the text line by line and returns a list of lines
import os
# handling file path
file_path = os.path.join(os.path.dirname(__file__), '../Files/demo.txt')
f = open(file_path)
# rstrip() is used to remove any trailing newline chars from the end of the string
print(f.readlines()) # ['Hey, it is a demo txt file\n', 'Goodbye!']
f.close()
```

- _splitlines()_
```python
# splitlines(keepends=False) method split the text into lines by '\n' and returns a list of lines
import os
# handling file path
file_path = os.path.join(os.path.dirname(__file__), '../Files/demo.txt')
f = open(file_path)
print(f.read().splitlines()) # ['Hey, it is a demo txt file', 'Goodbye!']
f.close()
```

To avoid forgetting to close files, it is recommended to use the with statement, context manager, in Python. The with statement will automatically close the file after the block of code inside it.

```python
import os
# handling file path
file_path = os.path.join(os.path.dirname(__file__), '../Files/demo.txt')
with open(file_path) as f:
    lprint(f.read().splitlines()) # ['Hey, it is a demo txt file', 'Goodbye!']
```

### Writing and Updating Files

There are two modes for modifying files - append ('a') and write ('w'). The former appends content to the end of the file while the latter overwrites the file content.


```py
import os
# handling file path
file_path = os.path.join(os.path.dirname(__file__), '../Files/demo.txt')

with open(file_path, 'a') as f:
    f.write('This context will be appended to the end.')

with open(file_path) as f:
    f.write('This context will overwrite the original file context.')
```

## Different File Types

### Txt File

The file type with the extension _txt_ is very common, and the operations related to this file type were demonstrated earlier.

### JSON File

JSON means JavaScript Object Notation. It is commonly used for storing and transporting data. In fact, it is a stringified JavaScript object or Python dictionary.

**Example**

```python
# dictionary
personal_info = {
    "name":"David",
    "country":"Taiwan",
    "married":"No"
}
# JSON: A string form a dictionary
# To make it more readable, programmers can use triple quotes
personal_json = '''{
    "name":"David",
    "country":"Taiwan",
    "married":"No"
}'''
```

### JSON & Dictionary Transformatting

In Python, there is a [_json_ module](https://docs.python.org/3/library/json.html) which supports multiply json operations.

- loads()
```python
# json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
# Changing Json to Dictionary
import json
# JSON
personal_json = '''{
    "name":"David",
    "country":"Taiwan",
    "married":"No"
}'''
person_info = json.loads(person_json)
print(type(person_info)) # <class 'dict'>
print(person_info) # dictionary format
```

- dumps()
```python
# json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
# Changing Dictionary to JSON
import json
# python dictionary
personal_info = {
    "name":"David",
    "country":"Taiwan",
    "married":"No"
}
personal_json = json.dumps(personal_info, indent=4) # indent could be any, just for formatting purpose
print(type(personal_json)) # <class 'str'>
print(personal_json)
```

### Saving as JSON File

To write a json file, programmers should use the json.dump() method, it can take dictionary, output file, ensure_ascii and indent.

- dump()
```python
# json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
import json
import os

# handling file path
file_path = os.path.join(os.path.dirname(__file__), '../Files/json_file_demo.json')
# python dictionary
personal_info = {
    "name":"David",
    "country":"Taiwan",
    "married":"No"
}
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(personal_info, f, ensure_ascii=False, indent=4)
```

### CSV File

CSV, short for Comma-Separated Values, is a straightforward file format employed to store tabular data, resembling a spreadsheet or database.
Please refer to [CSV Module](https://docs.python.org/3/library/csv.html#csv.Dialect)

**CSV Example:**

```csv
"name","country","married"
"David","Taiwan","No"
```

**Example:**

```python
import csv
import os
file_path = os.path.join(os.path.dirname(__file__), '../Files/csv_file_demo.csv')
with open(file_path) as f:
    # csv.reader(csvfile, dialect='excel', **fmtparams), dialect means parameter of processing csv file
    # delimiter parameter means the seperative character of each field, using comma by default
    reader = csv.reader(f, delimiter=',')
    row_count = 0
    for row in reader:
        if row_count == 0:
            print(f'Columns are :{", ".join(row)}')
            row_count += 1
        else:
            print(f'\tThis guy is name {row[0]}. He lives in {row[1]} and is {row[2]} married.')
            row_count += 1
    print(f'Number of data: {row_count - 1}')
# Result:
# Columns are :name, country, married
#        This guy is name David. He lives in Taiwan and is No married.
# Number of data: 1
```

### XML File

XML, short for eXtensible Markup Language, resembles HTML in its nature as a markup language. Primarily utilized for storing and transporting data in Tree like structure, especially structured data.
Please refer to [XML Module](https://docs.python.org/3/library/xml.etree.elementtree.html)


**XML Format Example**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<person gender="female">
  <name>Melody</name>
  <country>France</country>
  <age>27</city>
  <hobbies>
    <hobby>TV Series</hobby>
    <hobby>Hiking</hobby>
    <hobby>Singing</hobby>
  </hobbies>
</person>
```

**Example**

```python
import os
import xml.etree.ElementTree as ET

file_path = os.path.join(os.path.dirname(__file__), '../Files/xml_file_demo.xml')
tree = ET.parse(file_path)
root = tree.getroot()
print(f'Root tag: {root.tag}, Root attribute: {root.attrib}')
for child in root:
    print(f'Field name: {child.tag}')

# Result
# Root tag: person, Root attribute: {'gender': 'female'}
# Field name: name
# Field name: country
# Field name: age
# Field name: hobbies
```
