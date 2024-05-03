from door import door
from time import sleep

doorControl = door(17,80,180)

while True:
    doorControl.openDoor()
    sleep(1)
    doorControl.closeDoor()
    sleep(1)