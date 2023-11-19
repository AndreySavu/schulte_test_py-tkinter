import sqlite3
from tkinter import *
from tkinter import Tk, ttk
from tkinter.messagebox import showerror, showinfo, showwarning

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure

from entities.PatientStatistics import PatientStatistics


class PsychologistStatistics(PatientStatistics):
    def __init__(self, root:Tk, results, user_name=None):
        
        self._results = results
        self._user_name = user_name
        self.root = root

        self.functions = ['дата/среднее время', 'статистика за 5+ таблиц', 'что-то ещё']
        self.make_interface()
    
    def selected(self, event):
        selection = self.combobox.get()
        if selection == 'дата/среднее время':
            self.clean()
            self.date_duration_plot('many')
        elif selection == 'статистика за 5+ таблиц':
            self.clean()
            self.tables_stat()
        elif selection == 'что-то ещё':
            self.clean()
            showinfo(title='info', message='Что-нибудь добавится.')
    
    def date_duration_plot(self, mode):
        res_array = self._results.get_results()
        counter = 1
        fig, ax = plt.subplots()
        fig.set_dpi(100)
        fig.set_figheight(3.5)
        fig.set_figwidth(4.5)

        users = []
        for item in res_array:
            if str(item[7]+' '+item[8][:1]+'.'+item[9][:1]+'.') not in users:
                users.append(str(item[7]+' '+item[8][:1]+'.'+item[9][:1]+'.'))
        
        for user in users:
            date_duration = {}
            for item in res_array:
                if str(item[7]+' '+item[8][:1]+'.'+item[9][:1]+'.') == user:
                    print('tttt')
                    if item[2].split(' ')[0] not in date_duration:
                        date_duration[item[2].split(' ')[0]]= []
                        date_duration[item[2].split(' ')[0]].append(item[6])
                    else:
                        date_duration[item[2].split(' ')[0]].append(item[6])
            for item in date_duration:
                date_duration[item]=sum(date_duration[item])/len(date_duration[item])
            
            date = date_duration.keys()
            duration = date_duration.values()

            ax.plot(date, duration, '-h', linewidth=3, markersize=5, markerfacecolor='b', 
                label=user)
            counter +=1
        
        ax.set_xlabel('Дата', fontsize=8)
        ax.set_ylabel('Время', fontsize=8)
        ax.grid(color='b', linewidth=0.5)
        ax.legend(fontsize=8)
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        self.canvas = canvas.get_tk_widget()
        self.canvas.place(relx=0.5, rely=0.55, anchor=CENTER)
        