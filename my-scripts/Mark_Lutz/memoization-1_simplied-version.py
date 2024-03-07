'''Tutorial Link: https://dbader.org/blog/python-memoization'''

'''
#####memoization (also sometimes spelled memoisation)#####
Link: https://dbader.org/blog/python-memoization

Memoization is a specific type of caching that is used as a software optimization technique

A cache stores the results of an operation for later use. For example, your web browser will most likely use a cache to load this tutorial web page faster if you visit it again in the future.
So, when I talk about memoization and Python, I am talking about remembering or caching a function output based on its inputs

Memoization allows you to optimize a Python function by caching its output based on the parameters you supply to it. Once you memoize a function, it will only compute its output once for each set of parameters you call it with. Every call after the first will be quickly retrieved from a cache.
'''

'''
#####Why and When Should You Use Memoization in Your Python Programs?#####
The answer is expensive code:

When I am analyzing code, I look at it in terms of how long it takes to run and how much memory it uses. If I’m looking at code that takes a long time to run or uses a lot of memory, I call the code expensive.

Its expensive code because it costs a lot of resources, space and time, to run. When you run expensive code, it takes resources away from other programs on your machine.

If you want to speed up the parts in your Python application that are expensive, memoization can be a great technique to use
'''

'''
#####The Memoization Algorithm Explained#####
The basic memoization algorithm looks as follows:

Set up a cache data structure for function results
Every time the function is called, do one of the following:
**Return the cached result, if any; or
**Call the function to compute the missing result, and then update the cache before returning the result to the caller
'''

#####Let’s Write a Memoization Decorator From Scratch#####
#Let'simplement the above memoization algorithm as a Python decorator, which is a convenient way to implement generic function wrappers in Python:
#A decorator is a function that takes another function as an input and has a function as its output.

##memoize() decorator that implements the above caching algorithm
def memoize(func): #takes a function and returns a wrapped version of the same function that implements the caching logic (memoized_func)
    cache = dict() #Python dictionary as a cache here

    def memoized_func(*args):
        '''
        Whenever the decorated function gets called, we check if the parameters are already in the cache. If they are, then the cached result is returned. So, instead of re-computing the result, we quickly return it from the cache.
        '''
        if args in cache: #using a key to look-up a value in a dictionary is quick. This makes dict a good choice as the data structure for caching
            return cache[args]
        result = func(*args)
        cache[args] = result #If the result isn’t in the cache, we must update the cache so we can save some time in the future
        return result

    return memoized_func


###Let’s test our memoization decorator out on a recursive Fibonacci sequence function###
def fibonacci(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

#Calculating the n-th Fibonacci number this way has O(2^n) time complexity—it takes exponential time to complete. This makes it quite an expensive function indeed.

#Let's do some benchmarking using Python’s built-in timeit module
#Python’s built-in timeit module lets me measure the execution time in seconds of an arbitrary Python statement
#timeit.timeit(stmt, setup,timer, number)

#stmt: This will take the code for which you want to measure the execution time. The default value is "pass".
#setup: This will have setup details that need to be executed before stmt. The default value is "pass."
#timer: This will have the timer value, timeit() already has a default value set, and we can ignore it.
#number: The stmt will execute as per the number is given here. The default value is 1000000. But because a single fibonacci(35) call already takes a few seconds to execute I’m limiting the number of executions to one with the number argument

import timeit
print(timeit.timeit('fibonacci(35)',setup='from __main__ import fibonacci', number=1))
print(timeit.timeit('fibonacci(35)',setup='from __main__ import fibonacci', number=1))
#6.502343952655792 
#6.313030809164047


###Let’s see if we can speed it up by leveraging the function result caching provided by our memoization decorator##
@memoize
def fibonacci_memoized(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

#To inspect the cache I reached “inside” the memoized_fibonacci function using its __closure__ attribute.The cache dict is the first local variable and stored in cell 0
print(fibonacci_memoized.__closure__[0].cell_contents) #{} -- Since cache is empty for now
print(timeit.timeit('fibonacci_memoized(35)',setup='from __main__ import fibonacci_memoized', number=1))
#6.015703171491623
#we’ve got a similar execution time because the first time I ran the fibonacci_memoized function the result cache was cold—we started out with an empty cache which means there were no pre-computed results that could help speed up this function call.

print(fibonacci_memoized.__closure__[0].cell_contents) #{(35,): 9227465}
print(timeit.timeit('fibonacci_memoized(35)',setup='from __main__ import fibonacci_memoized', number=1))
#2.473592758178711e-06
#Notice the e-06 suffix at the end of that floating point number? The second run of memoized_fibonacci took only about 2.5 microseconds to complete.

print(fibonacci_memoized(35))
#9227465

#####Let’s do a nother little experiment to demonstrate how the function result cache works. I’ll call memoized_fibonacci a few more times to populate the cache and then we’ll inspect its contents again:######
print(fibonacci_memoized(1))
print(fibonacci_memoized(2))
print(fibonacci_memoized(4))
print(fibonacci_memoized(7))
print(fibonacci_memoized.__closure__[0].cell_contents) #{(7,): 13, (2,): 1, (35,): 9227465, (1,): 1, (4,): 3}


######A quick word of warning on the naive caching implementation in our memoize decorator###### 
'''
In this example the cache size is unbounded, which means the cache can grow at will. This is usually not a good idea because it can lead to memory exhaustion bugs in your programs.

With any kind of caching that you use in your programs, it makes sense to put a limit on the amount of data that’s kept in the cache at the same time. This is typically achieved either by having a hard limit on the cache size or by defining an expiration policy that evicts old items from the cache at some point.
'''
