from Day_11.ex_inhertinace.zwierzeta import *

zwierzak = Zwierz("pantofelek")
zwierzak.mow()
zwierzak.ruszaj_sie()
print(15 * '-')
kucyk = Kon("Stefan", "brązowy")
kucyk.mow()
kucyk.ruszaj_sie()
print(15 * '-')
osiolek = Osiol("uparciuch", 4)
osiolek.mow()
osiolek.ruszaj_sie()
print(15 * '-')

mul_1 = Mul("siwuch", "siwy")
mul_1.mow()
mul_1.ruszaj_sie()

print(help(Mul))
