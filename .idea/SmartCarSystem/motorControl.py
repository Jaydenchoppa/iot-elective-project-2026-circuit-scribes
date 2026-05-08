def start_motor():
    print("Motor Started")


def stop_motor():
    print("Motor Stopped")

# import RPi.GPIO as GPIO
#
# MOTOR_PIN = 18
#
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(MOTOR_PIN, GPIO.OUT)
#
#
# def start_motor():
#     GPIO.output(MOTOR_PIN, GPIO.HIGH)
#
#
# def stop_motor():
#     GPIO.output(MOTOR_PIN, GPIO.LOW)