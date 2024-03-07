from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    html = '''
    <html>
        <h1>Blog Home</h1>         
        <body>
            This is a blog home page
        </body>
    </html>'''

    return HttpResponse(html)

def about(request):
    html = '''
    <html>
        <h1>Blog About</h1>         
        <body>
            This is a blog about page
        </body>
    </html>'''

    return HttpResponse(html)

        
       

