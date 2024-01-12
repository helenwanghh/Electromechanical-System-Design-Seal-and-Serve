import RPi.GPIO as GPIO
import time

# Constants
RELAY_PIN = 2   # GPIO pin connected to the relay

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

# PWM setup
pwm = GPIO.PWM(RELAY_PIN, 100)  # Create a PWM object at 100 Hz
pwm.start(0)  # Start PWM with 0% duty cycle initially

try:
    while True:
        # Turn on pump
        pwm.ChangeDutyCycle(100)  # 100% duty cycle (full speed)
        time.sleep(5)
        print("on")
        pwm.ChangeDutyCycle(0)
        time.sleep(5)

except KeyboardInterrupt:
    # Graceful exit on Ctrl+C
    pwm.stop()
    GPIO.cleanup()
