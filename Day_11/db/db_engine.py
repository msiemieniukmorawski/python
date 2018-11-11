class DB:
    def __init__(self):
        self.names_list = []

    def search_name(self, name):
        '''
        Szuka podanego imienia w bazie. Zwraca True jeśli imię jest w bazie.

        (str) -> bool
        '''
        name = self.validate_name(name)
        return name in self.names_list

    @staticmethod
    def validate_name(name):
        name = name.upper()
        return name

    def add_to_base(self, name):
        '''
        Dodaje imię do bazy jeśli nie ma go w bazie. Gdy imie istnieje
        wyświetla komunikat.
        '''
        _name = self.validate_name(name)
        if not self.search_name(name):
            self.names_list.append(name.upper())
            print("Imię {} zostało dodane do kontaktów".format(_name))
        else:
            print("Imię {} jest już w kontaktach".format(_name))

    def delete_name(self, name):
        '''Usuwa imie z bazy jesli imie w bazie jest'''
        if self.search_name(name):
            self.names_list.remove(name)
            print("Imię {} zostało usunięte".format(name))
        else:
            print("Brak imienia na liście")

    def get_names_count(self):
        '''Drukuje liczbę imion w bazie'''
        print("Liczba imion na liście to {}".format(len(self.names_list)))

    def print_names(self):
        '''Drukuje listę imion istniejących w bazie'''
        print(self.names_list)
