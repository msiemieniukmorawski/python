from Day_9.car import Samochod
from Day_9.engine import Silnik

silnik_v4 = Silnik(1998, "benzyna")

beemka = Samochod("BMW", "3")

beemka.silnik = silnik_v4

print(beemka.silnik)

beemka.silnik.wlaczony = True
