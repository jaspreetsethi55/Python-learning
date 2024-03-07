from django.shortcuts import render ##Add this this use html from templates
from django.http import HttpResponse
from .models import Post

# Create your views here."""

#Let us say we got below list of dict from database

'''
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
'''

def home(request):
    ##Need to pass a dict to render function
    context = {
                'posts' : Post.objects.all()
               }
    return render(request,'blogs/home.html',context) ##above comment + including static css and some navigation bars in body via base3.html



def about(request):
    return render(request,'blogs/about.html',{'title':'about'})
                 
