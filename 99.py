import time
from tkinter import Button, Label, Tk, mainloop


class App(Tk):
    def __init__(self):
        super().__init__()

        self.label = Label(self, text="")
        self.label.pack()
        self.butt = Button(self, text ='butt')
        self.butt.pack()
        self.start = int(time.time())
        self.update_clock()

    def update_clock(self):
        now = int(time.time())
        self.label.configure(text=now-self.start)
        self.after(1000, self.update_clock)
    


def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()