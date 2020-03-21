# import relevant packages
from gpiozero import Button, OutputDevice
from time import sleep
from signal import pause

# initialize the GPIO pins for input buttons
pumpOneButton = Button(16, False)
pumpTwoButton = Button(20, False)

# initialize the GPIO pins for generic outputs
pumpOne = OutputDevice(17)
pumpTwo = OutputDevice(27)
circPump = OutputDevice(22)
heater = OutputDevice(25)

# bind toggle functions to button presses
pumpOneButton.when_pressed = pumpOne.toggle
pumpTwoButton.when_pressed = pumpTwo.toggle

pause()