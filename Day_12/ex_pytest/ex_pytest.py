from Day_12.unnecessary_math import multiply

# Moduł pytest nie potrzebuje żadnego boilerplate kodu (dodatkowych klas,
# inicjowania parametrów). Każda funkcja znajdująca się w scieżce uruchomienia,
# zaczynająca się na test zostanie uruchomiona.

def test_numbers_3_4():
    assert multiply(3, 4) == 12


def test_strings_a_3():
    assert multiply('a', 3) == 'aaa'