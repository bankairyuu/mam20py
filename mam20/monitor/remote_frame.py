from tkinter import Checkbutton, LabelFrame, Button


class RemoteFrame(LabelFrame):

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.switch1 = Checkbutton(self, text="Switch1").grid(column = 0, row=0)
        self.switch2 = Checkbutton(self, text="Switch2").grid(column = 1, row=0)
        self.switch3 = Checkbutton(self, text="Switch3").grid(column = 2, row=0)
        self.switch4 = Checkbutton(self, text="Switch4").grid(column = 3, row=0)

        self.btn1 = Checkbutton(self, text="Button1").grid(column = 4, row=0)
        self.btn2 = Checkbutton(self, text="Button2").grid(column = 5, row=0)
