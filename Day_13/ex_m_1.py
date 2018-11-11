# napisać dekorator mierzący czas wykonania funkcji za pomocą moduły ltime

import time

def time_duration(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        print(time.time() - start_time)
        return ret
    return inner



@time_duration
def funct(a,b):
    return a+b

funct(1, 6)
