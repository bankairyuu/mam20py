import glob
import serial
import sys
from mam20.logger import logger

arduino: serial.Serial


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


def read_serial() -> str:
    package = str(arduino.readline())
    logger.debug(package)
    return package


def write_serial(msg: str):
    arduino.write(str)
