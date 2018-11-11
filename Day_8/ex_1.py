int_1 = 5
int_2 = 0

def division(int_1, int_2):
    try:
        return int_1 / int_2
    except ZeroDivisionError:
        print('nie można dzielić przez zero')
    except IndentationError:
        print('wejście jest blędne')
    return ''

print(division(4,2))
print(division(5,0))
