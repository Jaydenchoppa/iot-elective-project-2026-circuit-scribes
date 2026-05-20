import RPi.GPIO as GPIO

RELAY_PIN = 17

class Motor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(RELAY_PIN, GPIO.OUT)

        # ✅ Motor OFF on startup
        GPIO.output(RELAY_PIN, GPIO.LOW)
        self.running = False
        self.authorised = False

    # ---------------- START ----------------
    def start(self):
        print("start() called — authorised:", self.authorised)
        GPIO.output(RELAY_PIN, GPIO.HIGH)
        self.running = True

    # ---------------- STOP ----------------
    def stop(self):
        GPIO.output(RELAY_PIN, GPIO.LOW)
        self.running = False
        self.authorised = False

    # ---------------- GRANT ACCESS ----------------
    def grant_access(self):
        print("grant_access() called")
        self.authorised = True

    # ---------------- DENY ACCESS ----------------
    def deny_access(self):
        self.authorised = False
        self.stop()

    # ---------------- STATUS ----------------
    def status(self):
        return {"running": self.running}

    # ---------------- CLEANUP ----------------
    def cleanup(self):
        self.stop()
        GPIO.cleanup()