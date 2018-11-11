# stwórz listę zawierającą wartości podzielne przez 5
# używając list comprehension
lista_a = [10,20,332,23,234,10,435,35,234, 20, 4938, 435]
lista_b = [x for x in lista_a if x % 5 == 0]
print(lista_b)