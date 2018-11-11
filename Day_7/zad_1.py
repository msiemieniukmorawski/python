# zaimportuj funkcję reverser z modułu my_mdule i użyj jej
# do zaimplemntowania funckji czy_palindrom

from my_module.reverser import reverse_string


def czy_palindrom(wyraz):
    """
    Check if given string is a palindrom.
    (str)->bool
    """

    return bool(wyraz == reverse_string(wyraz))

print(czy_palindrom("kajak"))
print(czy_palindrom("kopytko"))
print(czy_palindrom("a"))