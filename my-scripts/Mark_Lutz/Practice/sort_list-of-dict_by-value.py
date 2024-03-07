#!/usr/bin/python3.4

ds = [
        {'name' : 'jaspreet',
         'age': 31
         },

         {'name': 'seth',
          'age': 45
         },

         {'name': 'abhishek',
          'age': 35
          },

         {'name': 'anika',
          'age': 32
          }

       ]


new_ds = sorted(ds,key=lambda k : k['age'])
print(new_ds)


