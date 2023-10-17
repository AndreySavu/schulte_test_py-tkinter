import sys
import time
from threading import Thread
from tkinter import *
from tkinter import ttk

sys.path.append('./')
from entities.User import User


class TestWindow():
    def autoc(self):
        while True:
            time.sleep(1)
            self.time += 1
            self.time_label.configure(text='Время: ' + str(int(self.time)))
    
    def table_controller(self):
        Thread(target = self.autoc).start()
        while self.table_num != self.number_of_tables:
            self.next_table_button.place_forget()
            self.table_num+=1
            self.show_table


    def show_table(self):
        pass


    def __init__(self, root, user, num_tables, patient=None):
        self.root = root
        self.User = user
        self.number_of_tables = num_tables
        self.table_num = 0
        self.time = 0
        self.time_label = ttk.Label(self.root, text = 'Время: '+ str(self.time))
        
        self.next_table_button = ttk.Button(self.root, text = 'Начать', command=self.table_controller)
        
        self.time_label.place(relx=0.05, rely=0.06)
        self.next_table_button.place(relx=0.5, rely=0.6)