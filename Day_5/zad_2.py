# Napisz funkcję wyświetlającą imię i nazwisko, nazwisko wielkimi literami


def name(first_name, last_name):
    print(first_name, ' ', last_name.upper())


name(input('podaj imię: '), input('podaj nazwisko: '))