# funkcja zip zwraca skleja elementy podanych iteratorów (list, stringów)
# znajdujące się na tych samych indeksach w krotki (tuple).
# Kolejność podania iteratorów przekłada się na kolejność w krotce.
# Funkcja zwraca krotki tak długo, jak długo może pobrać po jednym elemencie
# z każdego iteratora

zz = list('abcdefg')  # rzutowanie stringa na listę nie jest konieczne
_list = [5,6,7,8]
for elem in zip(zz, _list):
    print(elem[0], ' ', elem[1])

# krotka może być "rozpakowana" (przypisana do oddzielnych zmiennych) już
# w definicji pętli

print('rozpakowanie')
for elem0, elem1 in zip(zz, _list):
    print(elem0, ' ', elem1)
