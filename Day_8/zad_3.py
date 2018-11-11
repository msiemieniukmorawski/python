# coding=utf-8
# Zmodyfikuj funckję calculator tak by w jej implementacji wykorzystać słownik
# oraz bibiliotekę operator (dla działań dodawania odejmowania itd.
# Obsługę podania błędnego wejścia zrealizuj przez intrukcję try-except.

from operator import add, sub, mul, truediv

calc_func = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}

def calc(func, arg1, arg2=1):
    try:
        return calc_func[func](arg1, arg2)
    except KeyError:
        return ('Podano błędne działanie!')
    except TypeError:
        return ('Podane argumenty mają błędny typ')

print()