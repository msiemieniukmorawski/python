class Pracownik(object):
    """Definiuje obiekt typu pracownik"""

    liczba_pracownikow = 0
    roczna_podwyzka = 7

    def __init__(self, imie, nazwisko, stawka):
        """Tworzy instancję Pracownik
        (str, str, int) -> Pracownik"""
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        Pracownik.liczba_pracownikow += 1

    @classmethod
    def zmien_roczna_podwyzka(cls, nowa_wartosc):
        """
        Zmienia wartość domyślnej rocznej podwyżki dla wszystkich pracowników.
        :param nowa_wartosc: podwyżka w p.p.
        :return: None
        """

        if not isinstance(nowa_wartosc, int):
            return

        if nowa_wartosc > 18:
            cls.roczna_podwyzka = 18
        else:
            cls.roczna_podwyzka = nowa_wartosc

    @staticmethod
    def sprawdz_pesel(pesel):
        """
        Sprawdza poprawność peselu.
        :param pesel: Numer pesel
        :return: True jeśli pesel poprawny, w innym przypadku False
        """
        if len(pesel) != 11:
            print("pesel nieprawidłowy!")
            return True
        else:
            print("pesel OK")
            return False

    def __str__(self):
        return f"Pracownik: {self.nazwisko} zarabia {self.stawka} PLN"

    def __del__(self):
        """
        Destruktor - wykonywany tuż przed usunieciem obiektu (użycie del)
        """
        Pracownik.liczba_pracownikow -= 1
        print(f"Pracownik {self.nazwisko} został usunięty")
