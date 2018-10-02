# Napisz funkcję podnoszącą podaną wartość (number) do podanej potęgi (index)
# Jeżeli potęga nie jest podana, podnieś do 2. potęgi


def my_pow(number, index=2):
    return number**index

number= input('podaj liczbę którą będziemy podnośić do potęgi: ')
index= input('potęga: ')

if number.isnumeric():
    number = int(number)
else:
    print('nie podales liczby')
    exit()

if index.isnumeric():
    index = int(index)
else:
    print('nie podales liczby potenga będzie 2')
    index = 2


print(my_pow(number, index))