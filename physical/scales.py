# -*- coding: utf-8 -*-
import serial

from contextlib import contextmanager
from decimal import Decimal
from time import sleep


TERMINATOR = chr(0x0A)  # \n
SEPERATOR = chr(0x0D)   # \r

MOCK_DEVICE = '/dev/mock'


class TimeoutError(RuntimeError):
    pass


@contextmanager
def connection(device="/dev/ttyUSB0"):
    conn = None
    try:
        if device == MOCK_DEVICE:
            conn = MockConnection()
        else:
            conn = serial.Serial(device, timeout=1)
        yield conn
    finally:
        if conn:
            conn.close()


class MockConnection(object):

    record = "0015.203\r4000.000\r\n"  # 15.203Kg, Tare = 0

    def __init__(self):
        self.pos = 0
        self.closed = False

    def read(self, num):
        if self.closed:
            raise serial.SerialException(
                'Attempting to use a port that is not open'
            )
        chars = ""
        for _ in range(num):
            if self.pos >= len(self.record):
                self.pos = 0
            chars = chars + self.record[self.pos]
            self.pos += 1
        return chars

    def close(self):
        self.closed = True


def read_record(conn):
    s = ""
    has_terminator = False
    while True:
        c = conn.read(1)
        if c == "":
            # Timed out
            raise TimeoutError()
        elif c == TERMINATOR:
            if has_terminator:
                has_terminator = False
                return s.strip().split(SEPERATOR)
            else:
                has_terminator = True
                s = ""

        else:
            s = s + c


def get_weight(device="/dev/ttyUSB0"):
    for i in range(5):
        with connection(device=device) as conn:
            try:
                record = read_record(conn)
            except TimeoutError:
                record = None
        if record:
            return Decimal(record[0].strip("0"))
        sleep(0.2 * i)  # geometric incremental back-off
    return None
