#!/usr/bin/python
#flowsensor.py
import RPi.GPIO as GPIO
import time, sys

FLOW_SENSOR = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count
count = 0

def countPulse(channel):
   global count
   if start_counter == 1:
      count = count+1
#      print count
#      flow = count / (60 * 7.5)
#      print(flow)

GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)

while True:
    try:
        start_counter = 1
        time.sleep(1)
        start_counter = 0
        flow = (count * 60 * 2.25 / 1000)
        print "The flow is: %.3f Liter/min" % (flow)
        count = 0
        time.sleep(5)
    except KeyboardInterrupt:
        print '\ncaught keyboard interrupt!, bye'
        GPIO.cleanup()
        sys.exit()