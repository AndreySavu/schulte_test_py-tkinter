
import sqlite3
from tkinter import *
from tkinter import Tk, ttk

from entities.PatientResults import PatientResults


class PsychologistResults(PatientResults):
    def load_from_db(self):
        connection = sqlite3.connect('storage/test.db')
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT patient_results.*, patients.f, patients.i, patients.o FROM patient_results \
                            LEFT JOIN patients ON patients.id = patient_results.patient_id;")
            rows = cursor.fetchall()
        except:
            self.load_error()

        connection.close()
        if len(rows)==0:
            return None
        return rows
    
    def insert_results(self):
        self.tree.delete(*self.tree.get_children())
        for i in self._results:
            self.tree.insert("", END, values=(f'{i[7]} {i[8][:1]}. {i[9][:1]}.',i[4],i[6],i[5],i[3],i[2].split(' ')[0],i[2].split(' ')[1]))
    
    def make_interface(self):
        columns = ('#1', "#2", "#3", "#4", "#5", "#6","#7")
        self.tree = ttk.Treeview(self.root, show="headings", columns=columns, height=18)
        
        self.tree.column('#1', width=100)
        self.tree.column('#2', width=84)
        self.tree.column('#3', width=72)
        self.tree.column('#4', width=59)
        self.tree.column('#5', width=59)
        self.tree.column('#6', width=67)
        self.tree.column('#7', width=57)

        self.tree.heading("#1", text="ФИО",command=lambda: self.sort(0, False))
        self.tree.heading("#2", text="Размерность",command=lambda: self.sort(1, False))
        self.tree.heading("#3", text="Время прохождения",command=lambda: self.sort(2, False))
        self.tree.heading("#4", text="N ошибок",command=lambda: self.sort(3, False))
        self.tree.heading("#5", text="N таблицы",command=lambda: self.sort(4, False))
        self.tree.heading("#6", text="Дата",command=lambda: self.sort(5, False))
        self.tree.heading("#7", text="Время",command=lambda: self.sort(6, False))

        self.tree.pack()