import firebase_admin
from firebase_admin import credentials, db
import logging
from door import door
import time
import RPi.GPIO as GPIO

logging.basicConfig(level=logging.ERROR)

try:

    cred = credentials.Certificate("/home/pi/Desktop/firebase/conf.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://sghproject-d4503-default-rtdb.firebaseio.com/'
    })

    door1 = door(17,90,180)

    relayPin = 24

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relayPin, GPIO.OUT)
    GPIO.output(relayPin, GPIO.LOW)

    pumpUpDuration = 5000 #5 seconds
    pumpStartTime = 0
    pump_status = False

    # Define callback functions for each data field
    def handle_door_open_change(event):
        door_open = event.data
        print("door status changed:", door_open)
        if(door_open):
            door1.openDoor()
        else:
            door1.closeDoor()

    def handle_pump_change(event):
        global pumpStartTime,pump_status

        pump_status = event.data
        if pump_status:
            print("start pump")
            pumpStartTime = time.time()
            GPIO.output(relayPin, GPIO.HIGH)
            print("pump start time changed ", pumpStartTime)
        else:
            print("close pump")
            GPIO.output(relayPin, GPIO.LOW)

    def handle_pump_duration_change(event):
        global pumpUpDuration

        pumpUpDuration = int(event.data)
        print("pump_duration status changed:", pumpUpDuration)

    # Get references to the specific data fields
    door_ref = db.reference('/devices/doorOpen')
    pump_ref = db.reference('/devices/pumpOn')
    pump_duration_ref = db.reference('/devices/pumpUpDuration')

    door_ref.listen(handle_door_open_change)
    pump_ref.listen(handle_pump_change)
    pump_duration_ref.listen(handle_pump_duration_change)

    while True:
        if ((time.time() - pumpStartTime >=(pumpUpDuration/1000)) and (pump_status)):
            print("pump duration ended")
            pump_status = False
            pump_ref.set(False)
            GPIO.output(relayPin, GPIO.LOW)

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

except Exception as e:
    logging.error("An error occurred:", exc_info=True)

