# main.py -- put your code here!
from ds18x20 import DS18X20
from onewire import OneWire
from wlan import connect_to_wifi,station
import ubinascii
from umqtt.simple import MQTTClient

import machine 
from machine import WDT,Pin, Timer
import socket



#TODO Add ssl mqtt here tutorial:
ssid="Vodafone-0A14"
pw="RckFd7eNxnkyPAys"

brocker_ip="axometeronline.online"
user="mali_esp"
pw_mqtt="as2a32fda39dbUHAd"
mqtt_ip_port=1883


messurement_period=1*60 # in s # todo increas wdt rightnow to 5

def get_temp():
    temp.convert_temp()
    return temp.read_temp(rom)

# TODO see if good in handler
def timer_callback(self):
    # TODO add if connected to wifi, else raise error
    temp=get_temp()
    print("Temp:",temp)
    if temp<60:
        client.publish(topic_temp,str(temp))
        #print("published successfully")
    else:
        print("Sensor error, temp not sent")

    wdt.feed()

# connect to wifi
# add timer callback
# TODO upgrade to peter hinches mqtt

wdt = WDT(timeout=6*60*1000)  # 10 min, # this needs to be bigger than "timeout" of the Server
## Setup:
ow = OneWire(Pin(32, Pin.OPEN_DRAIN))
temp = DS18X20(ow)
rom = temp.scan()[0]
connect_to_wifi(ssid, pw)

# -------------MQTT
client_id = ubinascii.hexlify(machine.unique_id())
topic_temp = b'temp'

client = MQTTClient(client_id, brocker_ip,port=mqtt_ip_port, user=user, password=pw_mqtt) 
client.connect()
# send inital State of light to mqtt
#-------------
#TODO add restart if not connected
tim0 = Timer(0)
tim0.init(period=messurement_period*1000, mode=Timer.PERIODIC, callback=timer_callback)

#TODO wdt.feed() only when timer is called
while True:
    #client.check_msg()
    # deepsleep
    # try connecting to wifi
    #wdt.feed()
    pass

