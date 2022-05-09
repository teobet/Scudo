import serial
from time import sleep

def read():
    serialPort = serial.Serial('COM1')

    dati = serialPort.readline()
    dati = dati.decode('ascii')

    arrayDati = dati.split(" ")

    return arrayDati


