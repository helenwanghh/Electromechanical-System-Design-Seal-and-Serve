import RPi.GPIO as GPIO
import time
# Constants
RELAY_PIN = 22  # GPIO pin number, which connects to the IN pin of relay
# Set up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, GPIO.LOW)
try:
    # Main loop
    while True:
        print('TURNING ON')
        GPIO.output(RELAY_PIN, GPIO.HIGH)
        time.sleep(5)
        print('TURNING Off')
        GPIO.output(RELAY_PIN, GPIO.LOW)  # turn off pump for 5 seconds
        time.sleep(5)
except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()
