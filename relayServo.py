from gpiozero import Servo
from RPi import GPIO
from time import sleep

# Setup for servo motor
servo_pin = 13  # Change to your GPIO pin
servo = Servo(servo_pin)

# Setup for relay
relay_pin = 13  # Change to your GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

# Function to move servo
def move_servo(angle):
    if angle == 45:
        servo.mid()  # This assumes that mid position corresponds to 45 degrees
    elif angle == 0:
        servo.min()  # This assumes that min position corresponds to 0 degrees

try:
    # Turn on the relay
    GPIO.output(relay_pin, GPIO.HIGH)
    print("Relay is ON")
    
    # Wait for 35 seconds
    sleep(2)
    
    # Move servo from 0 to 45 degrees
    move_servo(0)
    print("Servo moved to 70 degrees")
    
    # Wait for 5 seconds
    sleep(2)
    
    # Move servo back to 0 degrees
    print("Servo moved back to 0 degrees")

    
    # Turn off the relay
    GPIO.output(relay_pin, GPIO.LOW)
    print("Relay is OFF")
    
    # Wait for 30 seconds before ending the script or doing anything else
    sleep(2)

except KeyboardInterrupt:
    # Clean up GPIO on CTRL+C exit
    GPIO.cleanup()

# Clean up GPIO on normal exit
GPIO.cleanup()
