def reverse_string(zdanie):
    """
    Zwraca odwrócony string. Jeśli argument jest pustym
    stringiem lub None - zwraca None
    :param zdanie: Zdanie do odwrócenia
    :return: Odwrócone zdanie lub None
    """
    if zdanie == "" or zdanie == None:
        return None
    else:
        return zdanie[::-1]

def main():
    """Funkcja zawierająca proste testy funkcji odwroc string
    Ta funkcja będzie wywołana tylko jeśli ten plik zostanie
    uruchomiony. Jak będzie importowany to nie zostanie wykonana."""
    imie = "Ala"
    odwr_imie = reverse_string(imie)
    spr_imie = imie[::-1]

    if odwr_imie == spr_imie:
        print(f"Imię {imie} zostało prawidłowo obrócone na {odwr_imie}")
    else:
        print(f"Nieprawidłowo {spr_imie} != {odwr_imie}")

moja_zmienna = "Arek"

# sprawdzamy czy moduł jest uruchomiony bezpośrednio czy
# importowany
if __name__ == '__main__':
    main()










