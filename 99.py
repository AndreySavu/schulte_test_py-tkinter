import random
import time
from tkinter import *
from tkinter import Tk, ttk

from entities.Table import Table


class TestWindow:
    def autoc(self):
        self.time_label.configure(text= f'Время: {str(int(time.time()) - self.start_time)}' )
        self.root.after(1000, self.autoc)

    def table_controller(self):
        #print('-----',self.elems, self.table_num)
        if self.current_table != self.table_num[-1]:
            self.current_table=self.table_num[-1]
            self.table_num_label.configure(text = f'Таблица {self.table_num[-1]}')
            
            self.array_elems_times.append((self.elems, str(int(time.time()) - self.start_time)))
            self.elems = []#очищаем массив для результата
            self.start_time = int(time.time())#обнуляем счетчик
            self.show_table()#выводим новую таблицу
            
            
            print(self.array_elems_times)
        
        self.root.after(1000, self.table_controller)

    def start(self, iter=0):
        self.table_num_label.place(relx=0.5, rely=0.06)
        self.start_time = int(time.time())

        self.table_num_label.configure(text = f'Таблица {self.table_num[-1]}')
        self.start_button.place_forget()
        
        self.table_controller()
        self.autoc()
        self.show_table()#выводим первую таблицу
    
    def show_table(self):
        tab = Table(self.root, 5, self.elems, self.table_num)

    def __init__(self):
                    #объект Tkinter------
        self.root = Tk()
        self.root.geometry('1024x600')
        self.root.title("Тестирование Шульте")
        
        self.elems = []
        '''тут храним список (список номеров, время прохождения) для каждой таблицы.
        потом из количества номеров считаем сколько было ошибок на каждой таблице'''
        self.array_elems_times = []
        self.table_num = [1]


        self.number_of_tables = 0
        self.current_table = 1
        
        self.time = 0
        self.time_label = ttk.Label(self.root)
        self.table_num_label = ttk.Label(self.root, text = 'Таблица: 0')
        self.start_button = ttk.Button(self.root, text = 'Начать', command=self.start)
       
        self.time_label.place(relx=0.05, rely=0.06)
        self.start_button.place(relx=0.5, rely=0.6)
        
        self.root.mainloop()


app = TestWindow()