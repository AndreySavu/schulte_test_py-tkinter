import random
import time
from tkinter import *
from tkinter import Tk, ttk


class Table():
    def __init__(self, root:Tk, dimension:int, e, end):
        self.current_number = 0
        self.end = end
        self.elems=e
        self.root = root
        self.dim = dimension
        self.some_button_clicked = 0

        self.make_center_frame()
        self.numbers = self.make_sequence()
        self.create_buttons()
        self.makes_buttons_white()
    
    def create_buttons(self):
        self.buttons = []
        for x in range (self.dim**2):
            self.buttons.append(Button(self.frame, font=('Arial',19-self.dim)))

        for c in range(self.dim): self.frame.columnconfigure(index=c, weight=1)
        for r in range(self.dim): self.frame.rowconfigure(index=r, weight=1)
 
        for i in range (self.dim):
            for j in range(self.dim):
                self.buttons[(i)*self.dim + j].bind('<Button-1>', lambda ee,
                                                    e =((i)*self.dim + j,self.numbers[(i)*self.dim + j]) : self.onClick(e))
                self.buttons[(i)*self.dim + j].grid(row=i, column=j, sticky=NSEW)
                self.buttons[(i)*self.dim + j].configure(text = str(self.numbers[(i)*self.dim + j]), bg='white')

    def makes_buttons_white(self):
        if self.some_button_clicked:
            self.some_button_clicked=0
            #time.sleep(300)
            for btn in self.buttons:
                btn.configure(bg='white')
            
        
        self.root.after(300, self.makes_buttons_white)
    
    def onClick(self, btn):
        self.elems.append(btn[1])
        if btn[1] == self.current_number+1:
            self.current_number+=1
            self.buttons[btn[0]].configure(bg='green')
        else:
            self.buttons[btn[0]].configure(bg='red')
        self.some_button_clicked=1
        if  btn[1] == self.dim**2 and self.current_number==self.dim**2:
            self.end.append(self.end[-1]+1)
            self.some_button_clicked=2#чтобы прервать makes_button_white
            #destroy table
            self.frame.destroy()
            
    def make_sequence(self):
        return random.sample(range(1,self.dim**2+1),self.dim**2)
    
    def make_center_frame(self):
        self.frame = ttk.Frame(self.root, borderwidth=1, relief=SOLID, padding=[1, 1])
        self.frame.place(relx=0.5,rely=0.5, width=self.root.winfo_width()/3, height= self.root.winfo_width()/3, anchor=CENTER)