class Named:
    def __init__(self, name):
        self.name = name
        # self.__name = name
        # setattr(self, 'name', name)

    @property
    def name(self):
        return self.__name.capitalize()

    @name.setter
    def name(self, name):
        assert isinstance(name, str)
        self.__name = name

    @name.deleter
    def name(self):
        self.__name = ''



a = Named('adam')
# a = Named(0)
print(vars(a))
# print(a.__name)
# a.name = 7
# print(a._Named__name)
print(a.name)
# print(vars(a))
# print(a.__dict__)
# print(Named.__dict__)
del a.name
print(vars(a))
print(a.name)