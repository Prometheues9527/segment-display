  GNU nano 7.2                                                                                                                                                                                                                                                                             LED.py                                                                                                                                                                                                                                                                                       
  GNU nano 7.2                                                                        LED.py
import RPi.GPIO as GPIO
import time

import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

try:
        GPIO.output(21,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(21,GPIO.LOW)
        time.sleep(1)
#

        GPIO.output(21,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(21,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        time.sleep(1)


#
        GPIO.output(16,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(16,GPIO.LOW)
        time.sleep(1)

finally:
         GPIO.cleanup()
