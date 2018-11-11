# coding=utf-8
# Dodaj metodę przemaluj, która pozwoli na zmianę wartości atrybutu kolor.
# Metoda pozowli na przelowanie tylko jeżeli samochód jest zatrzymany.
# Jeżeli samochód jedzie zgłoś błąd.
# Utrudnienie: Wykorzystaj komendę assert

class Samochod(object):
    def __init__(self, marka, model, kolor = 'czerwony'):
        self.marka = marka
        self.model = model
        self.jedzie = True
        self.silnik = None
        self.kolor = kolor

    def ruszaj(self):
        self.jedzie = True
        print(f"{self.marka} ruszyl")

    def zatrzymaj(self):
        self.jedzie = False
        print(f"{self.marka} zatrzymal sie")

    def przemaluj(self, nowykolor):
        assert self.jedzie, 'samochód jedzie'
        self.kolor = nowykolor


samochod = Samochod('test', 'test', )