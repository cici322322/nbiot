# encoding: utf-8

import paho.mqtt.client as mqtt

HOST = "130.229.144.15"
PORT = 1883
Topic = "test"

def return_resultcode(rc):
    return{
        0 : " Connection accepted",
        1 : " Connection refused, unacceptable protocol version",
        2 : " Connection refused, identifier rejected",
        3 : " Connection refused, server unavailable",
        4 : " Connection refused, bad user name or password",
        5 : " Connection refused, not authorized"
    }.get(rc,9)

def MQTT_connect(client, userdata, flags, rc):
    print("Connected with result code :"+return_resultcode(rc))
    client.subscribe(Topic)
    print("Topic : "+Topic)

def MQTT_message(client, userdata, msg):
    print(msg.topic+":" + str(msg.payload))

client = mqtt.Client()
client.on_connect = MQTT_connect
client.on_message = MQTT_message
client.connect(HOST, PORT, 60)
client.loop_forever()