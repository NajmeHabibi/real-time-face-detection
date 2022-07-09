import time


def timeit(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        out = func(*args, **kwargs)
        t1 = time.time()
        return out, t1 - t0
    return wrapper
