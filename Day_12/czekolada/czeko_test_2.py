import pytest

from Day_10.ex_overloading.czekolada import Czekolada
from Day_12.catch_print import get_print_output

@pytest.fixture
def czekolada():
    return  Czekolada("wedel", "mleczna", 150)

def test_podaj_wage(czekolada):
    oczekiwana_waga = 150

    rzeczywista_waga = czekolada.podaj_wage()

    assert rzeczywista_waga == oczekiwana_waga


def test_podaj_producenta(czekolada):
    oczekiwany_prod = "wedel\n"

    rzeczywisty_prod = get_print_output(czekolada.podaj_producenta)

    assert rzeczywisty_prod == oczekiwany_prod


@pytest.mark.parametrize(
    [
        'quantity', 'expected', 'expected_buffer'
    ],
    [
        (100, 50, ''),
        (0, 150, ''),
        (200, 150, 'Nie ma tyle czekolady\n')
    ]
)
def test_zjed_czekolade(czekolada, quantity, expected, expected_buffer):
    buffer = get_print_output(czekolada.zjedz, quantity)
    assert czekolada.waga == expected
    assert buffer == expected_buffer