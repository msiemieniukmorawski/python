# Znajdź wszystkie samogłoski w podanym niżej stringu
a = "Zażółć gęślą jaźń."
vowels = ['a', 'o', 'i', 'u', 'e', 'ą', 'ę', 'ó']

print('ver 1:')
for elem in a:
    for ii in vowels:
        if elem == ii:
            print(elem)

print('ver 2')
for elem in a:
    if elem in vowels:
        print(elem)

print('ver 3')
vowels2 = 'aeiouyąęó'  # string jest indeksowalny jak lista 
for elem in a:
    if elem in vowels2:
        print(elem)
