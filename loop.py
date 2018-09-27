string = "Zażółć gęślą jaźń."
list_polish_char = ['ą','ć','ę','ł','ń','ó','ś','ź']
list_vowel = ['a', 'o', 'i', ' e', 'ę', 'ą', 'ó', 'u']
print('for 1')
for elem in string:
    if elem in list_vowel:
        print(elem)

print(' ')
print('for 2')
for elem in string:
    if elem in list_polish_char:
        print(elem)

print(' ')
print('for 3')
for elem in range(1, 10, 3):
    print(string[elem])