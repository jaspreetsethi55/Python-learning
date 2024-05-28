# beauty_soup.py

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

#Creates a BeautifulSoup object and assigns it to the soup variable
#BeautifulSoup object assigned to soup is created with two arguments. The first argument is the HTML to be parsed, and the second argument,the string "html.parser", tells the object which parser to use behind the scenes. "html.parser" represents Python’s built-in HTML parser.
soup = BeautifulSoup(html, "html.parser")
print(soup)

#BeautifulSoup objects have a .get_text() method that you can use to extract all the text from the document and automatically remove any HTML tags.
print(soup.get_text()) 
#There are a lot of blank lines in this output. These are the result of newline characters in the HTML document’s text. You can remove them with the .replace() string method if you need to.

#To get only specific text from an HTML document. Using Beautiful Soup first to extract the text and then using the .find() string method is sometimes easier than working with regular expressions.
#However, other times the HTML tags themselves are the elements that point out the data you want to retrieve. For instance, perhaps you want to retrieve the URLs for all the images on the page. These links are contained in the src attribute of <img> HTML tags. In this case, you can use find_all() to return a list of all instances of that particular tag:
print(soup.find_all("img"))
#[<img src="/static/dionysus.jpg"/>, <img src="/static/grapes.png"/>]

#This returns a list of all <img> tags in the HTML document. The objects in the list look like they might be strings representing the tags, but they’re actually instances of the Tag object provided by Beautiful Soup. Tag objects provide a simple interface for working with the information they contain.

#can explore this a little by first unpacking the Tag objects from the list:
image1, image2 = soup.find_all("img")

#Each Tag object has a .name property that returns a string containing the HTML tag type:
print(image1.name)
#'img'


#We can access the HTML attributes of the Tag object by putting their names between square brackets, just as if the attributes were keys in a dictionary.
#For example, the <img src="/static/dionysus.jpg"/> tag has a single attribute, src, with the value "/static/dionysus.jpg". Likewise, an HTML tag such as the link <a href="https://realpython.com" target="_blank"> has two attributes, href and target.

#To get the source of the images in the Dionysus profile page, you access the src attribute using the dictionary notation mentioned above:
print(image1["src"])
#'/static/dionysus.jpg'

print(image2["src"])
#'/static/grapes.png'

###Certain tags in HTML documents can be accessed by properties of the Tag object. For example, to get the <title> tag in a document, you can use the .title property:
print(soup.title)
#<title>Profile: Dionysus</title>

##If we view source the url, we'll see that <title> tag is written in all caps with spaces: "<TITLE >Profile: Dionysus</title  / >" but we don't see this when we used soup.title & this is because Beautiful Soup automatically cleans up the tags for you by removing the extra space in the opening tag and the extraneous forward slash (/) in the closing tag.


#########Search specific kind of tags#############
#One of the features of Beautiful Soup is the ability to search for specific kinds of tags whose attributes match certain values. For example, if you want to find all the <img> tags that have a src attribute equal to the value /static/dionysus.jpg, then you can provide the following additional argument to .find_all():
print(soup.find_all("img", src="/static/dionysus.jpg"))
#[<img src="/static/dionysus.jpg"/>]

####Note: HTML parsers like Beautiful Soup can save you a lot of time and effort when it comes to locating specific data in web pages. However, sometimes HTML is so poorly written and disorganized that even a sophisticated parser like Beautiful Soup can’t interpret the HTML tags properly.
#In this case, you’re often left with using .find() and regular expression techniques to try to parse out the information that you need.


###In some cases, you may find that Beautiful Soup doesn’t offer the functionality you need. The lxml library is somewhat trickier to get started with but offers far more flexibility than Beautiful Soup for parsing HTML documents.


##Beautiful Soup is great for scraping data from a website’s HTML, but it doesn’t provide any way to work with HTML forms. For example, if you need to search a website for some query and then scrape the results, then Beautiful Soup alone won’t get you very far.

