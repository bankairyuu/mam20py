import glob
import serial
import sys
from mam20.logger import logger

arduino: serial.Serial


class ArduinoDataPack:
    def __init__(self, package: bytes):
        decoded = str(bin(int.from_bytes(package, byteorder=sys.byteorder)))
        logger.debug(decoded)

        self.s1 = 0
        self.s2 = 0
        self.s3 = 0
        self.s4 = 0
        self.b1 = 0
        self.b2 = 0
        self.pot_meter = 128

    def to_bytes(self):
        pass


def available_ports():
    """
    Lists serial port names
    :raises EnvironmentError:
            On unsupported or unknown platforms
    :returns:
        A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        logger.debug('Windows detected')
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        logger.debug('Linux / cygwin detected')
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        logger.debug('darwin detected')
        ports = glob.glob('/dev/tty.*')
    else:
        logger.error('Unsupported platform detected')
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def set_serial(port: str):
    global arduino
    arduino = serial.Serial(port, baudrate=57600, timeout=100)
    arduino.flush()


def is_open() -> bool:
    return arduino.is_open


def read_serial() -> ArduinoDataPack:
    return ArduinoDataPack(arduino.read(size=4))


def write_serial(msg: str):
    arduino.write(str)
