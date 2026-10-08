from functools import lru_cache

def decorate(func):
    def wrapper(*args):
        import time
        start = time.perf_counter()
        result = func(*args)
        stop = time.perf_counter()
        print(f"Delai : {stop - start}")
        return result
    return wrapper

@lru_cache(maxsize=None)
def _operation(a, b):
    if b == 0:
        return 0
    if b == 1:
        return a
    return _operation(a, b-1) + _operation (a, b-2)

@decorate
def operation(a, b):
    return _operation(a, b)

result = operation(30, 12)
print(result)