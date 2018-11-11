from pprint import pprint

pracownicy = [
    {"imie": "Waldemar", "wiek": 30, "pensja": 3300.00},
    {"imie": "Marta", "wiek": 23, "pensja": 4200.00},
    {"imie": "Zdzisław", "wiek": 56, "pensja": 5300.00}
]

# liczby = [34,43,342,4,56543,234,5,45,67]
# print(sorted(liczby))
# # liczby.sort()
# print(liczby)
# # print(pracownicy)
# pprint(pracownicy)
# # print(sorted(pracownicy))

# prac_posortowani = sorted(pracownicy,
#                           key=lambda pracownik: pracownik["pensja"],
#                           reverse=True)
#
# # pprint(pracownicy)
# # pprint(prac_posortowani)
#
# class Pracownik(object):
#     def __init__(self, imie, pensja, wiek):
#         self.wiek = wiek
#         self.pensja = pensja
#         self.imie = imie
#
#     def __str__(self):
#         return f"{self.imie} {self.pensja} {self.wiek}"
#
#     def __repr__(self):
#         return f"Obiekt: {self.imie} {self.pensja} {self.wiek}"
#
#     # def __lt__(self, other):
#     #     return self.wiek < other.wiek
#
# p1 = Pracownik("marek", 2300, 23)
# p2 = Pracownik("darek", 3300, 63)
# p3 = Pracownik("bartek", 1300, 33)
#
# lista_p = [p1, p2, p3]
# print(p1)
# print(lista_p)
#
# posortowani = sorted(lista_p, key=lambda prac: prac.imie)
#
# print(posortowani)



