import random
import time
from tkinter import *
from tkinter import Tk, ttk

from entities.Patient import Patient
from entities.Table import Table
from entities.TestResult import TestResult
from entities.User import User


class TestWindow:
    def __init__(self, root:Tk, user:User=None, patient:Patient=None):
        self.root = root
        self._user = user
        self._patient = patient
        self.number_of_tables = None#количество таблиц
        self.dim = None#размерность таблицы
        self.current_table = 1#начинаем с первой таблицы
        
        self.elems = []#для хванения номеров текущей таблицы
        '''тут храним список (список номеров, время прохождения) для каждой таблицы.
        потом из количества номеров считаем сколько было ошибок в каждой таблице'''
        self.array_elems_times = []
        self.table_num = [1]#очевидный костыль, чтобы из table.py увеличивать current_table

        self.init_interface()
        self.place_interface()
    
    def init_interface(self):
        #labels and buttons

        if self._patient:
            self.user_lbl = ttk.Label(self.root, text = 'Пациент: '+ str(self._patient.get_surname_n_initials()))
            self.user_lbl.place(relx=0.1,rely=0.1)
        elif self._user:
            self.user_lbl = ttk.Label(self.root, text = 'Пользователь: '+ str(self._user.get_name()))
            self.user_lbl.place(relx=0.1,rely=0.1)
        
        self.time_label = ttk.Label(self.root)
        self.table_num_label = ttk.Label(self.root, text = 'Таблица: 0')
        self.start_button = ttk.Button(self.root, text = 'Начать', command=self.start)
        self.instruction_button = ttk.Button(self.root, text = 'Инструкция', command=self.show_instruction)
        self.back_button = ttk.Button(self.root, text = 'Назад', command=self.go_back)

        #selectors
        self.select_number = ttk.Label(self.root, text = 'Выберите количество таблиц')
        self.select_dimension = ttk.Label(self.root, text = 'Выберите размерность таблиц')
        self.spinbox_var1 = StringVar(value=1)
        self.spinbox_var2 = StringVar(value=5)
        self.spinbox1 = ttk.Spinbox(self.root, from_=1, to=10, increment=1, textvariable=self.spinbox_var1)
        self.spinbox2 = ttk.Spinbox(self.root, from_=3, to=7, increment=1, textvariable=self.spinbox_var2)
    
    def place_interface(self):
        
        self.time_label.place(relx=0.05, rely=0.06)
        self.start_button.place(relx=0.5, rely=0.6)
        self.instruction_button.place(relx=0.8, rely=0.07)
        self.back_button.place(relx=0.1, rely=0.07)

        self.select_number.place(relx=0.2,rely=0.4)
        self.select_dimension.place(relx=0.7,rely=0.4)
        self.spinbox1.place(relx=0.2,rely=0.45)
        self.spinbox2.place(relx=0.7,rely=0.45)

    def destroy_selectrors(self):
        self.select_number.place_forget()
        self.spinbox1.place_forget()
        self.select_dimension.place_forget()
        self.spinbox2.place_forget()

    def end_interface(self):
        self.save_button = ttk.Button(text='Сохранить', command=self.save_to_db)
        self.WOsave_button = ttk.Button(text='Не сохранять', command=self.go_back)
        self.enabled = IntVar()
        self.enabled_checkbutton = ttk.Checkbutton(text="Видимость результата для всех", variable=self.enabled)
        if self._patient==None:
            self.enabled_checkbutton.place(relx=0.4, rely=0.85)

        self.save_button.place(relx=0.4, rely=0.8)
        self.WOsave_button.place(relx=0.6, rely=0.8)

    def save_to_db(self):
        if self._patient:
            self.result.save_to_db(self._patient.get_id(),1)
        else:
            self.result.save_to_db(self._user.get_name(),0, self.enabled.get())

    def clean(self):
        self.destroy_selectrors()
        
        if self._user or self._patient:
            self.user_lbl.place_forget()
        self.time_label.place_forget()
        self.table_num_label.place_forget()
        self.instruction_button.place_forget()
        self.start_button.place_forget()
        self.back_button.place_forget()

    def go_back(self):
        from frames.PsychologistMenuWindow import PsychologistMenuWindow
        from frames.StartWindow import StartWindow
        from frames.UserMenuWindow import UserMenuWindow
        self.clean()
        try:
            self.tab.frame.place_forget()
        except:
            pass
        try:
            self.tree.place_forget()
            self.result_label.place_forget()
            self.save_button.place_forget()
            self.WOsave_button.place_forget()
            self.enabled_checkbutton.place_forget()
        except:
            pass
       

        if self._user==None:#if guest
            win = StartWindow(self.root)
        elif self._user.get_type() == 0:#user
            win = UserMenuWindow(self.root, self._user)
            
        else:#psychologist
            win = PsychologistMenuWindow(self.root, self._user)

    def autoc(self):
        self.time_label.configure(text= f'Время: {str(int(time.time()) - self.start_time)}' )
        self.root.after(1000, self.autoc)

    def table_controller(self):
        #print(self.spinbox_var1.get(), self.spinbox_var2.get())
        if self.table_num[-1]>self.number_of_tables:
            self.array_elems_times.append((self.elems, int(time.time()) - self.start_time))
            
            self.clean()
            self.raw_result()
            if self._user or self._patient:
                self.end_interface()
            else:
                self.back_button.place(relx=0.1, rely=0.07)

            #ТУТ ДОБАВИТЬ ГАЛОЧКУ ВИДИМОСТЬ ДЛЯ ВСЕХ и делать сохранение в бд по нажатию кнопки

            return#конец
        
        if self.current_table != self.table_num[-1] :
            self.current_table=self.table_num[-1]
            self.table_num_label.configure(text = f'Таблица {self.table_num[-1]}')
            self.array_elems_times.append((self.elems, int(time.time()) - self.start_time))

            self.elems = []#очищаем массив для результата
            self.start_time = int(time.time())#обнуляем счетчик
            self.show_table()#выводим новую таблицу
            
            
        self.root.after(1000, self.table_controller)

    def start(self):
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
        self.result = TestResult(self.array_elems_times, self.dim)
        self.res = self.result.get_mistakes_num_of_mistakes_time()
        self.make_treeview_for_results()

        for i in range(len(self.res)):
            self.tree.insert("", END, values=(i+1,self.res[i][0],self.res[i][1],self.res[i][2]))

    def show_instruction(self):
        frame = Tk()
        frame.geometry('300x200')
        frame.title('Инструкция')
        text = Text(frame, height = 12, width = 52)
        text.pack()
        with open('entities/instruction.txt', 'r') as reader:
            text.insert(END, reader.read())
        frame.mainloop()
    