#!/usr/bin/python3
import serial
import time
import serial.tools.list_ports

ServerIP = '85.228.22.65'
Port = '10000'
Protocol = 'UDP'
Mode = 'PSM'
TimeInterval = 10
# message length--bytes, no larger than 512bytes
Message_len = 16
Message = "a"*Message_len
# s='Send to Socket id 0 using TCP'
# len(s.encode('utf-8'))


# function used to automatically find the port
def serial_ports():
    # produce a list of all serial ports. The list contains a tuple with the port number, 
    # description and hardware address
    ports = list(serial.tools.list_ports.comports())  
    # return the port if 'USB' is in the description 
    # result = []
    for port_no, description, address in ports:
        if 'USB' in description:
            # result.append(port_no)
            return port_no
    # return result
ser = serial.Serial(serial_ports(),115200)
ser.flushInput()
# function for interaction with terminal
def send_at(command,back,timeout):
    rec_buff = ''
    ser.write((command+'\r\n').encode())
    time.sleep(timeout)
    if ser.inWaiting():
        time.sleep(0.1)
        rec_buff = ser.read(ser.inWaiting())
    if rec_buff != '':
        if back not in rec_buff.decode():
            print(command + ' ERROR\t')
            print(command + ' back:\t' + rec_buff.decode())
            return 0
        else:
            print(rec_buff.decode())
            return 1
    else:
        print(command + ' no responce')
        return 0
# set APN 
if True == send_at('AT+csgact=1,1,\"lpwa.telia.iot\"','OK',1):
    print('Set APN Successfully')
else:
    print('ERROR since APN already set')

def PSM():
    # network registration for PSM
    send_at('at+cereg=4','OK',1)
    # network registration check
    send_at('at+cereg?','OK',1)
    # Enable the use of PSM
    send_at('at+cpsms?','OK',1)

def UDP():
    if True == send_at('AT+CSOC=1,2,1','+CSOC:',1):
        print('Created UDP socket id Successfully!')
        send_at('AT+CSOCON=0,'+Port+',\"'+ServerIP+'\"','',1)
        send_at('AT+CSOSEND=0,0,''\"'+Message+'\"','',1)
        send_at('AT+CSOCL=0','OK',1)
        send_at('AT+CSOCON?','OK',1)
    print('Close Socket')

def TCP():
    if True == send_at('AT+CSOC=1,1,1','OK',1):
        print('Created TCP socket id 0 Successfully!')
        send_at('AT+CSOCON=0,'+Port+',\"'+ServerIP+'\"','',2)
        send_at('AT+CSOSEND=0,0,''\"'+Message+'\"','',2)
        # try:
        #     while True:
        #         if ser.inWaiting():
        #             rec_buff = ser.read(ser.inWaiting())
        #             print(binascii.a2b_hex(rec_buff.decode().split(",")[2].strip()).decode("utf8"))
        #         ser.flushInput()
        #         time.sleep(0.5)
        # except:  
        # except Exception as e:
        #     print(e)
        send_at('AT+CSOCL=0','OK',1)
        send_at('AT+CSOCON?','OK',1)
    print('Close Socket')
# def close_Socket():
    


if __name__ == '__main__':
    try:
        if(Mode == 'PSM'):
            PSM()
        while True:
            if(Protocol == 'UDP'):
                UDP()
            elif(Protocol == 'TCP'):
                TCP()
            time.sleep(TimeInterval)
    except:
        if ser != None:
            ser.close()


# >>> rnd = os.urandom(16)
# >>> rnd
# b'\xf0\xe9ZG3\xf0(\xd2\xc3\x04/\xf1\xae\x0b-\xb4'
# >>> len(rnd)
# 16
# np.random.bytes( X_1MB )