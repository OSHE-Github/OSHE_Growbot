import RPi.GPIO as GPIO
import os

# Read data from Raspberry Pi (specifically read GPU temperature)
temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
print("GPU temperature is {}".format(temp[5:]))

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

# Turn on/off LED based on user input
try:
    while True:
        user_input = input("Turn LED On or Off with 1 or 0 (Ctrl-C to exit): ")
        if user_input is "1":
            GPIO.output(18,GPIO.HIGH)
            print("LED is on")
        elif user_input is "0":
            GPIO.output(18,GPIO.LOW)
            print("LED is off")
except KeyboardInterrupt:
    GPIO.cleanup()
    print("")
