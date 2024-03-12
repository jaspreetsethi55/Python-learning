from urllib.request import urlopen
#function urlopen() can use to open a URL within a program

url = "http://olympus.realpython.org/profiles/aphrodite"

#open web page
page = urlopen(url)
print(page) #<http.client.HTTPResponse object at 0x7f8c2fb14190>

##To extract the HTML from the page, first use the HTTPResponse object’s .read() method, which returns a sequence of bytes. 
##Then use .decode() to decode the bytes to a string using UTF-8:
html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)

#We have the HTML as text, we can extract information from it in a couple of different ways.
#1. Extract Text From HTML With String Methods
#2. Extract Text From HTML With Regular Expressions

#################Extract Text From HTML With String Methods#################################
#.find() returns the index of the first occurrence of a substring, can get the index of the opening <title> tag by passing the string "<title>" to .find()
title_index = html.find("<title>")
print(title_index) #14

#index of the first character of the title value
start_index = title_index + len("<title>") #21

#index of the first character of the closing </title> tag
end_index = html.find("</title>") #39

title = html[start_index:end_index]
print(title) #Profile: Aphrodite


####if title tag has some extra space E.g. "<title >Profile: Poseidon</title>
url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html_bytes = page.read().decode("utf-8")

title_start_index = html_bytes.find("<title>") + len("<title>") #html_bytes.find("<title>") returns -1 as <title> doesn not exist, instead <title > exists

#index of the first character of the closing </title> tag
end_index = html_bytes.find("</title>") #39
title = html_bytes[title_start_index:end_index]
print(title) ##Incorrect result as html_bytes.find("<title>") returned -1
'''

<head>
<title >Profile: Poseidon
'''

#So we need a more reliable way to extract text from HTML i.e. using regular expresssions
