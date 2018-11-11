import pytest
from Day_10.ex_overloading.czekolada import Czekolada


def test_podaj_wage(self):
    czekolada = Czekolada("wedel", "mleczna", 150)
    oczekiwana_waga = 150

    rzeczywista_waga = czekolada.podaj_wage()

    self.assertEqual(rzeczywista_waga, oczekiwana_waga)