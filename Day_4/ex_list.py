# lista to przykład obiektu, który jest:
# - zmienny (mutable) - zdefiniowana wcześniej lista może zostać np. wydłużona
# - iterowalny - można przejść po jej elementach za pomocą pętli for
# - uporządkowany - kolejność dodawania elementów do listy ma znaczenie

a = [1, 2, 3]  # definicja 3-elementowej listy
print(a)  # wyświetlenie listy
print(a[1])  # wyświetlenie wartości elementu listy o indeksie 1
a[1] = 'nowa wartość'  # nadpisanie 1 indeksu listy stringiem
# wstawienie wartości po danym indeksie
a.insert(1, 'inna nowa wartość')
print(a)
# wydłużenie listy o nowy element (int 4) - wartość otrzymuje indeks "3"
a.append(4)
print(a)
# lub poprzez połączenie z inną listą
print(a + [5, 6.7])
# usunięcie elementu z indeksu 2,
# wszytkie dalsze wartości przesuwają o "jedno miejsce w lewo"
# usunięta wartość przypisana jest do zmiennej b
b = a.pop(2)
print('a: {}, b: {}'.format(a, b))
# lub po prostu usunięta - bez zwracania wartości pod indeksem
del a[0]
print(a)
