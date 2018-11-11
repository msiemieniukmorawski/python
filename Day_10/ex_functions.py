# funkcja bez parametrów
def foo():
    pass


# funkcja z parametrem obowiązkowym (zdefiniowanym)
def fun1(param1):
    return  param1


# funkcja z parametrami domyślnymi
def fun2(param1=None, param2=2):
    print(param1, param2)


# funkcja pozwalająca na podanie dowolnej liczby
# parametrów pozycyjnych (bez nazwy), zapisywanych w tupli args
def fun3(param1, *args):
    print(param1)
    print(param1, args)


# funkcja przyjmująca od 1 do nieskończenie wielu parametrów pozycyjnych
def fun4(param1, param2=2, *args):
    print(f'param2: {param2}')
    print(f'param1: {param1}')
    print(f'args: {args}')


# funkcja przyjmująca dowolną liczbę parametrów nazwanych,
# zapisywanych w słowniku kwargs
def fun5(param1, param2=2, **kwargs):
    print(f'param2: {param2}')
    print(f'param1: {param1}')
    print(f'kwargs: {kwargs}')
    print(kwargs.get('nowy_parametr'))
    print(locals())


# funckja przyjmująca przynajmniej jeden parametr
# UWAGA: w definicji funkcji ważne jest aby zachować kolejnosć:
# - parametry pozycyjne
# - parametry nazwane
# UWAGA 2: parametry pozycyjne "tworzą" w przestrzeni nazw funkcji zmienne
# o nazwach odpowiadających nazwą parametrów zdefiniowanych
# (obowiązkowych lub domyślnych), dlatego podając słownik parametrów nazwanych
# należy pamiętać by nie zduplikować kluczy
def fun6(param1, param2=2, *args, **kwargs):
    print(locals())
# fun3(4,'aa', 4.5, (1,))
# fun4(4,'aa', 4.5, (1,))
# fun4(4,'aa')
# fun4(4)

# print('v1')
# fun5(2, nowy_parametr=7)
# print('v2')
# fun5(2, inny=7)
# fun5(2, 7)
# print('v3')

print('v1')
fun6(2)
print('v2')
fun6(2, 7)
print('v3')
fun6(2, 7, 4, 5)
print('v4')
fun6(2, 7, 4, inny=2)
print('v5')
fun6(inny=2, param1=5)
print('v6')
slownik = {
    'inny': 4,
    'param1': 'param1',
}
fun6(slownik)
fun6(**slownik)
# print('v3')
# fun6(2, 7, 4, param2=2)
