import time
import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep


temp = -30

if temp < 30:
	#Cold temperatures (Blue)

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(22, GPIO.OUT)
	GPIO.output(22, True)
	time.sleep(60)
	GPIO.output(22, False)

elif   temp >= 30  and temp <=70 :
	#Normal temperatures (Green LED)
	
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(27, GPIO.OUT)
		GPIO.output(27, True)
		time.sleep(6)
		GPIO.output(27, False)


else:
 #Very hot temperatures (Red LED)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17, GPIO.OUT)
	GPIO.output(17, True)
	time.sleep(6)
	GPIO.output(17, False)

