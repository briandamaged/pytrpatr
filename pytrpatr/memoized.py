
from functools import wraps

def memoized(f):
    cache = {}
    @wraps(f)
    def memo(*args):
        try:
            return cache[args]
        except KeyError:
            retval = f(*args)
            cache[args] = retval
            return retval
    return memo

