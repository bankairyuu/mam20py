from tkinter import *
from mam20.camera.camera_frame import CameraFrame
from mam20.monitor.remote_frame import RemoteFrame


class MonitorFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.camera = CameraFrame(self, text="Camera module", padx=5, pady=5).grid(row=0, column=0, padx=10, pady=10,
                                                                                   columnspan=2)
        self.remote_status = RemoteFrame(self, text="Remote status", padx=5, pady=5).grid(row=1, column=0, padx=10,
                                                                                          pady=10)
        self.footer=Frame(self)
        self.footer.grid(column=99, row=99)
        self.footer.btnExit = Button(self.footer, text="Exit", command=self.master.destroy).pack(padx=5, pady=5)
