import sqlite3
from tkinter import *
from tkinter import Tk, ttk

from entities.PatientResults import PatientResults


class UserResults(PatientResults):
    def load_from_db(self):
        connection = sqlite3.connect('storage/test.db')
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT user_results.*, users.name FROM user_results \
                            LEFT JOIN users ON users.id = user_results.user_id\
                            WHERE user_id = (SELECT id FROM users WHERE name =?);",
                            (self._user.get_name(),))
            rows = cursor.fetchall()
            
            cursor.execute("SELECT user_results.*, users.name FROM user_results \
                            LEFT JOIN users ON users.id = user_results.user_id\
                            WHERE private=1 AND user_id != (SELECT id FROM users WHERE name =?);",
                            (self._user.get_name(),))
            rows+=cursor.fetchall()
        except:
            self.load_error()

        connection.close()
        if len(rows)==0:
            return None
        return rows

    def insert_results(self, dim_word='любая'):
        word_to_dim={
            'любая':True,
            '3x3':3,
            '4x4':4,
            '5x5':5,
            '6x6':6,
            '7x7':7
        }
        self.tree.delete(*self.tree.get_children())
        self._filtered_results =[]
        if self.var.get()==0:
            for i in self._results:
                if i[8] == self._user.get_name() and (word_to_dim[dim_word]==True or word_to_dim[dim_word]==i[4]):
                    self.tree.insert("", END, values=(i[8],i[4],i[6],i[5],i[3],i[2].split(' ')[0],i[2].split(' ')[1]))
                    self._filtered_results.append(i)
        else:
            for i in self._results:
                if word_to_dim[dim_word]==True or word_to_dim[dim_word]==i[4]:
                    self.tree.insert("", END, values=(i[8],i[4],i[6],i[5],i[3],i[2].split(' ')[0],i[2].split(' ')[1]))
                    self._filtered_results.append(i)
    
    def make_interface(self):
        self.var = IntVar()
        self.checkbutton = ttk.Checkbutton(self.root, text="Показать результат других", variable=self.var, command=self.insert_results)
        
        columns = ('#1', "#2", "#3", "#4", "#5", "#6","#7")
        self.tree = ttk.Treeview(self.root, show="headings", columns=columns, height=18)
        
        self.tree.column('#1', width=100)
        self.tree.column('#2', width=84)
        self.tree.column('#3', width=72)
        self.tree.column('#4', width=59)
        self.tree.column('#5', width=59)
        self.tree.column('#6', width=67)
        self.tree.column('#7', width=57)

        self.tree.heading("#1", text="Имя",command=lambda: self.sort(0, False))
        self.tree.heading("#2", text="Размерность",command=lambda: self.sort(1, False))
        self.tree.heading("#3", text="Время прохождения",command=lambda: self.sort(2, False))
        self.tree.heading("#4", text="N ошибок",command=lambda: self.sort(3, False))
        self.tree.heading("#5", text="N таблицы",command=lambda: self.sort(4, False))
        self.tree.heading("#6", text="Дата",command=lambda: self.sort(5, False))
        self.tree.heading("#7", text="Время",command=lambda: self.sort(6, False))
        
        self.checkbutton.pack()
        self.tree.pack()