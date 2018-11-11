
def func_a(arg1:str, arg2:dict, arg3:float=4.0) -> str:
    arg1 = arg1.capitalize()
    klucze = arg2.keys()
    is_int = arg3.is_integer()

    return arg1

x = func_a("ala", {"imie": "jan"}, 44.0)
print(x)
print(help(func_a))


def func_b(arg1:str, arg2:dict, arg3:float = 4.0) -> str:
    # arg1 = arg1.capitalize()
    klucze = arg2.keys()
    # is_int = arg3.is_integer()

    return klucze

func_b([], {"imie": "jan"}, "4")

def func_c(arg_1, arg_2):
    """Opis."""

print(help(func_c))