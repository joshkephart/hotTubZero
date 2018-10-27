# import relevant packages
from gpiozero import OutputDevice
from time import sleep

# set up pins we are going to use
pumpOne = OutputDevice(17)

# toggle pin every 5 seconds forever
while True:
    pumpOne.toggle()
    sleep(5)
