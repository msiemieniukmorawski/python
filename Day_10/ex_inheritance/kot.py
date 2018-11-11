from Day_10.ex_inheritance.zwierze import Zwierze

class Dusza:
    def mam_dusze(self):
        return True

class Kot(Zwierze, Dusza):
    def __init__(self, nazwa, kolor):
        super().__init__(nazwa)
        self.nazwa = nazwa
        self.kolor = kolor

    def ruszaj_sie(self):
        print(f"Kotek {self.nazwa} ruszy sie!")