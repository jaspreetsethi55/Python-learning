####functools.lru_cache decorator#####
'''
Now that we’ve seen how to implement a memoization function ourself, lets see how we can achieve the same result using Python’s functools.lru_cache decorator for added convenience

The lru_cache decorator is the Python’s easy to use memoization implementation from the standard library. Once you recognize when to use lru_cache, you can quickly speed up your application with just a few lines of code.
'''
import functools

@functools.lru_cache(maxsize=128) #maxsize argument is to limit the number of items stored in the cache at the same time
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

import timeit
print(timeit.timeit('fibonacci(35)',setup='from __main__ import fibonacci',number=1))
#0.0006153285503387451
'''
we’re getting the result of the first run so much faster this time around. Shouldn’t the cache be “cold” on the first run as well?
The difference is that, in this example, we applied the @lru_cache decorator at function definition time. This means that recursive calls to fibonacci() are also looked up in the cache this time around.

By decorating the fibonacci() function with the @lru_cache decorator we basically turned it into a dynamic programming solution, where each subproblem is solved just once by storing the subproblem solutions and looking them up from the cache the next time.
'''

print(timeit.timeit('fibonacci(35)',setup='from __main__ import fibonacci',number=1))
#1.7002224922180176e-05


########Why we Should Prefer functools.lru_cache#####
'''It provides a handy feature that allows you to retrieve caching statistics with the 'cache_info' method'''

print(fibonacci.cache_info())
#CacheInfo(hits=34, misses=36, maxsize=128, currsize=36)

'''It also provides a 'typed' boolean optional parameter in order to tell the cache that function arguments of different types should be cached separately. For example, fibonacci(35) and fibonacci(35.0) would be treated as distinct calls with distinct results. by default its 'typed=False' i.e. 35 and 35.0 will be treated same'''
#Example: use @functools.lru_cache(maxsize=128, typed=True) as decorator above fibonacci function

'''Another useful feature is the ability to reset the result cache at any time with the cache_clear method'''
fibonacci.cache_clear()
print(fibonacci.cache_info())
#CacheInfo(hits=0, misses=0, maxsize=128, currsize=0)


