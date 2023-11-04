class User():
    def __init__(self, name:str, age:int, typ:int):
        self.name = name
        self.age = age
        self.type = typ
    
    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def set_type(self, typ):
        self.type = typ
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_type(self):
        return self.type