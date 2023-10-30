import time
from tkinter import *
from tkinter import Tk, ttk

from Table import Table


class TestWindow():
    def autoc(self):
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
        self.show_table()
        self.autoc()
        self.update_tab_num()


    def show_table(self):
        tab = Table(self.root,5, self.ass)


    def __init__(self):
                    #объект Tkinter------
        self.root = Tk()
        self.root.geometry('1024x600')
        self.root.title("Тестирование Шульте")
        
        self.ass = []
        #self.number_of_tables = 0
        self.table_num = 1
        self.next_table = 0
        self.time = 0
        self.time_label = ttk.Label(self.root)
        self.table_num_label = ttk.Label(self.root, text = 'Таблица: 0')
        self.start_button = ttk.Button(self.root, text = 'Начать', command=self.table_controller)
        
        
        self.time_label.place(relx=0.05, rely=0.06)
        self.start_button.place(relx=0.5, rely=0.6)
        
        self.root.mainloop()
        time.sleep(3)
        print('-----',self.ass)

app = TestWindow()