import os
import time
import uuid
import datetime
import json
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep

def control_led(temp):
    if temp < 25:
        #Cold temperatures (Blue)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.OUT)
        GPIO.output(22, True)
        time.sleep(6)
        GPIO.output(22, False)

    elif   temp >= 25 and temp <=30 :
	    #Normal temperatures (Green LED)	
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(27, GPIO.OUT)
        GPIO.output(27, True)
        time.sleep(6)
        GPIO.output(27, False)
    else:
        #Very hot temperatures (Red LED)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.output(17, True)
        time.sleep(6)
        GPIO.output(17, False)

def msg_rcv(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '" + message.topic)
    try:
        data = json.loads(str(message.payload.decode("utf-8", "ignore")))
        print(data)
        temp = data["main"]["temp"]
        control_led(temp)
    except:
        print("A message not intended for me, ignoring...")

def on_log(client, userdata, level, buf):
    print("log: ",buf)

def main_loop():
    # mosquitto_sub -h 82.165.16.151 -t UCC/mark
    client = mqtt.Client("bje_client_"+ str(uuid.UUID.hex))
    client.on_message = msg_rcv
    client.on_log = on_log
    client.connect("82.165.16.151") 
    client.loop_start()
    client.subscribe("UCC/mark")

    while True:
        time.sleep(4)
        print(".")

if __name__ == "__main__":
    main_loop()
