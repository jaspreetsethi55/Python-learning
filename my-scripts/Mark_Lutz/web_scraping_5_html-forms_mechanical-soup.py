'''
The urllib module that we've used is well suited for requesting the contents of a web page but sometimes we need to interact with a web page to obtain the content we need.For example, we might need to submit a form or click a button to display hidden content.

"MechanicalSoup" is a popular and relatively straightforward package to use. MechanicalSoup installs what’s known as a headless browser, which is a web browser with no graphical user interface. This browser is controlled programmatically via a Python program.
'''

import mechanicalsoup
browser = mechanicalsoup.Browser()

url = "http://olympus.realpython.org/login"

#Browser objects represent the headless web browser. we can use them to request a response of the page from the internet by passing a URL to their .get() method:
page = browser.get(url)
print(page)
#<Response [200]>

#MechanicalSoup uses Beautiful Soup to parse the HTML from the request, and page has a .soup attribute that represents a BeautifulSoup object:
print(type(page.soup))
#<class 'bs4.BeautifulSoup'>

#we can view the HTML by inspecting the .soup attribute:
print(page.soup)
'''
<html>
<head>
<title>Log In</title>
</head>
<body bgcolor="yellow">
<center>
<br/><br/>
<h2>Please log in to access Mount Olympus:</h2>
<br/><br/>
<form action="/login" method="post" name="login">
Username: <input name="user" type="text"/><br/>
Password: <input name="pwd" type="password"/><br/><br/>
<input type="submit" value="Submit"/>
</form>
</center>
</body>
</html>
'''

#Notice above page has a <form> on it with <input> elements for a username and a password.

#######Submit a form With MechanicalSoup#################


