import random
import time
from tkinter import *
from tkinter import Tk, ttk

from entities.Table import Table
from entities.User import User


class TestWindow:
    def init_selectors(self):
        self.select_number = ttk.Label(self.root, text = 'Выберите количество таблиц')
        self.select_dimension = ttk.Label(self.root, text = 'Выберите размерность таблиц')
        
        self.spinbox_var1 = StringVar(value=1)
        self.spinbox1 = ttk.Spinbox(from_=1, to=10, increment=1, textvariable=self.spinbox_var1)
        self.spinbox_var2 = StringVar(value=5)
        self.spinbox2 = ttk.Spinbox(from_=3, to=7, increment=1, textvariable=self.spinbox_var2)

        self.select_number.place(relx=0.2,rely=0.4)
        self.spinbox1.place(relx=0.2,rely=0.45)
        self.select_dimension.place(relx=0.7,rely=0.4)
        self.spinbox2.place(relx=0.7,rely=0.45)

    def destroy_selectrors(self):
        self.select_number.destroy()
        self.spinbox1.destroy()
        self.select_dimension.destroy()
        self.spinbox2.destroy()

    def clean(self):
        self.select_number.place_forget()
        self.select_dimension.place_forget()
        self.spinbox1.place_forget()
        self.spinbox2.place_forget()
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
            self.array_elems_times.append((self.elems, str(int(time.time()) - self.start_time)))
            
            self.raw_result()
            return#конец
        
        if self.current_table != self.table_num[-1] :
            self.current_table=self.table_num[-1]
            self.table_num_label.configure(text = f'Таблица {self.table_num[-1]}')
            self.array_elems_times.append((self.elems, str(int(time.time()) - self.start_time)))

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
        tab = Table(self.root, self.dim, self.elems, self.table_num)

    def raw_result(self):
        print(self.array_elems_times)

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
