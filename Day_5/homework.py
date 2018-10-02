# Napisz funkcję (z docstringiem) calc, która będzie wykonywała podstawowe
# działania arytmetyczne (dodawanie, odejmowanie, mnożenie, dzielenie).
# Funkcja powinna przyjmować 3 argumetny:
# działanie (jako string), argument 1, argument 2 (domyślnie o wartości 1).
# Wywołaj funkcję na podanej liście parametrów


def calc(operator, arg1, arg2=1):

    if(operator == '+'):
        print(arg1 + arg2)
    elif(operator == '-'):
        print(arg1 - arg2)
    elif(operator == '/'):
        print(arg1 / arg2)
    elif(operator == '*'):
        print(arg1 * arg2)
    else:
        print('podaleś złe wartości')


test_parameters = [
    ('+', 2, 2),
    ('-', 5, 7),
    ('*', 6, 2.5),
    ('/', 4),
]

calc('+', 2, 2)
calc('-', 5, 7)
calc('*', 6, 2.5)
calc('/', 4)

while 1:
    calc_work = input('przerwać działanie kalkulatora: ')
    if(calc_work == 'tak'):
        break
    else:
        calc(input('podaj operację(+,-,/,*): '), input('podaj wartość pierwsza: '), input('podaj wartosc 2 (jak nie podasz będzie to wartość 1): '))


# Utrudnienie 1: Poproś o podanie parametrów przez konsolę
# Utrudnienie 2: Wykorzystaj podaną funkcję w programie kalkulator,
# która najpierw zapyta o działanie (arytmetyczne lub przerwanie programu),
# a póżniej o argumenty działania
