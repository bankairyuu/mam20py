from threading import Thread

import serial

from mam20.logger import logger
from mam20.serial.business import read_serial, write_serial, set_serial, is_open


class CommunicationThread(Thread):

    def __init__(self, serial_io_port: str) -> None:
        Thread.__init__(self)
        set_serial(serial_io_port)

    def run(self):
        logger.info('Communication thread started')
        while is_open():
            input = read_serial()
