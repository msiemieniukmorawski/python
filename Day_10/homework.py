# przepisz kalkulator tak, by był klasą posiadającą metody (add, sub, mul, div)
# oraz pamięć (atrybut klasy) z interfejsem:
# dodaj do pamięci (memory), wyczyść pamięć.
# Utrudnienie: jeżeli drugi argument działania nie jest podany (None)
# użyj wartość z pamięci kalkulatora. Obłsuż przypadki skrajne


class Calculator:
    def __init__(self):
        self._memory = None
        # Podpowiedz: użyj atrybutu do przechowywania wyniku
        # ostatniej wykonanej operacji
        self._short_memory = None

    def _second_param(self, param):
        return param if param is not None else self._memory

    def add(self, arg1, arg2=None):
        arg2 = self._second_param(arg2)
        self._short_memory = arg1 + arg2
        return self._short_memory

    def sub(self, arg1, arg2=None):
        self._short_memory = arg1 - self._second_param(arg2)
        return self._short_memory

    def mul(self, arg1, arg2=None):
        self._short_memory = arg1 * self._second_param(arg2)
        return self._short_memory

    def div(self, arg1, arg2=None):
        # TODO: obsłuż dzielenie przez zero
        self._short_memory = arg1 / self._second_param(arg2)
        return self._short_memory

    def memorize(self):
        """Zapamiętuje wynik ostatniego działania wartość."""
        self._memory = self._short_memory

    def clean_memory(self):
        """Usuwa zapamietaną wartość."""
        self._memory = None

    def in_memory(self):
        """Wyświetla zapamietaną wartość."""
        print(f"Zapamiętana wartość: {self._memory}")

    # taka implementacja blokuję możliwośc nadpisania atrybutu innaczej jak
    # przez interfejs klasy
    @property
    def memory(self):
        return self._memory

if __name__ == '__main__':
    calc = Calculator()
    calc.in_memory()
    # print(calc.memory)
    # print(vars(calc))
    print(calc.add(1,2))
    calc.memorize()
    calc.in_memory()
    print(calc.add(1))
    calc.clean_memory()
    # calc.in_memory()
    # calc.memorize()
    # calc.in_memory()
    # print(vars(calc))
    # print(calc.mul(7,2))
    # calc.in_memory()
    # print(vars(calc))