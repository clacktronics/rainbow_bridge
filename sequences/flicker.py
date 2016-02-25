import random, threading
from time import sleep

class pattern():
	def __init__(self):
		self.wait = False
	
	def sequence(self, neopixel, tstop, speed=1):
		
		speed /= 1000.

		last = (0, 0, 0)
		
		while not tstop.is_set():
			color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
			for i in range(random.randrange(1,20)):	
				for i in range(129):
					neopixel.setPixelColor(i, *last)
				neopixel.show()
				sleep(random.uniform(0,0.05))
				for i in range(129):
					neopixel.setPixelColor(i, *color)
				neopixel.show()
				sleep(random.uniform(0,0.5))
			sleep(random.randrange(1,5))
			last = color
		neopixel.clear()
		neopixel.show()

