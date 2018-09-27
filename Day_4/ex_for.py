# Pętla "for" przechodzi (iteruje) po wszystkich elementach podanego obiektu
# przypisując go do tymczasowej zmiennej

# w ramach bloku funkcji for powstaje tymczasowa zmienna elem,
# która przy każdym przejściu przez blok funkcji inicjowana jest wartością
# z np. listy
for elem in range(1, 11):
    print(elem)

for elem in "abcd":
    print(elem)

for elem in [1, 2, 3, 4]:
    print(elem)

# tymczasowa zmienna może zostać nadpisana, ale przed kolejnym przejściem
# zostanie zainicjowana wartością z iteratora
for ii in range(10):
    print(ii)
    ii = 100

# w pętli for działa również komenda "break" (przerwanie wykonywania pętli)
for ii in range(10):
    if ii % 5 == 3:
        break
    print(ii)
# oraz "continue" (natychmiast przejdź do kolejnej iteracji)
for ii in range(10):
    if ii % 5 == 0:
        continue
    print(ii)
