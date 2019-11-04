import serial.tools.list_ports

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



if __name__ == '__main__':
    print(serial_ports())