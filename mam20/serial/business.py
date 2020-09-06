import glob
import serial
import sys
from mam20.logger import logger

arduino: serial.Serial


class ArduinoDataPack:
    def __init__(self, package: bytes):
        decoded = str(bin(int.from_bytes(package, byteorder='big')))
        logger.debug(decoded)

        self.b1 = True if decoded[-21] == '0' else False
        self.b2 = True if decoded[-22] == '0' else False
        self.s1 = True if decoded[-20] == '1' else False
        self.s2 = True if decoded[-19] == '1' else False
        self.s3 = True if decoded[-18] == '1' else False
        self.s4 = True if decoded[-17] == '1' else False
        self.pot_meter = int(decoded[-16:], 2)
        logger.debug('switches: ' + str(self.s1) + ' ' + str(self.s2) + ' ' + str(self.s3) + ' ' + str(self.s4))
        logger.debug('buttons : ' + str(self.b1) + ' ' + str(self.b2))
        logger.debug('potmeter: ' + str(self.pot_meter))

        self.header = decoded[2:-24]
        logger.debug('header: ' + self.header)

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
