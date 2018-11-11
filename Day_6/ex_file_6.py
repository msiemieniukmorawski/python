sciezka = "tekst1.txt"

tekst = "Dopisana linijka tekstu"

# ten sposób umożliwia nam dopisywanie treści zawsze w nowej linijce

with open(sciezka, "r+") as plik:
    # print(plik.tell())
    # idziemy kursorem na koniec pliku
    plik.read()

    # bierzemy numer ostatniej pozycji
    # i cofamy kursor na przedostatnią pozycję
    pozycja = plik.tell()
    plik.seek(pozycja - 1)

    # odczytujemy ostatni znak
    ostatni_znak = plik.read()
    print(ostatni_znak)

    # teraz wiemy, że jeśli ostatni znak nie jest znakiem nowej linii
    # to w pliku nie ma na końcu pustego wiersza
    if ostatni_znak != '\n':
        plik.write('\n' + tekst + '\n')
    # a tu był znak nowej linii, czyli plik miał pusty wiersz
    else:
        plik.write(tekst + '\n')
