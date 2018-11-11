# trzeci sposób importowania
# importujemy wszystko z modułu
from dzien7.moj_modul.odwracacz import *

# tutaj możemy użyć bezpośrednio nazwy funkcji
odwrocony = odwroc_string("ewa")
print(odwrocony)


# uwaga przy tym sposobie może nastąpić konflikt nazw
# jeśli zaimportujemy w ten sposób kilka modułów i będą one mieć
# tak samo nazwane zmienne czy funkcje
# to ostatnio zaimportoway moduł będzie brał te nazwy
