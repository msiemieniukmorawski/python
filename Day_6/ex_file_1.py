sciezka = "tekst1.txt"

# otwieramy plik w trybie tekstowym, tylko do odczytu
plik = open(sciezka, 'r')

# read() czyta zawartość, od miejsca w któym jest kursor
# aż do kocńa pliku
tresc = plik.read()
print(tresc)

# pamiętać o zamykaniu pliku
plik.close()
