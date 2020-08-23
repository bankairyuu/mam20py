import tkinter as tk
from mam20.monitor.monitor_frame import MainFrame
from mam20.logger import logger

logger.info('================================================================')
logger.info('== Magyarok a Marson 2020 (amPEr) remote controller')
logger.info('==         and advanced monitor application')
logger.info('== -------------------------------------------------------------')
logger.info('==      Be sure, that the application is running')
logger.info('==      with sudo/administration rights, because')
logger.info('==          to detect the serial I/O ports,')
logger.info('==           those rights are necessary!')
logger.info('================================================================')
logger.debug('create root for GUI')
root = tk.Tk()
mainFrame = MainFrame(master=root)
mainFrame.mainloop()
