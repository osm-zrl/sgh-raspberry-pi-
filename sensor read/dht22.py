import time
import adafruit_dht
import board

#Pin 4
dht_device = adafruit_dht.DHT22(board.D4)

while True:
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity


        print("Temp:{:.1f} C  Humidity: {}%".format(temperature, humidity))
    except RuntimeError as err:
        print(err.args[0])

    time.sleep(2)
