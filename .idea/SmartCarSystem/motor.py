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