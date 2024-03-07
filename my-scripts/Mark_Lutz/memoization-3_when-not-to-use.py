######Caching Caveats – What Can Be Memoized?#################
#Ideally, you will want to memoize functions that are deterministic.

def deterministic_adder(x, y):
    return x + y

'''Here deterministic_adder() is a deterministic function because it will always return the same result for the same pair of parameters. For example, if you pass 2 and 3 into the function, it will always return 5.
'''

#Compare this behavior with the following nondeterministic function:

from datetime import datetime

def nondeterministic_adder(x, y):
    # Check to see if today is Monday (weekday 0)
    if datetime.now().weekday() == 0:
        return x + y + x
    return x + y

'''This function is nondeterministic because its output for a given input will vary depending on the day of the week: If you run this function on Monday, the cache will return stale data any other day of the week.
Generally I find that any function that updates a record or returns information that changes over time is a poor choice to memoize.
'''

