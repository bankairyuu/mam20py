from tkinter import LabelFrame, Label
from PIL import Image, ImageTk
from pkg_resources import resource_stream


class CameraFrame(LabelFrame):

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.master = master
        self.pack(padx=10, pady=10)
        self.create_widgets()

    def create_widgets(self):
        global img
        img = ImageTk.PhotoImage(Image.open(resource_stream('mam20.resources.images', 'demo.jpg')))
        self.cam = Label(self, image=img)
        self.cam.pack()
