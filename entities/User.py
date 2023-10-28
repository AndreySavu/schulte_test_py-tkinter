class User:
    def __init__(self, name, age, type):
        self._name = name
        self._age = age
        self._type = type

    @property
    def name(self):
        return getattr(self, '_name')

    @name.setter
    def name(self, name):
        setattr(self, '_name', name)

    @property
    def age(self):
        return getattr(self, '_age')

    @age.setter
    def age(self, age):
        setattr(self, '_age', age)

    @property
    def type(self):
        return getattr(self, '_type')

    @type.setter
    def type(self, type):
        setattr(self, '_type', type)