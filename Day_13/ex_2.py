pracownicy = [
    {"imie": "Waldemar", "wiek": 30, "pensja": 3300.00},
    {"imie": "Marta", "wiek": 23, "pensja": 4200.00},
    {"imie": "Zdzisław", "wiek": 56, "pensja": 5300.00}
]
pracownicy_2 = []
for elem in pracownicy:
    pracownicy_2.append((elem['imie'], elem['wiek'], elem['pensja']))


print(pracownicy_2)

posortowani = sorted(pracownicy_2, key=lambda elem: elem[1])
print(posortowani)