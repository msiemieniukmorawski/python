from Day_10.ex_inheritance.czlowiek import Czlowiek


class Student(Czlowiek):
    def __init__(self, indeks):
        super().__init__("anonimowy", 19)
        self.indeks = indeks

    def ruszaj_sie(self):
        print("Nie chce mi sie, jestem po imprezie.")

    def powiedz(self):
        print("Poprosze o troje!")

    def swietuj_egzaminy(self):
        print("Na zdrowie!")