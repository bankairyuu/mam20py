from unittest import TestCase
from mam20.serial.business import available_ports
from mam20.serial.comthread import CommunicationThread


class TestCommunicationThread(TestCase):
    def test_run(self):
        ardu = '/dev/ttyUSB0'
        contains: bool = False
        ports = available_ports()
        if ports is not None:
            for port in ports:
                if port == ardu:
                    contains = True
            if not contains:
                self.fail()
        else:
            self.fail()

        com_thread = CommunicationThread(ardu)
        com_thread.run()
