import RPi.GPIO as GPIO
import time

# Define the GPIO pin numbers
sensorPin = 17  # Sensor is connected to GPIO17
ledPin = 5     # LED is connected to GPIO23

# Set up the GPIO channels - one input and one output
GPIO.setmode(GPIO.BCM)       # Use Broadcom SoC pin numbers
GPIO.setup(sensorPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

try:
    while True:
        # Read the state of the sensor
        sensorState = GPIO.input(sensorPin)
        print(sensorState)

        # Turn on LED if sensor is triggered, otherwise turn it off
        if sensorState == GPIO.HIGH:
            GPIO.output(ledPin, GPIO.HIGH)
        else:
            GPIO.output(ledPin, GPIO.LOW)

        # Small delay to prevent excessive CPU usage
        time.sleep(0.1)
except KeyboardInterrupt:
    # Clean up GPIO settings before exiting
    GPIO.cleanup()
