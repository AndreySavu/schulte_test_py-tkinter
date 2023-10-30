import sys
import time
from threading import Thread
from tkinter import *
from tkinter import Tk, ttk

sys.path.append('./')
from entities.User import User


class TestWindow():
    def autoc(self):
        # def update(self):
        #     while True:
        #         print(int(self.click))
        #         self.time_label.configure(text='Время: ' + str(int(self.click)))
        #         time.sleep(1)
            
        #         self.click += 1
        # Thread(target = update(self), args = [1,]).start()
        self.time_label.configure(text= f'Время: {str(int(time.time()) - self.start_time)}' )
        self.root.after(1000, self.autoc)

    def update_tab_num(self):
        if self.next_table:
            self.next_table = 0
            self.table_num += 1
            self.table_num_label.configure(text = f'Таблица {self.table_num}')
            self.root.after(1000, self.update_tab_num)
    
    def table_controller(self):
        self.table_num_label.place(relx=0.5, rely=0.06)
        self.start_time = int(time.time())

        self.table_num_label.configure(text = f'Таблица {self.table_num}')
        self.start_button.place_forget()
        self.autoc()
        self.update_tab_num()
        # while self.table_num != self.number_of_tables:
        #     self.next_table_button.place_forget()
        #     self.table_num+=1
        #     self.show_table


    def show_table(self):
        pass


    def __init__(self, root:Tk, user, num_tables, patient=None):
        self.root = root
        self.User = user
        self.number_of_tables = num_tables
        self.table_num = 1
        self.next_table = 0
        self.time = 0
        self.time_label = ttk.Label(self.root)
        self.table_num_label = ttk.Label(self.root, text = 'Таблица: 0')
        self.start_button = ttk.Button(self.root, text = 'Начать', command=self.table_controller)
        

        
        self.time_label.place(relx=0.05, rely=0.06)
        self.start_button.place(relx=0.5, rely=0.6)