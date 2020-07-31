# import logging
import numpy as np, serial, time

# log = logging.getLogger(__name__)

class Driver():

    error_command = 'SYST:ERR?'
    """The SCPI command to query errors."""

    def __init__(self, addr=None, baudrate=115200, parity='N', bytesize=8, stopbits=1, timeout=3, **kw):
        self.addr = addr
        self.timeout = timeout
        self._baudrate = baudrate
        self._parity = parity
        self._bytesize = bytesize
        self._stopbits = stopbits


    def performOpen(self):

        self.handle=serial.Serial(self.addr,baudrate=self._baudrate,parity=self._parity,bytesize=self._bytesize,\
            stopbits=self._stopbits,timeout=self.timeout)
        if self.handle.isOpen():    # make sure port is open     
            print(self.handle.name + ' open...')
            # self.handle.write(b'*IDN?\n')
            # x = self.handle.readline().decode().split('\r''\n')
            # print(x[0])
            self.handle.write(b'ATT?\n')
            y = self.handle.readline().decode().split('\r''\n')
            print('last ATT',y[0])


    def set_att(self,att):
        self.handle.write(b'ATT %f\n'%att)
        time.sleep(1)
    

    def query_att(self):
        self.handle.write(b'ATT?\n')
        y = self.handle.readline().decode().split('\r''\n')
        return y[0]


    def close(self):
        try:
            self.handle.close()
        except:
            pass
