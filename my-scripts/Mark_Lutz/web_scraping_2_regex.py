#################Extract Text From HTML With Regular Expressions#################################
#we will try to parse "<TITLE >Profile: Dionysus</title  / >"

import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
#<re.Match object; span=(14, 51), match='<TITLE >Profile: Dionysus</title  / >'>

title = match_results.group()
#<TITLE >Profile: Dionysus</title  / >

title = re.sub("<.*?>", "", title) # Remove HTML tags
print(title)
#Profile: Dionysus

'''
Take a closer look at the first regular expression in the pattern string by breaking it down into three parts:

<title.*?> matches the opening <TITLE > tag in html. The <title part of the pattern matches with <TITLE because re.search() is called with re.IGNORECASE, and .*?> matches any text after <TITLE up to the first instance of >.

.*? non-greedily matches all text after the opening <TITLE >, stopping at the first match for </title.*?>.

</title.*?> differs from the first pattern only in its use of the / character, so it matches the closing </title  / > tag in html.

The second regular expression, the string "<.*?>", also uses the non-greedy .*? to match all the HTML tags in the title string. By replacing any matches with "", re.sub() removes all the tags and returns only the text.
'''
