class Monitor(object):
    """Monitor komputerowy"""
    def __init__(self, prod, przek, proporcje="16:9"):
        """
        Tworzy instancję obiektu typu monitor
        :param prod: str - producent
        :param przek: int - przekatna ekranu w calach
        :param proporcje: str - proporcje ekranu, defaultowo 16:9
        """
        self.przekatna = przek
        self.producent = prod
        self.proporcje = proporcje
        self.kolor = "czarny"
        self.wlaczony = False

    def wlacz(self):
        if not self.wlaczony:
            self.wlaczony = True
            print(f"Monitor {self.producent} zostal wlaczony.")
        else:
            print("Monitor jest juz wlaczony")

    def wylacz(self):
        if self.wlaczony:
            self.wlaczony = False
            print(f"Monitor {self.producent} jest wylaczony.")
        else:
            print("Juz jest przeciez wylaczony")

    def __str__(self):
        return f"Monitor producent: {self.producent}\n" \
               f"        przelatna: {self.przekatna}\n" \
               f"        proporcje: {self.proporcje}"




