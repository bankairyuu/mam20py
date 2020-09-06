import glob
import serial
import sys
from mam20.logger import logger
from mam20.monitor.model.model import lcd_queue

arduino: serial.Serial


class ArduinoOutputDataPack:
    def __init__(self, header, body):
        self.header = header
        self.body = body

    def to_bytes(self) -> bytes:
        pass


class RemoteData:
    """

    """

    def __init__(self, decoded: str):
        self.b1 = True if decoded[3] == '0' else False
        self.b2 = True if decoded[2] == '0' else False
        self.s1 = True if decoded[4] == '1' else False
        self.s2 = True if decoded[5] == '1' else False
        self.s3 = True if decoded[6] == '1' else False
        self.s4 = True if decoded[7] == '1' else False
        self.pot_meter = int(decoded[8:], 2)
        logger.debug('switches: ' + str(self.s1) + ' ' + str(self.s2) + ' ' + str(self.s3) + ' ' + str(self.s4))
        logger.debug('buttons : ' + str(self.b1) + ' ' + str(self.b2))
        logger.debug('potmeter: ' + str(self.pot_meter))


class StatusData:
    def __init__(self, decoded: str):
        pass


class ControlData(ArduinoOutputDataPack):
    """
    Data package Body for move the servos and steppers
    <servo>     7byte
    <mot-param> 1byte
    <steppers>  8byte
    """

    def __init__(self):
        super().__init__(0x03, self)
        self.servo = None
        self.mot_param = None
        self.steppers = None

    def calc_servo(self):
        pass

    def calc_mot_param(self):
        pass

    def calc_steppers(self):
        pass

    def to_bytes(self):
        pass


class ArduinoInputDataPack:
    def __init__(self, package: bytes):
        header_split = str(bin(int.from_bytes(package, byteorder='little')))[-8:]
        self.header = int(header_split, 2)
        logger.debug('header: ' + str(self.header))
        # ha 1, akkor x. indextől, ha nem, akkor meg "többedik" LoL kekw
        decoded = str(bin(int.from_bytes(package, byteorder='big')))
        logger.debug(decoded)

        self.remote_data: RemoteData = None
        self.status_data: StatusData = None

        if self.header == 1:
            self.remote_data = RemoteData(decoded=decoded[-24:])
        elif self.header == 2:
            self.status_data = StatusData(decoded=decoded[-25:])


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


def read_serial() -> ArduinoInputDataPack:
    return ArduinoInputDataPack(arduino.read(size=4))


def write_serial(msg: str):
    arduino.write(str)


def calculate_output(input: ArduinoInputDataPack) -> bytes:
    """
    It starts the calculations for the actual ArduinoInputDataPack input, and creates an ArduinoOutputDataPack output
    package. After that, the to_bytes() function creates the needed bytes that is needed to the serial-write
    :param input: Actual ArduinoInputDataPack input to handle
    :return: ArduinoOutputDataPack.to_bytes()
    """
    # TODO: átadni a felületnek a bemenetet, hogy az megjelenítse (1 -> remote, 2-> status)

    # TODO: kimenet létrehozása alapból ControlData, de ha egy tárolóban van az LCD-re írásos adat akkor azt küldi ki
    if lcd_queue.is_waiting():
        # TODO: LCD-re írásra adatosztály felső és alsó sorral + amíg van oda való adat, mindet kiolvasni és küldeni
        pass
    else:
        control_data = ControlData()  # TODO: egy getter valahonnan, vagy factory célravezetőbb és szebb is lenne, ahol a megfelelő adat a megfelelő bemenethez kiolvasásra kerül

    # TODO: kimenet byte kóddá konvertálása és visszatérés
    return control_data.to_bytes()
