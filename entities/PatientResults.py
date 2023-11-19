
import sqlite3
from tkinter import *
from tkinter import Tk, ttk
from tkinter.messagebox import showerror


class PatientResults():
    def __init__(self, root:Tk, user=None):
        self.root = root
        self._user = user
        self._results = self.load_from_db()
        self._filtered_results = self._results
        
        if self._results == None:
            self.no_results_label = ttk.Label(self.root, text = "Пока нет результатов тестирования.")
            self.no_results_label.place(relx=0.3, rely=0.5)
        else:
            self.make_interface()
            self.insert_results()
    
    def make_interface(self):
        columns = ('#1', "#2", "#3", "#4", "#5", "#6")
        self.tree = ttk.Treeview(self.root, show="headings", columns=columns, height=18)
        
        self.tree.column('#1', width=100)
        self.tree.column('#2', width=88)
        self.tree.column('#3', width=75)
        self.tree.column('#4', width=75)
        self.tree.column('#5', width=82)
        self.tree.column('#6', width=73)


        self.tree.heading("#1", text="Размерность",command=lambda: self.sort(0, False))
        self.tree.heading("#2", text="Время прохождения",command=lambda: self.sort(1, False))
        self.tree.heading("#3", text="N ошибок",command=lambda: self.sort(2, False))
        self.tree.heading("#4", text="N таблицы",command=lambda: self.sort(3, False))
        self.tree.heading("#5", text="Дата",command=lambda: self.sort(4, False))
        self.tree.heading("#6", text="Время",command=lambda: self.sort(5, False))
        
        self.tree.pack()
    
    def get_selected_results(self):
        return self.tree.item(self.tree.selection())['values']
    
    def get_results(self):
        return self._filtered_results
    
    def load_error(self):
        showerror(title='Error', message='Ошибка при загрузке результатов.')
    
    def load_from_db(self):
        connection = sqlite3.connect('storage/test.db')
        cursor = connection.cursor()
        rows=[]
        try:
            cursor.execute("SELECT * FROM patient_results \
                            WHERE patient_id = ?;",
                            (self._user.get_id(),))
            rows = cursor.fetchall()
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
        self._filtered_results =[]
        self.tree.delete(*self.tree.get_children())
        for i in self._results:
            if word_to_dim[dim_word]==True or word_to_dim[dim_word]==i[4]:
                self.tree.insert("", END, values=(i[4],i[6],i[5],i[3],i[2].split(' ')[0],i[2].split(' ')[1]))
                self._filtered_results.append(i)

    
    def sort(self, col, reverse):
        # получаем все значения столбцов в виде отдельного списка
        l = [(self.tree.set(k, col), k) for k in self.tree.get_children("")]
        # сортируем список
        l.sort(reverse=reverse)
        # переупорядочиваем значения в отсортированном порядке
        for index,  (_, k) in enumerate(l):
            self.tree.move(k, "", index)
        # в следующий раз выполняем сортировку в обратном порядке
        self.tree.heading(col, command=lambda: self.sort(col, not reverse))


