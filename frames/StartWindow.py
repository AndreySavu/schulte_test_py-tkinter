from tkinter import *
from tkinter import ttk

from frames.AuthorizationWindow import AuthorizationWindow
from frames.TestWindow import TestWindow


class StartWindow:
    def __init__(self, root:Tk):
        self.root = root
        self.process = ttk.Label(self.root, text = 'Выберите роль')
        self.button1 = ttk.Button(self.root, text = 'Гость', command=self.continue_as_guest)
        self.button2 = ttk.Button(self.root, text = 'Пользователь', command=self.continue_as_user)
        self.button3 = ttk.Button(self.root, text = 'Психоаналитик', command=self.continue_as_psychologist)
        
        self.process.place(relx = 0.5, rely = 0.3, anchor='center')
        self.button1.place(relx = 0.25, rely = 0.6, anchor='center')
        self.button2.place(relx = 0.50, rely = 0.6, anchor='center')
        self.button3.place(relx = 0.75, rely = 0.6, anchor='center')
    
    def clean(self):
        self.process.place_forget()
        self.button1.place_forget()
        self.button2.place_forget()
        self.button3.place_forget()


    def continue_as_guest(self):
        test_win = TestWindow(self.root)
        self.clean()
    
    def continue_as_user(self):
        auth_win = AuthorizationWindow(self.root, 0)
        self.clean()
    def continue_as_psychologist(self):
        auth_win = AuthorizationWindow(self.root, 1)
        self.clean()
        

        
        

