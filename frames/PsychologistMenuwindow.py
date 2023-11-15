import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo, showwarning

from entities.Patient import Patient
from entities.User import User
from frames.ResultsWindow import ResultWindow
from frames.TestWindow import TestWindow


class PsychologistMenuWindow():
    def __init__(self, root:Tk, user:User):
        self.root = root
        self._user = user
        self._patient = None
        self._mode = 0#0-insert, 1-update
        self.connection = sqlite3.connect('storage/test.db')
        self.load_interface()
    
    def wrong_info(self):
        showerror(title='Error', message='Неверно заполнена информация о пациенте.')
    
    def save_confirmed_info(self):
        showinfo(title='Info', message='Информация сохранена.')

    def deletion_confirmed_info(self):#удалять каскадно, думаю (из таблицы результатов тоже)
        showerror(title='Info', message='Пациент и его результаты удалены.')

    def load_interface(self):
        self.user_lbl = ttk.Label(self.root, text = "Психолог: "+ str(self._user.get_name()))
        self.user_lbl.place(relx=0.1,rely=0.1)
        
        self.cancel = ttk.Button(self.root, text = 'Выйти', command=self.back_to_start)
        self.cancel.place(relx=0.9,rely=0.1)


        self.make_patient_treeview()
        self.load_right_interface()

    def make_patient_treeview(self):
        self.patient_label = ttk.Label(self.root, text='Пациенты')
        self.patient_label.place(relx=0.1,rely=0.27, anchor=CENTER)
        
        self.refresh_btn = ttk.Button(self.root, text = 'Обновить', command=self.refresh_treeview)
        self.refresh_btn.place(relx= 0.22, rely = 0.25)
        
        
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

        self.add_btn = ttk.Button(self.root, text='Добавить', command=self.add_patient)
        self.add_btn.place(relx=0.2, rely=0.7)
        self.tree.bind('<ButtonRelease-1>', self.selectItem)
        self.all_results_button = ttk.Button(self.root, text='Просмотр всех результатов', command=self.show_all_results)
        self.all_results_button.place(relx=0.2, rely=0.7)
        self.refresh_treeview()

    def show_all_results(self):
        self.clean()
        res_win = ResultWindow(self.root, user=self._user, patient=0)

    def show_ones_results(self):
        if self._patient ==None:
            showwarning(title='warning', message='Выберите пациента.')
            return
        self.clean()
        res_win = ResultWindow(self.root, user=self._user, patient= self._patient)

    def refresh_treeview(self):
        self.tree.delete(*self.tree.get_children())
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM patients WHERE psy_id=(select id from users where name=?);', (self._user.get_name(),))
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert("", END, values=(row[0],row[2],row[3],row[4],row[5],row[6]))

    def selectItem(self,e):
        curItem = self.tree.focus()
        item = self.tree.item(curItem)['values']
        self._patient = Patient(item[0],item[1],item[2],item[3],item[4],item[5])

        self.enable_entries()
        self.clean_entries()
        self.surname_entry.insert(0,item[1])
        self.name_entry.insert(0, item[2])
        self.patronymic_entry.insert(0, item[3])
        self.age_entry.insert(0,str(item[4]))
        self.notes_entry.insert('1.0',item[5])
        self.disable_entries()


    def load_right_interface(self):
        def select_mode(x):
            if x:
                self.save_editing()
            else:
                self.save_new_patient()

        self.charecter_lbl = ttk.Label(self.root, text='Характеристика пациента')
        self.charecter_lbl.place(relx=0.6, rely=0.1)

        self.surname_lbl = ttk.Label(self.root, text='Фамилия:')
        self.surname_lbl.place(relx=0.6, rely=0.2)
        self.name_lbl = ttk.Label(self.root, text='Имя:')
        self.name_lbl.place(relx=0.6, rely=0.25)
        self.patronymic_lbl = ttk.Label(self.root, text='Отчество:')
        self.patronymic_lbl.place(relx=0.6, rely=0.3)
        self.age_lbl = ttk.Label(self.root, text='Возраст:')
        self.age_lbl.place(relx=0.6, rely=0.35)
        self.notes_lbl = ttk.Label(self.root, text='Описание:')
        self.notes_lbl.place(relx=0.6, rely=0.4)

        self.surname_entry = ttk.Entry(self.root, state='disabled')
        self.surname_entry.place(relx=0.7, rely=0.2)
        self.name_entry = ttk.Entry(self.root, state='disabled')
        self.name_entry.place(relx=0.7, rely=0.25)
        self.patronymic_entry = ttk.Entry(self.root, state='disabled')
        self.patronymic_entry.place(relx=0.7, rely=0.3)
        self.age_entry = ttk.Entry(self.root, state='disabled')
        self.age_entry.place(relx=0.7, rely=0.35)
        self.notes_entry = Text(self.root, width=30, height=5, state='disabled')
        self.notes_entry.place(relx=0.7, rely=0.4)

        self.delete_btn = ttk.Button(self.root, text='Удалить', command=self.delete_patient)
        self.delete_btn.place(relx=0.7, rely=0.6)
        self.edit_btn = ttk.Button(self.root, text='Редактировать', command=self.editing)
        self.edit_btn.place(relx=0.7, rely=0.65)
        self.save_editing_btn = ttk.Button(self.root, text='Сохранить', command=lambda:select_mode(self._mode) )
        self.save_editing_btn.place(relx=0.7, rely=0.70)
        self.start_test_btn = ttk.Button(self.root, text = 'Тестирование', command=self.start_test)
        self.start_test_btn.place(relx=0.7, rely=0.75)
        self.ones_results_btn = ttk.Button(self.root, text = 'Посмотреть результаты', command=self.show_ones_results)
        self.ones_results_btn.place(relx=0.7, rely=0.80)


    def enable_entries(self):
        self.surname_entry.configure(state='enabled')
        self.name_entry.configure(state='enabled')
        self.patronymic_entry.configure(state='enabled')
        self.age_entry.configure(state='enabled')
        self.notes_entry.configure(state='normal')

    def disable_entries(self):
        self.surname_entry.configure(state='disabled')
        self.name_entry.configure(state='disabled')
        self.patronymic_entry.configure(state='disabled')
        self.age_entry.configure(state='disabled')
        self.notes_entry.configure(state='disabled')
    
    def clean_entries(self):
        self.surname_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.patronymic_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.notes_entry.delete(1.0,END)

    def add_patient(self):
        self._mode = 0
        self.enable_entries()
        self.clean_entries()

    
    def delete_patient(self):
        if self._patient ==None:
            showwarning(title='warning', message='Выберите пациента.')
            return
        cursor = self.connection.cursor()
        try:
            cursor.execute('DELETE FROM patients WHERE psy_id=(SELECT id FROM USERS WHERE name = ?) AND f=? AND i=? AND o=? AND age=?;',
                    (self._user.get_name(), self.surname_entry.get(), self.name_entry.get(), self.patronymic_entry.get(), int(self.age_entry.get()),))
            self.connection.commit()
            self.deletion_confirmed_info()
            self._patient=None
        except:
            self.wrong_info()
    
    def editing(self):
        if self._patient ==None:
            showwarning(title='warning', message='Выберите пациента.')
            return
        self._mode = 1
        self.enable_entries()

    def save_editing(self):

        cursor = self.connection.cursor()
        try:
            cursor.execute('UPDATE patients SET f=?, i=?, o=?, age=?, notes=? WHERE psy_id = (SELECT id FROM users WHERE name = ?) AND id = ?;',
                    (self.surname_entry.get(), self.name_entry.get(), self.patronymic_entry.get(), int(self.age_entry.get()), self.notes_entry.get("1.0",'end-1c'),
                        self._user.get_name(), self._patient.get_id()))
            self.connection.commit()
            self._patient = Patient(self._patient.get_id(),self.surname_entry.get(), self.name_entry.get(), self.patronymic_entry.get(), int(self.age_entry.get()), self.notes_entry.get("1.0",'end-1c'))
            self.save_confirmed_info()
            self.disable_entries()
            self.refresh_treeview()
            
        except:
            self.wrong_info()
    
    def save_new_patient(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('INSERT INTO patients (psy_id, f, i, o, age, notes) values\
                            ((SELECT id FROM users WHERE name = ?),?,?,?,?,?);',
                    (self._user.get_name(),self.surname_entry.get(), self.name_entry.get(), self.patronymic_entry.get(), int(self.age_entry.get()), self.notes_entry.get("1.0",'end-1c'),))
            
            self.connection.commit()

            cursor.execute('SELECT * FROM patients WHERE psy_id=(select id from users where name=?) AND f=? AND i=? AND o=?;',\
                            (self._user.get_name(),self.surname_entry.get(), self.name_entry.get(), self.patronymic_entry.get(),))
            new_id = cursor.fetchall()[0]
            self._patient = Patient(new_id,self.surname_entry.get(), self.name_entry.get(), self.patronymic_entry.get(), int(self.age_entry.get()), self.notes_entry.get("1.0",'end-1c'))
            self.save_confirmed_info()
            self.disable_entries()
            self.refresh_treeview()
            
        except:
            self.wrong_info()
    
    def start_test(self):
        if self._patient ==None:
            showwarning(title='warning', message='Выберите пациента.')
            return
        self.clean()
        test_win = TestWindow(self.root, self._user, self._patient)

    def back_to_start(self):
        self.clean()
        from frames.StartWindow import StartWindow
        start_win = StartWindow(self.root)
    
    def clean(self):
        self.connection.close()
        
        self.user_lbl.place_forget()
        self.cancel.place_forget()
        self.start_test_btn.place_forget()
        self.charecter_lbl.place_forget()
        self.surname_lbl.place_forget()
        self.name_lbl.place_forget()
        self.patronymic_lbl.place_forget()
        self.age_lbl.place_forget()
        self.notes_lbl.place_forget()
        self.surname_entry.place_forget()
        self.name_entry.place_forget()
        self.patronymic_entry.place_forget()
        self.age_entry.place_forget()
        self.notes_entry.place_forget()
        

        self.delete_btn.place_forget()
        self.edit_btn.place_forget()
        self.save_editing_btn.place_forget()
        self.ones_results_btn.place_forget()
        
        self.patient_label.place_forget()
        self.refresh_btn.place_forget()
        self.tree.place_forget()
        self.add_btn.place_forget()
        self.all_results_button.place_forget()



