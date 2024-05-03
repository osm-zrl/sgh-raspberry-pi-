from gpiozero import AngularServo


#180 opened
#90 closed
class door:
    def __init__(self,pin,closed_angle,opened_angle):
        self.servo =  AngularServo(pin, min_angle=0, max_angle=180,min_pulse_width=0.0005, max_pulse_width=0.0025)
        self.closed_angle = closed_angle
        self.opened_angle = opened_angle
        self.servo.angle = 180 #initial angle

    def openDoor(self):
        self.servo.angle = self.opened_angle
        print("door opened:", self.servo.angle)

    def closeDoor(self):
        self.servo.angle = self.closed_angle
        print("door closed:", self.servo.angle)
