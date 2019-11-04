# encoding: utf-8

import paho.mqtt.client as mqtt

HOST = "130.229.144.15"
PORT = 1883
Topic = "test"

def test():
    client = mqtt.Client()
    client.connect(HOST, PORT, 60)
    client.loop_start()
    client.publish(Topic,"hello MQTT",2)
    client.loop_stop()

if __name__ == '__main__':
    test()