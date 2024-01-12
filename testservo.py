import RPi.GPIO as GPIO
import pigpio
import time

servo = 13

# more info at http://abyz.me.uk/rpi/pigpio/python.html#set_servo_pulsewidth
GPIO.setmode(GPIO.BCM)
pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)
HEAT_PIN = 16 
GPIO.setup(HEAT_PIN, GPIO.OUT)
pwm.set_PWM_frequency( servo, 50 )
pwm7 = GPIO.PWM(HEAT_PIN, 100)  # Create a PWM object at 100 Hz
pwm.set_servo_pulsewidth( servo, 1500 )
pwm7.start(100)  # Start PWM with 0% duty cycle initially
time.sleep(25)

print( "0 deg" )
pwm.set_servo_pulsewidth( servo, 500 ) ;
time.sleep( 8 )

print( "90 deg" )
pwm.set_servo_pulsewidth( servo, 1500 ) ;
pwm7.start(0)


# turning off servo
pwm.set_PWM_dutycycle( servo, 0 )
pwm.set_PWM_frequency( servo, 0 )
