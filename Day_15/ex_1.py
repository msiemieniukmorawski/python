import random

list = [random.random() for _ in range(100)]
print(list)
print(['{:.2f}'.format(elem) for elem in list if elem >= 0.5])