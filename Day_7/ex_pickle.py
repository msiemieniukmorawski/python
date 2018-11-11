# importujemy wbudowany moduł Pythona
import pickle

baza = [{"imie": "Adam", "nazwisko":"kowalski", "wiek":32},
{"imie": "Anna", "nazwisko":"nowak", "wiek":23},
{"imie": "Jan", "nazwisko":"nowacki", "wiek":34},
{"imie": "Tomasz", "nazwisko":"lato", "wiek":43}]

# zapisujemy cały słownik
with open("baza.pckl", 'wb') as plik:
    pickle.dump(baza, plik)

# otwieramy słownik
odczytana_baza = None

with open("baza.pckl", "rb") as plik:
    # musimy zwrócić uwagę na kodowanie, jeśli będą pojawiać się krzaczki
    odczytana_baza = pickle.load(plik, encoding="utf-8")

print(odczytana_baza)
