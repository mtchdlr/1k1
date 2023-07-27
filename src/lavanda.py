import time
from functools import wraps
from datetime import timedelta


def timed(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        start = time.time()
        result = f(*args, **kwds)
        elapsed = time.time() - start
        print('{} finished. time: {}'.format(f.__name__, str(timedelta(seconds=elapsed))))
        return result

    return wrapper