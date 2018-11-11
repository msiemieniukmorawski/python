with open("tekst1.txt", 'r') as plik:
    print(plik)
    for ii in range(3):
        print(plik.readline())