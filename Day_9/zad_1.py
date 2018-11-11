# coding=utf-8
# Zmodyfikuj definicję samochodu dodając mu nowy atrybut kolor.
# Kolor może być nadany przy tworzeniu samochodu, jeżeli nie domyślnym kolorem
# jest czerwony.

class Samochod(object):
    def __init__(self, marka, model, kolor = 'czerwony'):
        self.marka = marka
        self.model = model
        self.jedzie = None
        self.silnik = None
        self.kolor = kolor

    def ruszaj(self):
        self.jedzie = True
        print(f"{self.marka} ruszyl")

    def zatrzymaj(self):
        self.jedzie = False
        print(f"{self.marka} zatrzymal sie")


samochod = Samochod('volvo', '199')
print(vars(samochod))
