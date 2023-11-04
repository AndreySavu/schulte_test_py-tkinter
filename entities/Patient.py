#from entities.User import User
#тут хорошо бы было пронаследовать user, но я не знаю как сделать пока

class Patient():
    def __init__(self, id:int, f:str, i:str, o:str, age:int, notes:str):
        self._id = id
        self._surname = f
        self._name = i
        self._patronymic = o
        self._age = age
        self._notes = notes

    def get_patient(self):
        return (self._id,
                self._surname,
                self._name,
                self._patronymic,
                self._age,
                self._notes)
    
    def get_id(self):
        return self._id
    
    def get_surname_n_initials(self):
        return f'{self._surname} {self._name[:1]}. {self._patronymic[:1]}.'