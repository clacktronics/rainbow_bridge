import random, threading
from time import sleep

class pattern():
	def __init__(self):
		self.wait = False
	
	def sequence(self, neopixel, tstop, speed=1):
		
		speed /= 50.
		
		while not tstop.is_set():
			color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
			for i in range(65):
				neopixel.setPixelColor(64+i, *color)
				neopixel.setPixelColor(64-i, *color)
				neopixel.show()
				sleep(speed)
			color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
			sleep(2)
			for i in range(65):
				neopixel.setPixelColor(i, *color)
				neopixel.setPixelColor(128-i, *color)
				neopixel.show()
				sleep(speed)
			sleep(2)
		neopixel.clear()
		neopixel.show()

