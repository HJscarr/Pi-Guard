from gpiozero import Buzzer, MotionSensor
from time import sleep

# Set up the motion sensor and buzzer
pir = MotionSensor(4)
buzzer = Buzzer(16)

# Let the sensor settle
sleep(3)

# Main program
try:
    while True:
        pir.wait_for_motion()
        print("Motion detected!!!")
        
        buzzer.on()
        sleep(2)
        buzzer.off()
except KeyboardInterrupt:
    print("Program terminated.")
