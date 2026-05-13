def start():
    print("Motor Started")


def stop():
    print("Motor Stopped")


# --- Raspberry Pi version (uncomment to use) ---
# import RPi.GPIO as GPIO
#
# PIN = 18
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(PIN, GPIO.OUT)
#
# def start():
#     GPIO.output(PIN, GPIO.HIGH)
#
# def stop():
#     GPIO.output(PIN, GPIO.LOW)

# Code for the L298N
import RPi.GPIO as GPIO

# L298N control pins
IN1 = 23
IN2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

def start():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    print("Motor Started")

def stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    print("Motor Stopped")