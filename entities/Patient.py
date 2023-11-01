#from entities.User import User
#тут хорошо бы было пронаследовать user, но я не знаю как сделать пока

class Patient():
    def __init__(self, f, i, o, age, notes, id = None):
        self.__id__ = id
        self.__surname__ = f
        self.__name__ = i
        self.__patronymic__ = o
        self.__age__ = age
        self.__notes__ = notes

    
