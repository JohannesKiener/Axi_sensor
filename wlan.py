
import network
import time



station = network.WLAN(network.STA_IF)

def connect_to_wifi(ssid,pw):
    station.active(True)
    # TODO maybe station.ifconfig((ip_address, subnet_mask, router_ip, router_ip))
    station.connect(ssid, pw)
    print("Connecting to wifi...",end="")
    for i in range (15):
        time.sleep(1)
        print(".",end="")
        if station.isconnected():
            print('WLAN connection successful:')
            print(station.ifconfig())
            return True

    print("Not Connected to Wifi")  
    return False       

