#!/usr/bin/python3.4

emp = {'name':'jaspreet', 'age':'30'}

#######Simplest way but not good
sentence = 'my name is ' + emp['name'] + ' and i am ' + emp['age'] + ' years old'   ##not much readable
print(sentence) #my name is jaspreet and i am 30 years old

#######Better way(using 'format' function)######
sentence = 'my name is {} and i am {} years old'.format(emp['name'],emp['age']) #Much more readable. {} is known as placeholder's
print(sentence #my name is jaspreet and i am 30 years old)

#######Numbering the placeholders
sentence = 'my name is {1} and i am {0} years old'.format(emp['age'],emp['name'])
print(sentence #my name is jaspreet and i am 30 years old)

##Example: Numbering placeholders - useful in repitative tags
tag, text = 'h1', 'this is paragraph'
html = '<{0}>{1}</{0}>'.format(tag,text)
print(html) #<h1>this is paragraph</h1>

######Grasping key/fields from placeholders
sentence = 'my name is {0[name]} and i am {1[age]} years old'.format(emp,emp)
print(sentence) #my name is jaspreet and i am 30 years old

#####just using single list/dict
sentence = 'my name is {0[name]} and i am {0[age]} years old'.format(emp) #This even applies on list, just use indexes in place of key for list
print(sentence) #my name is jaspreet and i am 30 years old

##Grasping Attributes from Placeholders
class Emp():
    def __init__(self,name,age):
        self.name = name 
        self.age = age

p = Emp('jaspreet','30')

sentence = 'my name is {0.name} and i am {0.age} years old'.format(p)
print(sentence) #my name is jaspreet and i am 30 years old

##Passing keyword to placeholders
sentence = 'my name is {name} and i am {age} years old'.format(age='30',name='jaspreet')
print(sentence) #my name is jaspreet and i am 30 years old


##Formating Numbers
for i in range(1,11):
    sentence = 'the value is {:02}'.format(i) # ':' inside placeholders in necesarry for number formatting. 
    print(sentence)

#{:02} means atleast getting 2 digit number i.e. adding leading zeroes in case number is single digit. Similarly {:03} for 3 getting atleast digits

#Formatting Decimal Numbers
Pi = 3.141559625
sentence = 'pi is equal to {:.2f}'.format(Pi) # .2 is for upto 2 decimal places and f symbolizes floating point number
print(sentence) #pi is equal to 3.14

##printing large numbers with comma for readability
sentence = '1 mb is equal to {:,} bytes'.format(1000**2)
print(sentence) #1 mb is equal to 1,000,000 bytes

##combining comma + decimal placess
sentence = '1 mb is equal to {:,.2f} bytes'.format(1000**2)
print(sentence) #1 mb is equal to 1,000,000.00 bytes


##printing/formatting dates
import datetime
my_date = datetime.datetime(2019,3,27,8,59,5) #2019-03-27 08:59:05
print(my_date)
print('{:%Y_%m_%d_%H_%M_%S}'.format(my_date)) ##Google 'python strptime behaviour' for more date formats

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)

