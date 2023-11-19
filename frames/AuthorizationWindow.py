import hashlib
import sqlite3
from tkinter import *
from tkinter import font, ttk
from tkinter.messagebox import showerror, showinfo

#sys.path.append('./')
from entities.User import User
from frames.PsychologistMenuWindow import PsychologistMenuWindow
from frames.RegisrationWindow import RegistrationWindow
from frames.UserMenuWindow import UserMenuWindow


class AuthorizationWindow():
    def __init__(self, root:Tk, user_type):
        self.user_type = user_type
        self.root = root
        self.init_interface()
        self.place_interface()
    
    def init_interface(self):
        label_font1 = font.Font(size =10)
        label_font2 = font.Font(underline=True, size =9)
        #все элементы окна
        self.process = ttk.Label(self.root, text = 'Введите логин и пароль', font = label_font1)
        self.l_login = ttk.Label(self.root, text = 'Логин: ')
        self.l_password = ttk.Label(self.root, text = 'Пароль: ')
        self.e_login = ttk.Entry(self.root)
        self.e_password = ttk.Entry(self.root, show = "*")
        self.checkbutton = ttk.Checkbutton(self.root, text="Показать пароль", onvalue=False, offvalue=True, command=self.toggle)
        self.forgot_password = ttk.Label(self.root, text="Забыли пароль?", font = label_font2)
        self.registrate = ttk.Label(self.root, text="Зарегистрироваться", font = label_font2)
        self.enter = ttk.Button(self.root, text="Войти", command=self.enter_system)
        self.go_back_button = ttk.Button(self.root, text="Назад", command=self.go_back)

        print(self.l_login['font'])
        self.forgot_password.bind("<Button-1>", self.forgot_password_info)
        self.registrate.bind("<Button-1>", self.registration)

    def place_interface(self):
        self.process.place(relx = 0.45, rely = 0.3)
        self.l_login.place(relx = 0.43, rely = 0.4)
        self.l_password.place(relx = 0.43, rely = 0.45)
        self.e_login.place(relx = 0.5, rely = 0.4)
        self.e_password.place(relx = 0.5, rely = 0.45)
        
        self.checkbutton.place(relx = 0.65, rely = 0.45)
        self.forgot_password.place(relx = 0.5, rely = 0.50)
        self.registrate.place(relx = 0.5, rely = 0.55)
        self.enter.place(relx = 0.55, rely = 0.65)
        self.go_back_button.place(relx = 0.45, rely = 0.65)
    
    def clean(self):
        self.process.place_forget()
        self.l_login.place_forget()
        self.l_password.place_forget()
        self.e_login.place_forget()
        self.e_password.place_forget()
        self.checkbutton.place_forget()
        self.forgot_password.place_forget()
        self.registrate.place_forget()
        self.enter.place_forget()
        self.go_back_button.place_forget()

    def go_back(self):
        from frames.StartWindow import StartWindow
        self.clean()
        win = StartWindow(self.root)
    
    def toggle(self):
        if self.e_password.cget('show') == "":
            self.e_password.config(show = "*")
        else:
            self.e_password.config(show = "")
    
    def forgot_password_info(self,qq):
        showerror(title='Error', message='Не стоило забывать.')

    def wrong_password_error(self):
        showerror(title='Error', message='Не верный логин или пароль.')

    def entered_system_info(self):
        showinfo(title='Info', message='Выполнен вход.')

    def enter_system(self):
        connection = sqlite3.connect('storage/test.db')
        cursor = connection.cursor()
        h = hashlib.shake_256(self.e_password.get().encode('utf-8'))
        cursor.execute('SELECT * FROM users WHERE name=? AND password=? AND type=?;',
                       (self.e_login.get(),h.hexdigest(20),self.user_type,))
        
        row = cursor.fetchall()
        if len(row)==0:
            self.wrong_password_error()
            return

        connection.close()
        self.clean()
        if(row[0][4]==0):
            menu_win = UserMenuWindow(self.root, User(row[0][1], row[0][3],row[0][4]))
        else:
            menu_win = PsychologistMenuWindow(self.root, User(row[0][1], row[0][3],row[0][4]))

    def registration(self,qq):
        self.clean()
        reg_win = RegistrationWindow(self.root)