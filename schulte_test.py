import time
from tkinter import *

from frames.StartWindow import StartWindow


class App:
        def autoc(self):
            self.time_l.configure(text= str(int(time.time()) - self.start_time) )
            self.root.after(1000, self.autoc)

        def __init__(self):
            #объект Tkinter------
            self.root = Tk()
            self.root.geometry('1000x600')
            self.root.title("Тестирование Шульте")
            start = StartWindow(self.root)
            self.root.mainloop()

app = App()