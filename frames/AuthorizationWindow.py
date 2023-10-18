import hashlib
import sqlite3
import sys
from tkinter import *
from tkinter import font, ttk
from tkinter.messagebox import showerror, showinfo

sys.path.append('./')
from entities.User import User
from frames.RegisrationWindow import RegistrationWindow
from frames.UserMenuWindow import UserMenuWindow


class AuthorizationWindow():
    def toggle(self):
        if self.e_password.cget('show') == "":
            self.e_password.config(show = "*")
        else:
            self.e_password.config(show = "")
    
    def forgot_password_info(self,qq):
        showerror(title='Error', message='Не стоило забывать.')

    def wrong_password(self):
        showerror(title='Error', message='Не верный логин или пароль.')

    def entered_system(self):
        showinfo(title='Info', message='Выполнен вход.')

    def enter_system(self):
        connection = sqlite3.connect('storage/test.db')
        cursor = connection.cursor()
        h = hashlib.shake_256(self.e_password.get().encode('utf-8'))
        cursor.execute('SELECT * FROM users WHERE name=? AND password=? AND type=?;',
                       (self.e_login.get(),h.hexdigest(20),self.user_type,))
        print(self.e_login.get(),h.hexdigest(20),self.user_type)
        row = cursor.fetchall()
        print(row)
        if len(row)==0:
            self.wrong_password()
            return
        
        connection.close()
        self.clean()
        print(row[0][1], row[0][3],row[0][4])
        if(row[0][4]==0):
            menu_win = UserMenuWindow(self.root, User(row[0][1], row[0][3],row[0][4]))
        else:
            pass#тут окно для психолога

    def registration(self,qq):
        self.clean()
        reg_win = RegistrationWindow(self.root)
        
        

    def __init__(self, root:Tk, user_type):
        self.user_type = user_type
        label_font = font.Font(underline=True)
        self.root = root
        #все элементы окна
        self.process = ttk.Label(self.root, text = 'Введите логин и пароль')
        self.l_login = ttk.Label(self.root, text = 'Логин: ')
        self.l_password = ttk.Label(self.root, text = 'Пароль: ')
        self.e_login = ttk.Entry(self.root)
        self.e_password = ttk.Entry(self.root, show = "*")
        self.checkbutton = ttk.Checkbutton(self.root, text="Показать пароль", onvalue=False, offvalue=True, command=self.toggle)
        self.forgot_password = ttk.Label(self.root, text="Забыли пароль?", font = label_font)
        self.registrate = ttk.Label(self.root, text="Зарегистрироваться", font = label_font)
        self.enter = ttk.Button(self.root, text="Войти", command=self.enter_system)

        self.forgot_password.bind("<Button-1>", self.forgot_password_info)
        self.registrate.bind("<Button-1>", self.registration)
        
        self.process.place(relx = 0.5, rely = 0.3)
        self.l_login.place(relx = 0.4, rely = 0.4)
        self.l_password.place(relx = 0.4, rely = 0.5)
        self.e_login.place(relx = 0.5, rely = 0.4)
        self.e_password.place(relx = 0.5, rely = 0.5)
        self.checkbutton.place(relx = 0.65, rely = 0.5)
        self.forgot_password.place(relx = 0.4, rely = 0.55)
        self.registrate.place(relx = 0.4, rely = 0.6)
        self.enter.place(relx = 0.5, rely = 0.65)
    
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
        


