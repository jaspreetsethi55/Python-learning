'''Write a program that grabs the full HTML from the following URL:

>>> url = "http://olympus.realpython.org/profiles/dionysus"
Then use .find() to display the text following Name: and Favorite Color: (not including any leading spaces or trailing HTML tags that might appear on the same line).
'''

from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)

html = page.read().decode('utf-8')
print(html)
results = re.findall('Name:[a-zA-Z0-9_ ]+|Favorite Color:.*', html,re.IGNORECASE)
print(results)
