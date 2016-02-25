import random, threading
from time import sleep

class pattern():
	def __init__(self):
		self.wait = False
	
	def sequence(self, neopixel, tstop, speed=1):
		
		speed /= 1000.

		last = (0, 0, 0)
		
		while not tstop.is_set():

			color = (random.randrange(0, 100), random.randrange(0, 100), random.randrange(0, 100))

			lower_range = random.randrange(0,60)
			upper_range = random.randrange(lower_range,129)

			for i in range(random.randrange(1,20)):	
				for i in range(lower_range, upper_range):
					neopixel.setPixelColor(i, 0, 0, 0)
				neopixel.show()
				sleep(random.uniform(0,0.05))
				for i in range(lower_range, upper_range):
					neopixel.setPixelColor(i, *color)
				neopixel.show()
				sleep(random.uniform(0,0.5))

			last = color
		neopixel.clear()
		neopixel.show()

