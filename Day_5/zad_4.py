
text = 'Lorem ipsum dolor sit amet, consectetur addipiscing elit. Suspendisse lacinia ligula at nunc ultrices, vel euismod purus interdum. Donec posuere risus eget metus dapibus sodales at tempus arcu. '

# Wyświetl do 10 pierwszych znaków pojawiających się w stringu (text).
def print_10(text):
    return text[:10]

# Wyśwetl do 10 pierwszych znaków pojawiających się w stringu
# wraz z krotnościa ich wystąpienia.
def print_10_count(text):
    text= list(text)
    b = [''] * 10
    c = [1] * 10
    for ii, j in enumerate(text):
        if(ii < 10):
            b[ii] = j
        else:
            if j in b:
                for x, y in enumerate(b):
                    if j == y:
                        c[x] += 1
    zipped_list = zip(b, c)
    return list(zipped_list)

# Utrudnienie: Jako drugi parametr można podać listę znaków lub stringa
# - jeżeli została podana używamy do 10 znaków z niej,
# resztę uzupełniając pierwszymi znakami ze stringa
def print_10_hard(text, extra_list):
    text = list(text)
    count_list = len(extra_list)
    if(count_list < 10):
        count_list = 10 - count_list
        b = list(extra_list) + [' '] * count_list
        chech_leater = 10
    elif(count_list > 10):
        b = list(extra_list)
        chech_leater = len(extra_list)
    else:
        b = [''] * count_list
        chech_leater = count_list
    if len(b) > len(text):
        return 'za długi podałeś wyraz'

    c = [1] * chech_leater
    for ii, j in enumerate(text):
        if (ii < chech_leater):
            if(b[ii] != ' '):
                pass
            else:
                b[ii] = text[ii - len(extra_list)]
        else:
            if j in b:
                for x, y in enumerate(b):
                    if j == y:
                        c[x] += 1

    zipped_list = zip(b, c)
    return list(zipped_list)



print(print_10(text))
print(print_10_count(text))
print(print_10_hard(text, input('podaj ciąg znaków jaki mam znaleźć w stingu:')))