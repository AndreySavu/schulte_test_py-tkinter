from tkinter import *
from tkinter import Tk, ttk

from entities.PatientResults import PatientResults
from entities.PatientStatistics import PatientStatistics
from entities.PsychologistResults import PsychologistResults
#from entities.PsychologistStatistics import PsychologistStatistics
from entities.UserResults import UserResults
from entities.UserStatistics import UserStatistics


class ResultWindow():

    def __init__(self, root, user=None, patient=None):
        self.root = root
        self._user = user
        self._patient = patient
        self.init_interface()
        self.place_interface()

    
    def init_interface(self):
        self.root.update()
        self.results_label = ttk.Label(self.root, text='Результаты')
        self.stats_label = ttk.Label(self.root, text='Статистика')
        self.left_frame = ttk.Frame(self.root, borderwidth=1, relief=SOLID, padding=[1, 1], width=self.root.winfo_width()/2.05, height= self.root.winfo_height()*0.7)
        self.right_frame = ttk.Frame(self.root, borderwidth=1, relief=SOLID, padding=[1, 1], width=self.root.winfo_width()/2.05, height= self.root.winfo_height()*0.7)

        self.back_button = ttk.Button(self.root,text='Назад',command=self.go_back)

        if self._patient == 0:
            self.user_lbl = ttk.Label(self.root, text = 'Психолог: '+ str(self._user.get_name()))
            self.user_lbl.place(relx=0.05,rely=0.05)
            self.results = PsychologistResults(self.left_frame, self._patient)
            self.stats = UserStatistics(self.right_frame, self.results, self._user.get_name())

        elif self._patient:
            self.user_lbl = ttk.Label(self.root, text = 'Пациент: '+ str(self._patient.get_surname_n_initials()))
            self.user_lbl.place(relx=0.05,rely=0.05)
            self.results = PatientResults(self.left_frame, self._patient)
            self.stats = PatientStatistics(self.right_frame, self.results, self._user.get_name())
        
        elif self._user:
            self.user_lbl = ttk.Label(self.root, text = 'Пользователь: '+ str(self._user.get_name()))
            self.user_lbl.place(relx=0.05,rely=0.05)
            self.results = UserResults(self.left_frame, self._user)
            self.stats = UserStatistics(self.right_frame, self.results, self._user.get_name())

    
    def place_interface(self):
        self.back_button.place(relx=0.9, rely=0.05)
        self.results_label.place(relx=0.2,rely=0.12)
        self.stats_label.place(relx=0.7,rely=0.12)

        self.left_frame.place(relx=0.01,rely=0.15, anchor=NW)
        self.right_frame.place(x=self.root.winfo_width()/2+5, rely=0.15, anchor=NW)

    def go_back(self):
        self.back_button.place_forget()
        self.user_lbl.place_forget()
        self.results_label.place_forget()
        self.stats_label.place_forget()
        self.left_frame.place_forget()
        self.right_frame.place_forget()
        
        if self._patient!=None:
            from frames.PsychologistMenuWindow import PsychologistMenuWindow
            win = PsychologistMenuWindow(self.root, self._user)
        else:
            from frames.UserMenuWindow import UserMenuWindow
            win = UserMenuWindow(self.root, self._user)

