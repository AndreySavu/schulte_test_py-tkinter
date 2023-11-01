import random
import time
from tkinter import *
from tkinter import Tk, ttk

from entities.Results import Results
from entities.Table import Table
from entities.User import User


class TestWindow:
    def init_selectors(self):
        self.select_number = ttk.Label(self.root, text = 'Выберите количество таблиц')
        self.select_dimension = ttk.Label(self.root, text = 'Выберите размерность таблиц')
        
        self.spinbox_var1 = StringVar(value=1)
        self.spinbox1 = ttk.Spinbox(self.root, from_=1, to=10, increment=1, textvariable=self.spinbox_var1)
        self.spinbox_var2 = StringVar(value=5)
        self.spinbox2 = ttk.Spinbox(self.root, from_=3, to=7, increment=1, textvariable=self.spinbox_var2)

        self.select_number.place(relx=0.2,rely=0.4)
        self.spinbox1.place(relx=0.2,rely=0.45)
        self.select_dimension.place(relx=0.7,rely=0.4)
        self.spinbox2.place(relx=0.7,rely=0.45)

    def destroy_selectrors(self):
        self.select_number.place_forget()
        self.spinbox1.place_forget()
        self.select_dimension.place_forget()
        self.spinbox2.place_forget()

    def clean(self):
        self.destroy_selectrors()

        self.time_label.place_forget()
        self.table_num_label.place_forget()
        self.instruction_button.place_forget()
        self.start_button.place_forget()

    def autoc(self):
        self.time_label.configure(text= f'Время: {str(int(time.time()) - self.start_time)}' )
        self.root.after(1000, self.autoc)

    def table_controller(self):
        #print(self.spinbox_var1.get(), self.spinbox_var2.get())
        if self.table_num[-1]>self.number_of_tables:
            self.array_elems_times.append((self.elems, int(time.time()) - self.start_time))
            
            self.clean()
            self.raw_result()
            return#конец
        
        if self.current_table != self.table_num[-1] :
            self.current_table=self.table_num[-1]
            self.table_num_label.configure(text = f'Таблица {self.table_num[-1]}')
            self.array_elems_times.append((self.elems, int(time.time()) - self.start_time))

            self.elems = []#очищаем массив для результата
            self.start_time = int(time.time())#обнуляем счетчик
            self.show_table()#выводим новую таблицу
            
            
        self.root.after(1000, self.table_controller)

    def start(self, iter=0):
        
        self.table_num_label.place(relx=0.5, rely=0.06)
        self.start_time = int(time.time())
        
        #присваиваем значения количеству таблиц и размерности из spinbox'ов
        self.number_of_tables = int(self.spinbox_var1.get())
        self.dim = int(self.spinbox_var2.get())
        self.destroy_selectrors()#убираем селекторы
        
        self.table_num_label.configure(text = f'Таблица {self.table_num[-1]}')
        self.start_button.place_forget()
        
        self.table_controller()
        self.autoc()
        self.show_table()#выводим первую таблицу
    
    def show_table(self):
        self.tab = Table(self.root, self.dim, self.elems, self.table_num)

    def make_treeview_for_results(self):
        self.result_label = ttk.Label(self.root, text='Результат')
        columns = ('#1', "#2", "#3", "#4")
        self.tree = ttk.Treeview(self.root, show="headings", columns=columns)
        
        self.tree.column('#1', width=150)
        self.tree.column('#2', width=150)
        self.tree.column('#3', width=150)
        self.tree.column('#4', width=150)
        self.tree.heading("#1", text="Номер таблицы")
        self.tree.heading("#2", text="Ошибочные нажатия")
        self.tree.heading("#3", text="Количество ошибок")
        self.tree.heading("#4", text="Время, сек")
        self.tree.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.result_label.place(relx=0.5,rely=0.27, anchor=CENTER)

    def raw_result(self):
        res = Results(self.array_elems_times, self.dim).get_mistakes_num_of_mistakes_time()
        #Table.make_center_frame(self)
        self.make_treeview_for_results()

        for i in range(len(res)):
            self.tree.insert("", END, values=(i+1,res[i][0],res[i][1],res[i][2]))
        

    def show_instruction(self):
        frame = Tk()
        frame.geometry('300x200')
        frame.title('Инструкция')
        text = Text(frame, height = 12, width = 52)
        text.pack()
        with open('entities/instruction.txt', 'r') as reader:
            text.insert(END, reader.read())
        frame.mainloop()
    
    def __init__(self, root:Tk, user=None, num_tables=None, dimension=None,  patient=None):
        self.root = root
        self.number_of_tables = num_tables#количество таблиц
        self.dim = dimension#размерность таблицы
        self.current_table = 1#начинаем с первой таблицы
        
        self.elems = []#для хванения номеров текущей таблицы
        '''тут храним список (список номеров, время прохождения) для каждой таблицы.
        потом из количества номеров считаем сколько было ошибок в каждой таблице'''
        self.array_elems_times = []
        self.table_num = [1]#очевидный костыль, чтобы из table.py увеличивать current_table

        self.time_label = ttk.Label(self.root)
        self.table_num_label = ttk.Label(self.root, text = 'Таблица: 0')
        self.start_button = ttk.Button(self.root, text = 'Начать', command=self.start)
        self.instruction_button = ttk.Button(self.root, text = 'Инструкция', command=self.show_instruction)
        
        self.time_label.place(relx=0.05, rely=0.06)
        self.start_button.place(relx=0.5, rely=0.6)
        self.instruction_button.place(relx=0.8, rely=0.1)
        self.init_selectors()
