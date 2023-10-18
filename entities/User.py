class User:
    def __init__(self, name, age, type):
        self._name = name
        self._age = age
        self._type = type

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def type(self):
        return self._type

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    @type.setter
    def type(self, type):
        self._type = type
