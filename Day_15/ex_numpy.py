import numpy as np
from numpy import pi

# zainicjowanie tablicy
a = np.array([1,2,3,4])
print(a)

# zainicjowanie tablicy kolejnymi integerami od zera
a = np.arange(15)
print(a)
# zmienienie wymiaru tablicy
a = a.reshape(3, 5)
print(a)

# zwraca tablicę 2D zer
print(np.zeros((3,4)))

# 9 liczb z przedziału od 0 do 2, równo odległych
np.linspace( 0, 2, 9 )

# przydatne jeżeli chcielbyśmy coś wykreślić
x = np.linspace( 0, 2*pi, 100 )
f = np.sin(x)