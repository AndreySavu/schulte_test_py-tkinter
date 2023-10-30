import time
from tkinter import *
from tkinter import Tk, ttk


class Table():
    def create_buttons(self):
        self.buttons = []
        for x in range (self.dim**2):
            self.buttons.append(ttk.Button(self.frame, 
                                           #command=lambda: self.onClick(x)
                                           ))
                         
            

        for c in range(self.dim): self.frame.columnconfigure(index=c, weight=1)
        for r in range(self.dim): self.frame.rowconfigure(index=r, weight=1)
 
        for i in range (self.dim):
            for j in range(self.dim):
                self.buttons[(i)*self.dim + j].bind('<Button-1>', lambda ee, e =(i)*self.dim + j : self.onClick(e))
                self.buttons[(i)*self.dim + j].grid(row=i, column=j, sticky=NSEW)
                self.buttons[(i)*self.dim + j].configure(text = str(i+1)+str(j+1))
                

                

    def onClick(self, btn):
        self.aaa.append(btn)
        print(self.aaa)
                
    
    def place_buttons(self):
        pass
    def __init__(self, root, dimension, aaa):
        
        self.aaa=aaa
        self.root = root
        self.dim = dimension
        
        self.frame = ttk.Frame(self.root, borderwidth=1, relief=SOLID, padding=[1, 1])
        self.frame.place(relx=0.5,rely=0.5, width=self.root.winfo_width()/3, height= self.root.winfo_width()/3, anchor=CENTER)
        self.create_buttons()
        
