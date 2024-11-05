  GNU nano 7.2                                                                                                                                                                                                                                                                          stopwatch.py                                                                                                                                                                                                                                                                                    
  GNU nano 7.2                                                                  stopwatch2.py
import RPi.GPIO as GPIO
import time
from tm1637 import TM1637

GPIO.setmode(GPIO.BCM)
clkPin = 21
dioPin = 16
inputPin = 20
ledPin = 26

tm = TM1637(clk=clkPin, dio=dioPin) # giving it the library, so i can use tm for both the clock and display.

GPIO.setup(inputPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # setting up the button
GPIO.setup(ledPin, GPIO.OUT) # setting up the light

running = False
num = 0 # starting time to give timer

try:
    while True:
        if GPIO.input(inputPin) == GPIO.LOW: # pressing the button starts it
            running = not running  # Toggle running state
            if running:
                GPIO.output(ledPin, GPIO.HIGH)  # Turn on LED
            else:
                GPIO.output(ledPin, GPIO.LOW)  # else Turn off LED
            time.sleep(0.1)  # the delay

        if running:    # THIS IS THE ACTUAL COUNTING PART
            tm.numbers(num // 60, num % 60)  # the time increments
            num = (num + 1) % 10000  # resets after 9999 because of the limit
            time.sleep(1)  # Update every second
        else:
            # When its not running, show the time without TURNING OFF!!!!!
            tm.numbers(num // 60, num % 60)  # Keep displaying the time
            time.sleep(0.1)  # delay when not running

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
