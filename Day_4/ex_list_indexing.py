c = [1,2,3,4,5,6]
print('c', c)
# jeżeli chcielibyśmy użyć tylko fragmentu listy możemy wybrać go za pomocą
# zakresu
print(c[2:5])  # od elementu o indeksie 2 do 5. elementu (element ma indeks 4
# ponieważ tablice indeksowane są od 0)
print(c[1:])  # od elementu o indeksie 1 do końca listy
print(c[:4])  # 4 pierwsze elementy
print(c[-4:])  # 4 ostatnie elementy
print(c[::2])  # co drugi element od indeksu 0
print(c[3:-1:2])  # wszystkie wartości w liście od indeksu 3, co drugi indeks,
# bez ostatniego elementu listy
print(c, c[0:len(c):1])  # wartości domyślne indeksu
