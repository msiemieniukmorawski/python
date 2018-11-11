# coding=utf-8
# Zaimplementuj klasy: Rectangle, Square, Circle dziedziczące z klasy Figure.
# Rectangle powinien mieć dwa atrybuty odpowiadające bokom (a i b)
# oraz definiować metody klasy Figure.
# Klasa Square powinna dziedziczyć z Rectangle, wiążąc ze sobą boki a i b
# (tzn. modyfikacja boku a lub boku b powinna ustawiać tę samą wartość
# dla drugiego atrybutu.
# Circle ma posiadać tylko atrybut promień.
# Utrudnienie 1: Zaimplementuj classmetod "name" zwracającą nazwę klasy
# Utrudnienie 2: Zaimplementuj metody statyczne pozwalające na obliczenie pola
# figury na podstawie podanych parametrów.
# Zamień metody obliczające pole i obwód w property.
# Utrudnienie 3 (nieobowiązkowe): Zaimplementuj klasę Diamond (romb)
# dziedziczącą z Figure, po której będzie dziedziczyć Square.
# Klasa wprowadza atrybuty przekątnych oraz metody:
# - sprawdź równość przekątnych
# - to_square: po sprawdzeniu równości przekątnych zwróci instancję
# klasy Square o takich przekątnych


class Figure:
    def area(self):
        raise NotImplemented

    def perimeter(self):
        raise NotImplemented
