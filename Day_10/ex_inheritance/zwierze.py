class Zwierze(object):
    """

    """
    def __init__(self, nazwa):
        self.nazwa = nazwa
        print(f'Rodzę się ({self.nazwa})')

    def ruszaj_sie(self):
        print(f"Zwierze {self.nazwa} rusza sie.")