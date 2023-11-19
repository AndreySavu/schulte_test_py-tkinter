from tkinter import *
from tkinter import ttk

from frames.AuthorizationWindow import AuthorizationWindow
from frames.TestWindow import TestWindow


class StartWindow:
    def __init__(self, root:Tk):
        self.root = root
        self.make_interface()
    
    def make_interface(self):
        s1 = ttk.Style()
        s1.configure('my.TLabel', font=('Arial', 11), justify='center')
        s2 = ttk.Style()
        s2.configure('my.TButton', font=('Arial', 11))
        self.naming_label = ttk.Label(self.root, text = 'Программное обеспечение для проведения тестирования\nпо методике Шульте', style='my.TLabel')
        self.process_label = ttk.Label(self.root, text = 'Выберите роль', style='my.TLabel')
        self.button1 = ttk.Button(self.root, text = 'Гость',padding=(5,5), style='my.TButton', command=self.continue_as_guest)
        self.button2 = ttk.Button(self.root, text = 'Пользователь',padding=(5,5), style='my.TButton', command=self.continue_as_user)
        self.button3 = ttk.Button(self.root, text = 'Психоаналитик',padding=(5,5), style='my.TButton', command=self.continue_as_psychologist)
        
        self.naming_label.place(relx = 0.5, rely = 0.25, anchor='center')
        self.process_label.place(relx = 0.5, rely = 0.5, anchor='center')
        self.button1.place(relx = 0.30, rely = 0.6, anchor='center')
        self.button2.place(relx = 0.50, rely = 0.6, anchor='center')
        self.button3.place(relx = 0.70, rely = 0.6, anchor='center')

    def clean(self):
        self.naming_label.place_forget()
        self.process_label.place_forget()
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
        

        
        

