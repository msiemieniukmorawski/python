# Zmodyfikuj kod tak aby korzystał z instrukcji try-except.
# w celu zarówno obsługi błędów jak i zapewnienia zamknięcia strumienia do pliku
# (usunąć instrukcję with)

import os

file_path = "dane.txt"

try:
    plik = open(file_path)
except FileNotFoundError:
    print('plik nie istenieje')
else:
    plik.close()




