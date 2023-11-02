import hashlib
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo


class RegistrationWindow():
    def toggle(self):
        if self.e_password.cget('show') == "":
            self.e_password.config(show = "*")
            self.e_password2.config(show = "*")
        else:
            self.e_password.config(show = "")
            self.e_password2.config(show = "")
    
    def wrong_name(self):
        showerror(title='Error', message='Пользователь с таким именем уже существует.')

    def wrong_data(self):
        showerror(title='Error', message='Заполните все поля.')

    def different_passwords(self):
        showerror(title='Error', message='Пароли не совпадают.')
    
    def user_added(self):
        showinfo(title='Info', message='Новый пользователь добавлен.')
    
    def back_to_start(self):
        self.clean()
        from frames.StartWindow import StartWindow
        start_win = StartWindow(self.root)


    def create_new_user(self):
        if self.e_login.get()=='' or self.e_password.get()=='' or self.e_age.get()=='':
            self.wrong_data()
            return
        
        if self.e_password.get()!= self.e_password2.get():
            self.different_passwords()
            return
        
        connection = sqlite3.connect('storage/test.db')
        cursor = connection.cursor()
        h = hashlib.shake_256(self.e_password.get().encode('utf-8'))
        try:
            #print((self.e_login.get(),h.hexdigest(20), self.e_age.get(), self.var.get()))
            cursor.execute('INSERT INTO users (name, password, age, type) values (?, ?, ?, ?);',
                    (self.e_login.get(),h.hexdigest(20), self.e_age.get(), self.var.get(),))
            self.user_added()
            connection.commit()
            connection.close()
            self.clean()
            from frames.AuthorizationWindow import AuthorizationWindow
            auth_win = AuthorizationWindow(self.root, self.var.get())
            
        except:
            self.wrong_name()


    def __init__(self, root: Tk):
        self.root = root
        self.var = IntVar()
        #все элементы окна
        self.process = ttk.Label(self.root, text = 'Создание новой учетной записи')
        self.l_age = ttk.Label(self.root, text = 'Ваш возраст: ')
        self.l_login = ttk.Label(self.root, text = 'Логин: ')
        self.l_password = ttk.Label(self.root, text = 'Пароль: ')
        self.l_password2 = ttk.Label(self.root, text = 'Пароль еще раз: ')
        
        self.e_age = ttk.Entry(self.root)
        self.e_login = ttk.Entry(self.root)
        self.e_password = ttk.Entry(self.root, show = "*")
        self.e_password2 = ttk.Entry(self.root, show = "*")
        self.checkbutton = ttk.Checkbutton(self.root, text="Показать пароль", onvalue=False, offvalue=True, command=self.toggle)
        self.be_psycologist = ttk.Checkbutton(self.root, text="Быть психологом", variable=self.var)
        self.enter = ttk.Button(self.root, text="Создать", command=self.create_new_user)
        self.cancel = ttk.Button(self.root, text="Отмена", command=self.back_to_start)
        
        self.process.place(relx = 0.5, rely = 0.3)
        self.l_age.place(relx = 0.4, rely = 0.35)
        self.l_login.place(relx = 0.4, rely = 0.4)
        self.l_password.place(relx = 0.4, rely = 0.45)
        self.l_password2.place(relx = 0.4, rely = 0.5)
        
        self.e_age.place(relx = 0.5, rely = 0.35)
        self.e_login.place(relx = 0.5, rely = 0.4)
        self.e_password.place(relx = 0.5, rely = 0.45)
        self.e_password2.place(relx = 0.5, rely = 0.5)
        
        self.checkbutton.place(relx = 0.65, rely = 0.5)
        self.be_psycologist.place(relx = 0.5, rely = 0.55)
        self.enter.place(relx = 0.5, rely = 0.65)
        self.cancel.place(relx = 0.6, rely = 0.65)


    def clean(self):
        self.process.place_forget()
        self.l_age.place_forget()
        self.l_login.place_forget()
        self.l_password.place_forget()
        self.l_password2.place_forget()
        
        self.e_age.place_forget()
        self.e_login.place_forget()
        self.e_password.place_forget()
        self.e_password2.place_forget()
        
        self.checkbutton.place_forget()
        self.be_psycologist.place_forget()
        self.enter.place_forget()
        self.cancel.place_forget()