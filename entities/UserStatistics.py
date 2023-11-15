
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
        

