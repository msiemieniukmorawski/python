sciezka = "tekst1.txt"

# klauzula with ułatwia pracę z plikami
# nie musimy pamiętać o zamykaniu pliku
with open(sciezka) as plik:
    # readline odczytuje jedną linijkę
    # po odczytaniu, kursor ustawia się na początku
    # kolejnej linijki (o ile jest jeszcze)
    linijka = plik.readline()
    # tell mówi nam w którym miejscu w pliku znjaduje
    # się kursor
    pozycja = plik.tell()
    print(f"Kursor znajduje się w pozycji nr {pozycja}")

    # print(linijka, end='')
    # print("Kolejna linijka")
    # print(plik.read())

    # seek przenosi kursor we wskazaną pozycję
    plik.seek(3)
    print(plik.read())

