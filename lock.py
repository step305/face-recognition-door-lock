import RPi.GPIO as GPIO
import time

def initalize_pins():
    print("pins are initialized")

def open_door():
    print("door is opening")

def close_door():
    print("door is closing")

def check_motion():
    print("motion detected")
    return True

def reset():
    print("reseting system")

def pi_cleanup():
    print("shutting down")
    GPIO.cleanup()

if __name__ == "__main__":
    # test your functions here
    pass