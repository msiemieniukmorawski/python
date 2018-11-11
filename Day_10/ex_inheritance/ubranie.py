class Ubranie(object):
    def __init__(self, marka, rozmiar):
        self.marka = marka
        self.rozmiar = rozmiar

class But(Ubranie):
    def __init__(self, marka, rozmiar, plec):
        super().__init__(marka, rozmiar)
        self.plec = plec

class Szpilka(But):
    def __init__(self, marka, wysokosc):
        super().__init__(marka, None, "kobiecy")
        self.wysokosc = wysokosc

class OdziezWierzchnia(Ubranie):
    pass

class Polbut(But):
    pass

class Plaszcz(OdziezWierzchnia):
    pass

# ubranko = Ubranie("hm", "40")
# print(ubranko)
#
# bucik = But("adidas", "43", "meski")
# print(bucik)

szpileczka = Szpilka("Laboutin", 15)
print(szpileczka.marka)
print(szpileczka.rozmiar)
print(szpileczka.plec)
print(szpileczka.wysokosc)

szpileczka.rozmiar = 36
print(szpileczka.rozmiar)


# plaszczyk = Plaszcz("no name", "34")
# print(plaszczyk)