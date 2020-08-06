"""
A monitorozáshoz használatos modellek
"""

from dataclasses import dataclass


@dataclass
class RemoteState:
    """
    A távirányítón egy adott állapot reprezentációjáért felelős modell osztály

    Attributes:
        swtich1: ---
        swtich2:    |______ A kapcsolók állapotai, True, ha az állapot 1, False, ha az állapot 0
        swtich3:    |
        swtich4: ---
        button1: ---______ A gombok állapotai, True, ha az állapot 1, False, ha az állapot 0
        button2: ---
        pot_meter: int -- A potmeter állása
    """
    swtich1: bool
    swtich2: bool
    swtich3: bool
    swtich4: bool
    button1: bool
    button2: bool
    pot_meter: int

    def __init__(self, s1: bool, s2: bool, s3: bool, s4: bool, b1: bool, b2: bool, potMeter: int) -> None:
        self.swtich1 = s1
        self.swtich2 = s2
        self.swtich3 = s3
        self.swtich4 = s4
        self.button1 = b1
        self.button2 = b2
        self.pot_meter = potMeter
