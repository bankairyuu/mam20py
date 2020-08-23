"""
A monitorozáshoz használatos modellek
"""

from dataclasses import dataclass


@dataclass
class RemoteState:
    """
    A távirányítón egy adott állapot reprezentációjáért felelős modell osztály

    Attributes:
        switch1: ---
        switch2:    |______ A kapcsolók állapotai, True, ha az állapot 1, False, ha az állapot 0
        switch3:    |
        switch4: ---
        button1: ---______ A gombok állapotai, True, ha az állapot 1, False, ha az állapot 0
        button2: ---
        pot_meter: int -- A potmeter állása
    """
    switch1: bool
    switch2: bool
    switch3: bool
    switch4: bool
    button1: bool
    button2: bool
    pot_meter: int

    def __init__(self, s1: bool, s2: bool, s3: bool, s4: bool, b1: bool, b2: bool, pot_meter: int) -> None:
        self.switch1 = s1
        self.switch2 = s2
        self.switch3 = s3
        self.switch4 = s4
        self.button1 = b1
        self.button2 = b2
        self.pot_meter = pot_meter
