from pytest import fixture

from Day_12.unnecessary_math import multiply

# Fixture to funkcja wykonywana w za każdym razem w danym zakresie ("scope").
# Zakresem może być pojedynczy test('function'),
# klasa, metoda i uruchomienie testów.
# Jeżeli fixtura nazywa się tak jak parametr funkcji,
# zostanie użyta jako parametr.
# Więcej o fixturach: https://docs.pytest.org/en/latest/fixture.html
@fixture
def param_2():
    return 4


def test_numbers_3_4(param_2):
    print(param_2)
    assert multiply(3, param_2) == 12


def test_strings_a_3():
    assert multiply('a', 3) == 'aaa'