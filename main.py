from gpiozero import LED
from signal import pause
from time import sleep

red = LED(17)


while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)
    print("hello world!")


