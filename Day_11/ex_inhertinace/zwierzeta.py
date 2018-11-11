class Zwierz(object):
    def __init__(self, nazwa):
        # super().__init__()
        self.nazwa = nazwa
        # print('Zwierz')

    def mow(self):
        print(f"Zwierzak {self.nazwa} nie mówi")

    def ruszaj_sie(self):
        print(f"Zwierz {self.nazwa} rusza się.")


class Kon(Zwierz):
    def __init__(self, nazwa, umaszczenie):
        # lepiej podawać jawnie skąd ma być dziedziczone
        # super().__init__(nazwa)
        Zwierz.__init__(self, nazwa)
        self.umaszczenie = umaszczenie
        print(vars(self))
        # print('Kon')

    def mow(self):
        print(f"Koń {self.nazwa} mówi: iiiiihhhhhhaaaaa")

    def ruszaj_sie(self):
        print(f"Koń {self.nazwa} hasa po łące.")


class Osiol(Zwierz):
    def __init__(self, nazwa, st_uparotsci):
    # def __init__(self, nazwa):
        Zwierz.__init__(self, nazwa)
        self.st_upartosci = st_uparotsci
        # print('Osiol')

    def ruszaj_sie(self):
        print(f"Osioł {self.nazwa} nie chce sie ruszyc"
              f" przez najbliższe {self.st_upartosci} minuty.")

    def wypisz_upartosc(self):
        print(f"Upartość: {self.st_upartosci} minuty.")


class Mul(Kon, Osiol):
    def __init__(self, nazwa, umaszczenie):
        # jawnie używamy inicjalizator pierwszego rodzica
        # Kon.__init__(self, nazwa, umaszczenie)
        super().__init__(nazwa, umaszczenie)
        # print('Mul')
