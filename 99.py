from tkinter import *
from tkinter import Tk, ttk


class ResultWindow():
    def delete_this(self):
        self.root = Tk()
        self.root.geometry('1024x600')
        self.root.title("Тестирование Шульте")

        
    
    def __init__(self, root=None, user=None):
        self.delete_this()
        self.init_interface()
        self.place_interface()
        
        self.root.mainloop()
    
    def init_interface(self):
        self.root.update()
        self.results_label = ttk.Label(self.root, text='Результаты')
        self.stats_label = ttk.Label(self.root, text='Статистика')
        self.left_frame = ttk.Frame(self.root, borderwidth=1, relief=SOLID, padding=[1, 1], width=self.root.winfo_width()/2.05, height= self.root.winfo_height()*0.7)
        self.right_frame = ttk.Frame(self.root, borderwidth=1, relief=SOLID, padding=[1, 1], width=self.root.winfo_width()/2.05, height= self.root.winfo_height()*0.7)

    
    def place_interface(self):

        self.results_label.place(relx=0.2,rely=0.12)
        self.stats_label.place(relx=0.7,rely=0.12)

        self.left_frame.place(relx=0.01,rely=0.15, anchor=NW)
        self.right_frame.place(x=self.root.winfo_width()/2+5, rely=0.15, anchor=NW)

win = ResultWindow()