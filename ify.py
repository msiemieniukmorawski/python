# name = input('podaj imię: ')
#
# if name[-1] == 'a' or name[-1] == 'A':
#     print('Witaj koleżanko')
# else:
#     print('Witaj kolego')

# temp = input('jaka jest temperatura na klimazatorze: ')
# if temp.isnumeric():
#     temp = int(temp)
# else:
#     print('błędna dana')
#     exit()
#
# ideal_temp = 23.0
#
# if temp < ideal_temp:
#     print('jest za zimno')
# elif temp > ideal_temp:
#     print('jest za cieplo')
# else:
#     print('jest idealnie')

# sprawdź czy liczba jest podzielna przez 2 5 7

# digit = input('podaj liczbę: ')
# if digit.isnumeric():
#     digit = int(digit)
# else:
#     print('nie podales liczby')
#     exit()
# if (digit % 3) == 0:
#     print('liczba jest podzielna przez 3')
# else:
#     print('liczba nie jest podzielna przez 3 ')
# if (digit % 5) == 0:
#     print('liczba jest podzielna przez 5')
# else:
#     print('liczba nie jest podzielna przez 5 ')
# if (digit % 7) == 0:
#     print('liczba jest podzielna przez 7')
# else:
#     print('liczba nie jest podzielna przez 7')


# oblicz czy podany rok jest przestępny
# year = input('podaj rok: ')
# message_true = 'rok jest przestępny'
# massage_false = 'rok jest nie przestępny'
# if year.isnumeric():
#     year = int(year)
# else:
#     print('nie podales liczby')
#     exit()
# if year % 400 == 0:
#     print(message_true)
# elif year % 4 == 0 and year % 100 != 0:
#     print(message_true)
# else:
#     print(massage_false)


number_h = input('liczbę godzin przepracowanych: ')
price = input('płaca za nadgodziny: ')
standart_h = 35

if number_h.isnumeric():
    number_h = int(number_h)
else:
    print('nie podales liczby')
    exit()

if price.isnumeric():
    price = int(price)
else:
    print('nie podales liczby')
    exit()


if number_h < standart_h + 11 and number_h >= standart_h:
    new_price = price * 1.5
    price_more = (number_h - standart_h) * new_price
    price_new = standart_h * price + price_more
    print(price_new)
elif number_h > standart_h + 11:
    new_price = price * 2
    price_more = (number_h - standart_h) * new_price
    price_new = standart_h * price + price_more
    print(price_new)
else:
    price_new = number_h * price
    print(price_new)
