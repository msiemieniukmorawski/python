# Wypisz które liczby z tupli "b" występuję w liście "liczby"


liczby = [2, 4324, 25, 43, 4, 5765, 756, 7, 3425, 325, 364]
b = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for ii in b:
    if ii in liczby:
        print(ii)

