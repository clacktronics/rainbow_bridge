import random, threading
from time import sleep

class pattern():
	def __init__(self):
		self.wait = False
	
	def sequence(self, neopixel, tstop, speed=1,r=255,g=10,b=100):
		
		def map(x, in_min, in_max, out_min, out_max):
			return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

		self.wait = True

		speed /= 1000.		
		
		while not tstop.is_set():
			neopixel.clear()
			for i in range(129):
				brightness = random.randrange(0,255)
				Red = map(brightness, 0, 255, 0, r)
				Green = map(brightness, 0, 255, 0, g)
				Blue = map(brightness, 0, 255, 0, b)
				neopixel.setPixelColor(i, Red, Green, Blue)
			neopixel.show()
			sleep(speed)
		neopixel.clear()
		neopixel.show()
		print 'end'
		self.wait = False

