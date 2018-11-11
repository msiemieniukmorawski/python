def logger(func):
    def inner(*args, **kwargs):
        print(f"Arguments were: {args}, {kwargs}")
        return func(*args, **kwargs)
    return inner


@logger
def func1(a, b):
    return a + b

print(func1(1,2))



