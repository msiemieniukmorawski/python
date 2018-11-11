class Named:
    def __init__(self, name):
        self.name = name

    def name_getter(self):
        return self.__name.capitalize()

    def name_setter(self, name):
        assert isinstance(name, str)
        self.__name = name

    def name_deleter(self):
        self.__name = ''

    name = property(name_getter, name_setter, name_deleter)


a = Named('adam')
print(vars(a))
print(a.name)
del a.name
print(vars(a))
print(a.name)