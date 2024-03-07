'''
Slicing lists from the end
We want to run some analytics on our investments. To start, we're given a list containing the balance at the end of the day for some number of days. The last item in the list represents yesterday's closing balance and each previous item refers to the day before.

  daily_balances = [107.92, 108.67, 109.86, 110.15]
  Python 2.7
  The first step in the process is to grab adjacent items in the list. To get started, we want a function that takes in our list of daily_balances and prints pairs of adjacent balances for the last 3 days:

    show_balances(daily_balances)

    should print:

      "slice starting 3 days ago: [108.67, 109.86]"
      "slice starting 2 days ago: [109.86, 110.15]"
'''

daily_balances = [107.92, 108.67, 109.86, 110.15]

def show_balances(l):
    for index in range(-3,0):
        print(index,index+2)
        print("slice starting {} days ago: {}".format(abs(index),l[index:index+2]))

show_balances(daily_balances)
    
