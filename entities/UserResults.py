import sqlite3
from tkinter import *
from tkinter import Tk, ttk
from tkinter.messagebox import showerror, showinfo


class UserResults():
    def __init__(self, root:Tk, user):
        self.root = root
        self._user = user
        self._results = self.load_from_db()
        
        if self._results == None:
            self.no_results_label = ttk.Label(self.root, text = "Пока нет результатов тестирования.")
            self.no_results_label.place(relx=0.3, rely=0.5)
        else:
            self.make_interface()
            self.insert_results()
        
        
        #print(self._results)
    
    def get_selected_results(self):
        return self.tree.item(self.tree.selection())['values']
    
    def get_results(self):
        return self._results
    
    def load_error(self):
        showerror(title='Error', message='Ошибка при загрузке результатов.')
    
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
            #print(rows)
        except:
            self.load_error()

        connection.close()
        if len(rows)==0:
            return None
        return rows
    
    def insert_results(self):
        self.tree.delete(*self.tree.get_children())

        if self.var.get()==0:
            for i in self._results:
                if i[8] == self._user.get_name():
                    self.tree.insert("", END, values=(i[8],i[4],i[6],i[5],i[3],i[2].split(' ')[0],i[2].split(' ')[1]))
        else:
            for i in self._results:
                self.tree.insert("", END, values=(i[8],i[4],i[6],i[5],i[3],i[2].split(' ')[0],i[2].split(' ')[1]))
    
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
        
        # self.tree.place(relx=0.5, rely=0.1, anchor=N)
        # self.checkbutton.place(relx = 0.6, rely=0.01)
    