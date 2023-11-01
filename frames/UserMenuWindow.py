from tkinter import *
from tkinter import ttk

from entities.User import User
from frames.StartWindow import *
from frames.TestWindow import TestWindow


class UserMenuWindow():
    def start_test(self):
        self.clean()
        test_win = TestWindow(self.root, self.__user__)
        
    
    def watch_results(self):
        pass
    
    def back_to_start(self):
        self.clean()
        start_win = StartWindow(self.root)
    
    def clean(self):
        #self.user_lbl.place_forget()
        #self.pass_test.place_forget()

        self.start.place_forget()
        
        self.stats.place_forget()
        self.cancel.place_forget()

    def __init__(self, root:Tk, user):
        self.root = root
        self.__user__ = user

        self.user_lbl = ttk.Label(self.root, text = 'Пользователь: '+ str(self.__user__.get_name()))
        #self.pass_test = ttk.Label(self.root, text = 'Пройти тест')

        
        self.start = ttk.Button(self.root, text = 'Начать', command=self.start_test)
        self.stats = ttk.Button(self.root, text = 'Посмотреть результаты', command=self.watch_results)
        self.cancel = ttk.Button(self.root, text = 'Выйти', command=self.back_to_start)

        self.user_lbl.place(relx=0.1,rely=0.1)
        #self.pass_test.place(relx=0.2,rely=0.3)

        self.start.place(relx=0.3,rely=0.55)
        
        self.stats.place(relx=0.7,rely=0.5)
        self.cancel.place(relx=0.5,rely=0.8)