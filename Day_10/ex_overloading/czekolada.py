class Czekolada(object):
    def __init__(self, producent, rodzaj, waga):
        self.producent = producent
        self.rodzaj = rodzaj
        self.waga = waga
        self.cena = None

    def zjedz(self, ilosc_g):
        if ilosc_g <= self.waga:
            self.waga = self.waga - ilosc_g

        else:
            print("Nie ma tyle czekolady")

    def podaj_wage(self):
        return self.waga

    def podaj_producenta(self):
        print(self.producent)

    def __add__(self, other):
        try:
            return self.waga + other.waga
        except AttributeError:
            return self.waga + other

    def __sub__(self, other):
        return self.waga - other.waga

    def __lt__(self, other):
        return self.waga < other.waga

    # def __gt__(self, other):
    #     return self.waga > other.waga

    def __str__(self):
        return f"Czekolada {self.rodzaj} od {self.producent}"