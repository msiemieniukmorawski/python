from Day_10.ex_overloading.czekolada import Czekolada
from Day_10.ex_overloading.producent import Producent

prod1 = Producent("Milka", "Zurich")

czeko1 = Czekolada(prod1, "z orzechami", 400)
czeko2 = Czekolada(prod1, "z rodzynkami", 600)

print(czeko1)
print(czeko2)

# klasa, która pozwala na korzystanie z polimorfizmu względem kalsy Czekolada
class Weight:
    def __init__(self, waga=200):
        self.waga = waga

    # metodę trzeba dodać, żeby można było wykonać linijkę 27
    # def __lt__(self, other):
    #     return self.waga > other.waga

ciezar1 = Weight()
# print(czeko1 + czeko2)
print(czeko1 + ciezar1)
# print(czeko1 + 2)
# print(czeko1 - czeko2)

# print(czeko1 > czeko2)
print(czeko1 > ciezar1)