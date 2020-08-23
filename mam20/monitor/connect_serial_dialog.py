from tkinter import simpledialog, Label, ttk
from mam20.serial.business import available_ports


class ConnectSerialDialog(simpledialog.Dialog):
    """
    Simple dialog for selecting the serial I/O port you want to use
    """
    def body(self, master):
        Label(master, text="Choose the serial I/O port").grid(row=0)
        self.cb = ttk.Combobox(master, values=available_ports())
        self.cb.grid(row=1)
        return self.cb

    def apply(self):
        port = str(self.cb.get())
        self.result = port