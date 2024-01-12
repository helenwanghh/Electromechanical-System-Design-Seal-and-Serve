import spidev
import RPi.GPIO as GPIO
import time

# Configure GPIO
GPIO.setmode(GPIO.BCM)
PWM_PIN = 17 # Adjust this based on your wiring
GPIO.setup(PWM_PIN, GPIO.OUT)
pwm = GPIO.PWM(PWM_PIN, 1000)  # 1000 Hz frequency

# Configure SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000  # Adjust this based on your sensor's requirements

def read_water_sensor():
    # Your water sensor reading logic using SPI
    # This is a placeholder; modify based on your sensor's protocol
    # Example: Read analog value from MCP3008 ADC
    adc_channel = 0
    adc_data = spi.xfer2([1, (8 + adc_channel) << 4, 0])
    sensor_value = ((adc_data[1] & 3) << 8) + adc_data[2]
    return sensor_value

def main():
    try:
        pwm.start(0)  # Start PWM with duty cycle 0

        while True:
            # Read water sensor value
            water_level = read_water_sensor()
            print(water_level)

            # Adjust PWM duty cycle based on water level
            #pwm_duty_cycle = min(water_level, 100)
            #pwm.ChangeDutyCycle(pwm_duty_cycle)

            #print(f"Water Level: {water_level}, PWM Duty Cycle: {pwm_duty_cycle}")

            time.sleep(1)

    except KeyboardInterrupt:
        pass
    finally:
        # Cleanup
        pwm.stop()
        spi.close()
        GPIO.cleanup()

if __name__ == "__main__":
    main()

