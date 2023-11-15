
import sqlite3
from tkinter import *
from tkinter import Tk, ttk
from tkinter.messagebox import showerror, showinfo, showwarning

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure


class UserStatistics():
    def __init__(self, root:Tk, results, user_name):
        
        self._results = results
        self._user_name = user_name
        self.root = root

        self.functions = ['дата/среднее время', 'дата/среднее время(с другими польз-ми)', 'статистика за 5+ таблиц', 'что-то ещё']
        self.make_interface()
    
    def make_interface(self):
        self.combobox = ttk.Combobox(self.root, values=self.functions, state="readonly", width=50)
        self.combobox.place(relx=0.4, y=15, anchor=CENTER)
        self.do_button = ttk.Button(self.root, text='Сделать', command=self.make_stat)
        self.do_button.place(relx=0.9, y=15, anchor=CENTER)
        
        self.combobox.bind("<<ComboboxSelected>>", self.selected)

        self.label_about = ttk.Label(self.root)


    def make_stat(self):
        res_array = self._results.get_results()
        selected_res = self._results.get_selected_results()
        selected_res_array = []

        if selected_res[4] not in [1,2,3,4,5,6,7,8,9,10]:
            showwarning(title='warning',message='Выберите таблицу с индексом не 0')
            return

        for item in res_array:
            if selected_res[6][:-1] == item[2].split(' ')[1][:-1]:#проверяем совпадает ли время сохранения, с точностью до 10 секунд
                selected_res_array.append((item[3], item[6]))#номер таблицы + время прохождения

        if len(selected_res_array)<5:
            showwarning(title='warning',message='Выборка меньше 5-ти таблиц')
            return
        self.lbl0.place_forget()
        efficiency = 0
        for i in selected_res_array:
            efficiency+=i[1]
        efficiency/=len(selected_res_array)
        self.lbl1.config(text=f'Количество таблиц = {len(selected_res_array)}' )
        self.lbl2.config(text=f'Эффективность работы = {efficiency}')
        self.lbl3.config(text=f'Степень врабатываемости = {selected_res_array[0][1]/efficiency}')
        #предпоследний элемент массива/эффективность
        self.lbl4.config(text=f'Психическая устойчивость = {selected_res_array[len(selected_res_array)-2][1]/efficiency}')
    
    def date_duration_plot(self, mode):
        res_array = self._results.get_results()
        counter = 1
        #fig = Figure(figsize=(4.5, 3.5), dpi=100)
        fig, ax = plt.subplots()
        if mode == 'one':
            users=[self._user_name]
        else:
            users = []
            for item in res_array:
                if item[8] not in users:
                    users.append(item[8])
        print(users)
            
        for user in users:
            date_duration = {}
            for item in res_array:
                if item[8] == user:
                    if item[2].split(' ')[0] not in date_duration:
                        date_duration[item[2].split(' ')[0]]= []
                        date_duration[item[2].split(' ')[0]].append(item[6])
                    else:
                        date_duration[item[2].split(' ')[0]].append(item[6])
            print(date_duration)
            for item in date_duration:
                date_duration[item]=sum(date_duration[item])/len(date_duration[item])
            
            
            date = date_duration.keys()
            duration = date_duration.values()
            
            # ax = fig.add_subplot(1, len(users), counter)
            # ax.plot(date, duration, '-rh', linewidth=3, markersize=5, markerfacecolor='b', 
            #     label=user)
            # ax.grid(color='b', linewidth=0.5)
            # ax.legend(fontsize=8)
            plt.plot(date, duration, label=user)

            counter +=1
        
        plt.legend()
        plt.ylabel('Время', fontsize= 8 )
        plt.xlabel('Дата', fontsize= 8 )

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        self.canvas = canvas.get_tk_widget()
        self.canvas.place(relx=0.5, rely=0.55, anchor=CENTER)

        # toolbar = NavigationToolbar2Tk(canvas, root)
        # toolbar.update()
        # canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    def selected(self, event):
        selection = self.combobox.get()
        if selection == 'дата/среднее время':
            self.clean()
            self.date_duration_plot('one')
        elif selection == 'дата/среднее время(с другими польз-ми)':
            self.clean()
            self.date_duration_plot('many')
        elif selection == 'статистика за 5+ таблиц':
            self.clean()
            self.tables_stat()
        elif selection == 'что-то ещё':
            self.clean()
            showinfo(title='info', message='Что-нибудь добавится.')


    def tables_stat(self):
        self.label_about.config(text='Расчет показателей внимания')
        self.lbl0 = ttk.Label(self.root)
        self.lbl1 = ttk.Label(self.root)
        self.lbl2 = ttk.Label(self.root)
        self.lbl3 = ttk.Label(self.root)
        self.lbl4 = ttk.Label(self.root)
        
        self.lbl0.config(text='Нажмите на любую таблицу c номером 1-10 из серии 5 и более тестов слева..')

        self.label_about.place(relx=0.5, y=50, anchor=CENTER)
        self.lbl0.place(relx=0.1, y=70, anchor=W)
        self.lbl1.place(relx=0.1, y=90, anchor=W)
        self.lbl2.place(relx=0.1, y=110, anchor=W)
        self.lbl3.place(relx=0.1, y=130, anchor=W)
        self.lbl4.place(relx=0.1, y=150, anchor=W)
        
    def clean(self):
        try:
            self.lbl1.place_forget()
            self.lbl2.place_forget()
            self.lbl3.place_forget()
            self.lbl4.place_forget()
            self.lbl0.place_forget()
        except: pass
        try:
            self.canvas.place_forget()
        except: pass
        

