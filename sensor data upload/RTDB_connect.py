import firebase_admin
from firebase_admin import credentials, db
import logging

logging.basicConfig(level=logging.ERROR)

try:
    # Initialize Firebase Admin SDK
    cred = credentials.Certificate("conf.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://sghproject-d4503-default-rtdb.firebaseio.com/'
    })

    # Define callback functions for each data field
    def handle_pump_duration_change(event):
        pump_duration = event.data
        print("pump duration status changed:", pump_duration)

    def handle_pump_change(event):
        pump_status = event.data
        print("Pump status changed:", pump_status)

    # Get references to the specific data fields
    pump_dur_ref = db.reference('/devices/pumpUpDuration')
    pump_ref = db.reference('/devices/pumpOn')

    # Listen for changes on each data field
    pump_dur_ref.listen(handle_pump_duration_change)
    pump_ref.listen(handle_pump_change)

except Exception as e:
    logging.error("An error occurred:", exc_info=True)
