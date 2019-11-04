import serial

import time

ser = serial.Serial(

    port='COM4',

    baudrate=9600,

    timeout=1,

    parity=serial.PARITY_ODD,

    stopbits=serial.STOPBITS_TWO,

    bytesize=serial.SEVENBITS

)

ser.isOpen()

# Reading the data from the serial port. This will be running in an infinite loop.



while 1 :

        # get keyboard input

        bytesToRead = ser.inWaiting()

        data = ser.read(bytesToRead)

        time.sleep(1)

        print(data)