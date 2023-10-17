import sys
from tkinter import *
from tkinter import ttk

sys.path.append('./')
from entities.User import User


class UserMenuWindow():
    def start_test(self):
        pass
    
    def watch_results(self):
        pass
    
    def back_to_start(self):
        self.clean()
        from frames.StartWindow import StartWindow
        start_win = StartWindow(self.root)
    
    def clean(self):
        self.user_name.place_forget()
        self.pass_test.place_forget()
        self.select_number.place_forget()
        self.spinbox.place_forget()
        self.start.place_forget()
        
        self.stats.place_forget()
        self.cancel.place_forget()

    def __init__(self, root, user):
        self.root = root
        self.User = user

        self.user_name = ttk.Label(self.root, text = 'Пользователь: '+ str(self.User.get_name()))
        self.pass_test = ttk.Label(self.root, text = 'Пройти тест')
        self.select_number = ttk.Label(self.root, text = 'Выберите количество таблиц')

        self.spinbox_var = StringVar(value=1)
        self.spinbox = ttk.Spinbox(from_=1, to=10, increment=1, textvariable=self.spinbox_var)
        
        self.start = ttk.Button(self.root, text = 'Начать', command=self.start_test)
        self.stats = ttk.Button(self.root, text = 'Посмотреть результаты', command=self.watch_results)
        self.cancel = ttk.Button(self.root, text = 'Выйти', command=self.back_to_start)

        self.user_name.place(relx=0.1,rely=0.1)
        self.pass_test.place(relx=0.2,rely=0.3)
        self.select_number.place(relx=0.2,rely=0.4)
        self.spinbox.place(relx=0.2,rely=0.45)
        self.start.place(relx=0.3,rely=0.55)
        
        self.stats.place(relx=0.7,rely=0.5)
        self.cancel.place(relx=0.5,rely=0.8)