# Wypisz co 3 liczbę z przedziału od 1 do 10 wyłącznie,
# wykorzystując pętlę "for"
print('ver 1')
for ii in range(1, 10, 3):
    print(ii)

print('ver 2')
for ii in range(1, 10):
    if ii % 3 == 1:
        print(ii)

print('ver 3')
for ii in (1, 4, 7):
    print(ii)

#  wersja z wykorzystaniem pętli while
a = 1
while True:
    print('before: {}'.format(a))
    if a >= 10:
        break
    print(a)
    a = a + 3
