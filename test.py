#!/usr/bin/python3
import serial
import time

#for windows
ser = serial.Serial("COM3",115200)
#for linux
#ser = serial.Serial("ttyUSB0",115200)
ser.flushInput()

command_input = ''
rec_buff = ''

try:
    while True:
        command_input = input('Please input the AT command:')
        ser.write((command_input + '\r\n').encode())
        time.sleep(0.1)
        if ser.inWaiting():
            time.sleep(0.01)
            rec_buff = ser.read(ser.inWaiting())
        if rec_buff != '':
            print(rec_buff.decode())
            rec_buff = ''
except:
    if ser != None:
        ser.close()

# import serial.tools.list_ports

# plist = list(serial.tools.list_ports.comports())

# if len(plist) <= 0:
#     print ("The Serial port can't find!")
# else:
#     plist_0 =list(plist[0])
#     serialName = plist_0[0]
#     serialFd = serial.Serial(serialName,9600,timeout = 60)
#     print ("check which port was really used >",serialFd.name)