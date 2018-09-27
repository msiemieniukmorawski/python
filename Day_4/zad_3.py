# Wyświetl wszystkie elementy listy i jej indeksy

zz = [1, 2, 3, 4, 5]

print('ver 1')  # z wykorzystaniem pętli while
ii = 0
while ii < len(zz):
    print(ii, ' ', zz[ii])
    ii = ii + 1

print('ver 2')  # z wykorzystaniem pętli for i dodatkowej zmiennej na indeksy
for ii in range(len(zz)):
    print(ii, ' ', zz[ii])

print('ver 3')  # z wykorzystaniem pętli for i funkcji enumerate
for ii, elem in enumerate(zz):
    print(ii, ' ', elem)
