from tkinter import *
from mam20.logger import logger

from mam20.camera.camera_frame import CameraFrame
from mam20.monitor.remote_frame import RemoteFrame


class MonitorFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        logger.debug('Monitor frame - init')
        self.master = master
        self.pack()
        logger.debug('choosing the serial I/O port to use')
        self.ioport = self.connect_serial()
        if self.ioport is None:
            logger.warning('No Serial I/O port is selected!!!')
        else:
            logger.info('Serial I/O port to use is: ' + self.ioport)
        self.create_widgets()

    def create_widgets(self):
        """
        create the used widgets on the Monitor frame
        :return: None
        """
        self.camera = CameraFrame(self, text="Camera module", padx=5, pady=5).grid(row=0, column=0, padx=10, pady=10,
                                                                                   columnspan=2)
        self.remote_status = RemoteFrame(self, text="Remote status", padx=5, pady=5).grid(row=1, column=0, padx=10,
                                                                                          pady=10)
        self.footer = Frame(self)
        self.footer.grid(column=99, row=99)
        self.footer.btnExit = Button(self.footer, text="Exit", command=self.master.destroy).pack(padx=5, pady=5)

    def connect_serial(self) -> str:
        """
        Dialog window for selecting the serial I/O port to use
        If there is no ports to list, you need to check if the application is running in administration mode
        :return: choosen I/O port
        """
        from mam20.monitor.connect_serial_dialog import ConnectSerialDialog
        dialog = ConnectSerialDialog(self)
        return dialog.result
