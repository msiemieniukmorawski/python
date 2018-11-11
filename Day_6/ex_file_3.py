sciezka = "tekst1.txt"

with open(sciezka) as plik:
    print(plik.tell())

    # readlines odczytuje zawartość od kursora do końca
    # poszczególne linijki będą elementami listy
    # uwaga odczytywanie pliku powoduje odczytanie
    # znaków niedrukowalnych - takich jak taby i znaki nowej linii
    linijki = plik.readlines()

    print(linijki)

    for linijka in linijki:
        print(linijka)
