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
    area = None
    perimeter = None

    def get_area(self):
        raise NotImplemented

    def get_perimeter(self):
        raise NotImplemented

    def print(self):
        print(self.name())
        # print(f'area: {self.area():.3f}\nperimeter: {self.perimeter():.3f}')
        print(
            f'area: {self.area or 0:.3f}\nperimeter: {self.perimeter or 0:.3f}'
        )

    @classmethod
    def name(cls):
        return cls.__name__


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    @staticmethod
    def get_area(r):
        return math.pi * r ** 2

    @property
    def area(self):
        return self.get_area(self.r)

    @staticmethod
    def get_perimeter(r):
        return 2 * math.pi * r

    @property
    def perimeter(self):
        return self.get_perimeter(self.r)


class Diamond(Figure):
    def __init__(self, e, f):
        self.e = e
        self.f = f

    @property
    def area(self):
        return self.get_area(self.e, self.f)

    @staticmethod
    def get_area(e, f):
        return e * f / 2

    @property
    def perimeter(self):
        return self.get_perimeter(self.e, self.f)

    @staticmethod
    def get_perimeter(e, f):
        return 2 * math.sqrt(e ** 2 + f ** 2)

    def is_diagonal_equal(self):
        return self.e == self.f

    def to_square(self):
        if self.is_diagonal_equal():
            return(Square.create_from_diagonal(self.e))


class Rectangle(Figure):
    def __init__(self, a, b, *args, **kwargs):
        self.a = a
        self.b = b

    @staticmethod
    def get_area(a, b):
        return a * b

    @property
    def area(self):
        return self.get_area(self.a, self.b)

    @staticmethod
    def get_perimeter(a, b):
        return 2 * (a + b)

    @property
    def perimeter(self):
        return self.get_perimeter(self.a, self.b)


class Square(Rectangle, Diamond):
    def __init__(self, a, b=None):
        b = b or a
        e = f = a * math.sqrt(2)
        super().__init__(a, b)
        Diamond.__init__(self, e, f)

    @property
    def b(self):
        return self.a

    @b.setter
    def b(self, b):
        self.a = b

    @classmethod
    def create_from_diagonal(cls, e):
        a = 2 * math.sqrt(2 * e ** 2)
        return cls(a)

if __name__ == '__main__':
    # print("Circle")
    kolo1 = Circle(1)
    kolo1.print()

    # print("Rectangle")
    rec_1 = Rectangle(2, 4)
    rec_1.print()

    # print("Square")
    sqr_1 = Square(2, 4)
    sqr_1.print()
    # print(sqr_1.e)

    # print("Square")
    sqr_2 = Square(2)
    sqr_2.print()

    diam_1 = Diamond(6, 8)
    diam_1.print()

    diam_2 = Diamond(1, 1)
    diam_2.print()
    sqr_3 = diam_2.to_square()
    sqr_3.print()
    print(sqr_3.a)
