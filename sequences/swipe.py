import random, threading
from time import sleep

class pattern():
	def __init__(self):
		self.wait = False
	
	def sequence(self, neopixel, tstop, speed=1):
		
		speed /= 1000.
		
		while not tstop.is_set():
			color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
			for i in range(129):
				neopixel.setPixelColor(i, *color)
				neopixel.show()
				sleep(speed)
			color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
			for i in range(129,-1,-1):
				neopixel.setPixelColor(i, *color)
				neopixel.show()
				sleep(speed)
		neopixel.clear()
		neopixel.show()

