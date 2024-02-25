# Day16 - Web Scrapping
[<< Day 15](../Day15/Day15.md)  |  [Day 17 >>](../Day17/Day17.md)

### Agenda
- [Python Web Scraping](#python-web-scraping)

## Python Web Scraping

Web scraping involves extracting extensive data from websites and parsing it for useful information using Python. In this section, we use _requests_ and _beautifoulSoup4_ to implement web scraping.

To extract data from websites, a fundamental comprehension of HTML tags and CSS selectors is essential. Programmers can get content on a website by leveraging HTML tags, classes, and/or IDs.
Please refer to [Web status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) for more status code information

**Some common used Function Example**
```python
# Using requests to connect to specific URL
import requests
url = 'https://www.ptt.cc/bbs/Python/index.html'

response = requests.get(url)
print(response.status_code) # prints web status code
print(response.reason) # prints the text of corresponding status code
print(response.text) # prints the web html and css context
```

Using beautifulSoup to parse content from the page

- Basic web scraping example
```py
import requests
from bs4 import BeautifulSoup
url = 'https://www.ptt.cc/bbs/Python/index.html'

response = requests.get(url)
# parse text as html code
soup = BeautifulSoup(response.text,"html.parser")
# Storing tag <a> in <div class="title"></div> into variable selected
selected = soup.select("div.title a")

for tag in selected:
    # Prints all title
    print(tag["href"], tag.text)
```

Please refer to [Scraping Data from a Real Website | Web Scraping in Python](https://www.youtube.com/watch?v=8dTpNajxaH0) for step-by-step tutorial
