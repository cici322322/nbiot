#!/usr/bin/python3

import serial
import time

#for windows
ser = serial.Serial("COM3",115200)
#for linux
#ser = serial.Serial("ttyUSB0",115200)
ser.flushInput()

rec_buff = ''
ServerIP = '85.228.22.65'
Port = '10000'
Message = 'Sending udp data with socket_id'

def send_at(command,back,timeout):
    rec_buff = ''
    ser.write((command+'\r\n').encode())
    time.sleep(timeout)
    if ser.inWaiting():
        time.sleep(0.1 )
        rec_buff = ser.read(ser.inWaiting())
    if rec_buff != '':
        if back not in rec_buff.decode():
            print(command + ' ERROR')
            print(command + ' back:\t' + rec_buff.decode())
            return 0
        else:
            print(rec_buff.decode())
            return 1
    else:
        print(command + ' no responce')
        return 0

try:
    if True == send_at('AT+csgact=1,1,\"lpwa.telia.iot\"','OK',2):
        print('Set APN Successfully')
    if True == send_at('AT+CSOC=1,2,1','+CSOC:',0.5):
        print('Created UDP socket id Successfully!')
        send_at('AT+CSOCON=0,10000,\"130.237.5.243\"','',2)
        send_at('AT+CSOSEND=0,0,\"Send to Socket id 0 using UDP\"','',2)
        # send_at('AT+CSOSEND=0,0,\"Send to Socket id 0 using UDP\"','',2)
        # send_at('AT+CSOSEND=0,0,\"Send to Socket id 0 using UDP\"','',2)
        send_at('AT+CSOCL=0','OK',0.5)
        send_at('AT+CSOCON?','OK',1)
    print('Close Socket')
except:
     if ser != None:
        ser.close()
