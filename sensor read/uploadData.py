import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
import time
import adafruit_dht
import board

#Pin 4
dht_device = adafruit_dht.DHT22(board.D4)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("/home/pi/Desktop/firebase/conf.json")
firebase_admin.initialize_app(cred)

# Create Firestore client
db = firestore.client()

def temp_dht():
    try:
        return dht_device.temperature
    except RuntimeError:
        print("couldn't read dht data: check dht connection")
        return None
    except:
        return None

def hum_dht():
    try:
        return dht_device.humidity
    except RuntimeError:
        print("couldn't read dht data: check dht connection")
        return None
    except:
        return None


def generate_data():
        data = {}
        # Generate random values
        data['airHumidity'] = hum_dht()
        data['airTempreture'] =  temp_dht()
        data['epocheTimestamp'] = int(time.time())
        data['soilHumidity'] = None
        data['soilTempreture'] = None
        data['waterLevel'] = None
        print(data)
        return data

while True:
    db.collection('data').add(generate_data())
    time.sleep(5)
