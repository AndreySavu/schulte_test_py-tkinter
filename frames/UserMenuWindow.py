from tkinter import *
from tkinter import ttk

from entities.User import User
from frames.TestWindow import TestWindow


class UserMenuWindow():
    def __init__(self, root:Tk, user:User):
        self.root = root
        self._user = user
        self.init_interface()
        self.place_interface()

    def init_interface(self):
        self.user_lbl = ttk.Label(self.root, text = 'Пользователь: '+ str(self._user.get_name()))
        self.start = ttk.Button(self.root, text = 'Пройти тест', command=self.start_test)
        self.stats = ttk.Button(self.root, text = 'Посмотреть результаты', command=self.watch_results)
        self.cancel = ttk.Button(self.root, text = 'Выйти', command=self.back_to_start)

    def place_interface(self):
        self.user_lbl.place(relx=0.1,rely=0.1)
        self.start.place(relx=0.3,rely=0.55)
        self.stats.place(relx=0.7,rely=0.5)
        self.cancel.place(relx=0.5,rely=0.8)
    
    def clean(self):
        self.start.place_forget()
        self.stats.place_forget()
        self.cancel.place_forget()
        self.user_lbl.place_forget()
    
    def back_to_start(self):
        from frames.StartWindow import StartWindow
        self.clean()
        start_win = StartWindow(self.root)
    
    def start_test(self):
        self.clean()
        test_win = TestWindow(self.root, self._user)
          
    def watch_results(self):
        pass