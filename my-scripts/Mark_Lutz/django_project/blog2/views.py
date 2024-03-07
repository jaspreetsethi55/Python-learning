from django.shortcuts import render ##Add this this use html from templates
from django.http import HttpResponse

# Create your views here."""

"""##Directly using html
def home(request):
    html = '''
    <html>
        <h1>Blog2 Home</h1>         
        <body>
            This is a blog2 home page
        </body>
    </html>'''

    return HttpResponse(html)
"""

"""
def about(request):
    html = '''
    <html>
        <h1>Blog2 About</h1>         
        <body>
            This is a blog2 about page
        </body>
    </html>'''

    return HttpResponse(html)
"""

##using from template
"""
def home(request):
    return render(request,'blog2/home.html') ##static page
def about(request):
    return render(request,'blog2/about.html')
"""

##using data from our script in html templates - dynamic web pages
#Let us say we got below list of dict from database

posts = [
            { 'title' : 'blog post 1',
              'author' : 'Jaspreet Sethi',
              'date_posted' : 'Feb 21, 2020',
              'content': 'First post content'
             },

            { 'title' : 'blog post 1',
              'author' : 'Jaspreet Sethi',
              'date_posted' : 'Feb 21, 2020',
              'content': 'Second post content'
             }
          ]

def home(request):
    ##Need to pass a dict to render function
    context = {
                'posts' : posts
               }

    #return render(request,'blog2/home2.html',context) ##Passing 3rd argument as dict of data that needs to be passed to html templates - dynamic page
    #return render(request,'blog2/home3.html',context) ##above comment + using template inheritance - see template home3.html to understand this
    #return render(request,'blog2/home4.html',context) ##above comment + using bootstrap classes and js 
    return render(request,'blog2/home5.html',context) ##above comment + including static css and some navigation bars in body via base3.html



def about(request):
    #return render(request,'blog2/about2.html',{'title':'about'})
    #return render(request,'blog2/about3.html',{'title':'about'})
    #return render(request,'blog2/about4.html',{'title':'about'})
    return render(request,'blog2/about5.html',{'title':'about'})
                 
