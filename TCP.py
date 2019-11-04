#!/usr/bin/python3

import serial
import time
import binascii

#for windows
ser = serial.Serial("COM3",115200)
#for linux
#ser = serial.Serial("ttyUSB0",115200)
ser.flushInput()

rec_buff = ''


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
    if True == send_at('AT+CSOC=1,1,1','OK',1):
        print('Created TCP socket id 0 Successfully!')
        send_at('AT+CSOCON=0,9999,\"130.237.5.169\"','',2)
        send_at('AT+CSOSEND=0,0,\"Send to Socket id 0 using TCP\"','OK',2)
        try:
            while True:
                if ser.inWaiting():
                    rec_buff = ser.read(ser.inWaiting())
                    print(binascii.a2b_hex(rec_buff.decode().split(",")[2].strip()).decode("utf8"))
                ser.flushInput()
                time.sleep(0.5)
        except:  
        # except Exception as e:
        #     print(e)
            send_at('AT+CSOCL=0','OK',1)
            send_at('AT+CSOCON?','OK',1)
    print('Close Socket')
except:
	if ser != None:
		ser.close()