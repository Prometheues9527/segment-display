  GNU nano 7.2                                                                                                                                                                                                                                                                            button.py                                                                                                                                                                                                                                                                                     
import RPi.GPIO as GPIO
import time

ledPin = 21 # this one sets the LED as a input
inputPin = 13 # this one sets the button as the "activator"

GPIO.setmode(GPIO.BCM) # this sets the pin mode numbering system
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(inputPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # idk i found this online

led_state = False
last_button_state = GPIO.HIGH

try:    # basically lets you test a line of code for errors
    while True:
        current_button_state = GPIO.input(inputPin)     #reads the currnet state

        if last_button_state == GPIO.HIGH and current_button_state == GPIO.LOW:
            led_state = not led_state
            GPIO.output(ledPin, led_state)              # this code turns the button on or off when pressed

        last_button_state = current_button_state
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:     # do this code after try is done
    GPIO.cleanup() # resets the modes of all pins to input

