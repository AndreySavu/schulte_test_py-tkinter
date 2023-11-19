
import sqlite3
from tkinter import *
from tkinter import Tk, ttk
from tkinter.messagebox import showerror, showinfo, showwarning

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure

from entities.PatientStatistics import PatientStatistics


class UserStatistics(PatientStatistics):
    def __init__(self, root:Tk, results, user_name=None):
        
        self._results = results
        self._user_name = user_name
        self.root = root

        self.functions = ['дата/среднее время', 'дата/среднее время(с другими польз-ми)', 'статистика за 5+ таблиц', 'что-то ещё']
        self.make_interface()
    def date_duration_plot(self, mode):
        res_array = self._results.get_results()
        print(self._results.get_results())
        counter = 1
        fig, ax = plt.subplots()
        fig.set_dpi(100)
        fig.set_figheight(3.5)
        fig.set_figwidth(4.5)
        if mode == 'one':
            users=[self._user_name]
        else:
            users = []
            for item in res_array:
                if item[8] not in users:
                    users.append(item[8])

        for user in users:
            date_duration = {}
            for item in res_array:
                if item[8] == user:
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

