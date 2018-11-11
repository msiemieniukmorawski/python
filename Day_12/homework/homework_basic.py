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
import math


class Figure:
    def area(self):
        raise NotImplemented

    def perimeter(self):
        raise NotImplemented

    def print(self):
        print(self.name())
        print(f'area: {self.area():.3f}\nperimeter: {self.perimeter():.3f}')

    @classmethod
    def name(cls):
        return cls.__name__


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    @staticmethod
    def get_area(r):
        return math.pi * r ** 2

    def area(self):
        return self.get_area(self.r)

    @staticmethod
    def get_perimeter(r):
        return 2 * math.pi * r

    def perimeter(self):
        return self.get_perimeter(self.r)


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def get_area(a, b):
        return a * b

    def area(self):
        return self.get_area(self.a, self.b)

    @staticmethod
    def get_perimeter(a, b):
        return 2 * (a + b)

    def perimeter(self):
        return self.get_perimeter(self.a, self.b)


class Square(Rectangle):
    def __init__(self, a, b=None):
        b = b or a
        super().__init__(a, b)

    @property
    def b(self):
        return self.a

    @b.setter
    def b(self, b):
        self.a = b


if __name__ == '__main__':
    # print("Circle")
    kolo1 = Circle(1)
    kolo1.print()

    print(f'Pole koła o promieniu 4: {Circle.get_area(4)}')

    # print("Rectangle")
    rec_1 = Rectangle(2, 4)
    rec_1.print()

    # print("Square")
    sqr_1 = Square(2, 4)
    sqr_1.print()