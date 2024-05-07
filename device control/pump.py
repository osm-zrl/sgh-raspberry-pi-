import RPi.GPIO as GPIO

class pump:
    def __init__(self, pin):

        self.pin = pin

    def StartPump(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def ClosePump(self):
        GPIO.output(self.pin, GPIO.LOW)

    def CleanPump(self):
        GPIO.cleanup()
