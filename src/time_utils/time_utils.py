"""
time utilities
"""
import time

# return time in milliseconds
def function_timer(function):
    def wrap(*args):
        start_time = time.time()
        func = function(*args)
        finish_time = time.time()
        print('{:s} function took {:.4f} ms'.format(function.__name__, (finish_time-start_time)*1000.0))
        return func
    return wrap
