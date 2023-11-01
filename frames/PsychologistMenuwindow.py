import sqlite3
from tkinter import *
from tkinter import ttk

from entities.Patient import Patient
from entities.User import User


class PsychologistMenuWindow():
    def load_interface(self):
        self.user_lbl = ttk.Label(self.root, text = "Психолог: "+ str(self.__user__.get_name()))\
                        .place(relx=0.1,rely=0.1)
        
        self.cancel = ttk.Button(self.root, text = 'Выйти', command=self.back_to_start)\
                        .place(relx=0.9,rely=0.1)

        self.start_test_btn = ttk.Button(self.root, text = 'Тестирование', command=self.start_test)\
                        .place(relx=0.5, rely=0.8)
        self.make_patient_treeview()
        self.load_right_interface()

    def make_patient_treeview(self):
        self.patient_label = ttk.Label(self.root, text='Пациенты')\
                                        .place(relx=0.1,rely=0.27, anchor=CENTER)
        
        self.refresh_btn = ttk.Button(self.root, text = 'Обновить', command=self.refresh_treeview)\
                                        .place(relx= 0.22, rely = 0.25)
        
        
        columns = ('#1', "#2", "#3", "#4", '#5', '6')
        self.tree = ttk.Treeview(self.root, show="headings", columns=columns)
        
        self.tree.column('#1', width=20)
        self.tree.column('#2', width=100)
        self.tree.column('#3', width=100)
        self.tree.column('#4', width=100)
        self.tree.column('#5', width=100)
        self.tree.column('#6', width=100)
        self.tree.heading("#1", text="id")
        self.tree.heading("#2", text="Фамилия")
        self.tree.heading("#3", text="Имя")
        self.tree.heading("#4", text="Отчество")
        self.tree.heading("#5", text="Возраст")
        self.tree.heading("#6", text="Описание")
        self.tree.place(relx=0.01, rely=0.5, anchor=W)

        self.add_btn = ttk.Button(self.root, text='Добавить', command=self.add_patient).place(relx=0.2, rely=0.7)
        self.tree.bind('<ButtonRelease-1>', self.selectItem)
        self.refresh_treeview()

    def refresh_treeview(self):
        self.tree.delete(*self.tree.get_children())
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM patients WHERE psy_id=(select id from users where name=?);', (self.__user__.get_name(),))
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert("", END, values=(row[0],row[2],row[3],row[4],row[5],row[6]))

    def selectItem(self,e):
        curItem = self.tree.focus()
        print (self.tree.item(curItem))


    def load_right_interface(self):

        self.charecter_lbl = ttk.Label(self.root, text='Характеристика пациента').place(relx=0.6, rely=0.1)

        self.surname_lbl = ttk.Label(self.root, text='Фамилия:').place(relx=0.6, rely=0.2)
        self.name_lbl = ttk.Label(self.root, text='Имя:').place(relx=0.6, rely=0.25)
        self.patronymic_lbl = ttk.Label(self.root, text='Отчество:').place(relx=0.6, rely=0.3)
        self.age_lbl = ttk.Label(self.root, text='Возраст:').place(relx=0.6, rely=0.35)
        self.notes_lbl = ttk.Label(self.root, text='Описание:').place(relx=0.6, rely=0.4)

        self.surname_entry = ttk.Entry(self.root, state='disabled').place(relx=0.7, rely=0.2)
        self.name_entry = ttk.Entry(self.root, state='disabled').place(relx=0.7, rely=0.25)
        self.patronymic_entry = ttk.Entry(self.root, state='disabled').place(relx=0.7, rely=0.3)
        self.age_entry = ttk.Entry(self.root, state='disabled').place(relx=0.7, rely=0.35)
        self.notes_entry = Text(self.root, width=30, height=5, state='disabled').place(relx=0.7, rely=0.4)

        self.delete_btn = ttk.Button(self.root, text='Удалить', command=self.delete_patient).place(relx=0.7, rely=0.6)
        self.edit_btn = ttk.Button(self.root, text='Редактировать', command=self.editing).place(relx=0.7, rely=0.65)
        self.save_editing_btn = ttk.Button(self.root, text='Сохранить', command=self.save_editing).place(relx=0.7, rely=0.70)

    def enable_entries(self):
        self.surname_entry.configure(state='enabled')
        self.name_entry.configure(state='enabled')
        self.patronymic_entry.configure(state='enabled')
        self.age_entry.configure(state='enabled')
        self.notes_entry.configure(state='enabled')

    def disable_entries(self):
        self.surname_entry.configure(state='disabled')
        self.name_entry.configure(state='disabled')
        self.patronymic_entry.configure(state='disabled')
        self.age_entry.configure(state='disabled')
        self.notes_entry.configure(state='disabled')
    
    def add_patient(self):
        self.enable_entries()

    
    def delete_patient(self):
        pass

    def editing(self):
        pass

    def save_editing(self):
        self.__patient__=Patient()
    
    def start_test(self):
        pass

    def back_to_start(self):
        self.clean()
        from frames.StartWindow import StartWindow
        start_win = StartWindow(self.root)
    
    def clean(self):
        self.connection.close()
        
        self.user_lbl.place_forget()
        self.cancel.place_forget()

    def __init__(self, root:Tk, user:User):
        self.root = root
        self.__user__ = user
        self.__patient__ = None
        self.connection = sqlite3.connect('storage/test.db')
        self.load_interface()