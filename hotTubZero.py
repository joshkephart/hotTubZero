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

# button toggle functions
# - need one for each because it seems that you cannot pass in parameters with when_pressed binding
def pumpOneToggle():
    pumpOne.toggle()
def pumpTwoToggle():
    pumpTwo.toggle()

# bind toggle function to button press
pumpOneButton.when_pressed = pumpOneToggle
pumpTwoButton.when_pressed = pumpTwoToggle

pause()