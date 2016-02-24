import random, threading
from time import sleep

class pattern():
	def __init__(self):
		self.wait = False

	def sequence(self, neopixel, tstop, number=10, speed=1):
		self.wait = True

		speed /= 1000.		

		output = {}
		sprites = [random.randint(1,128) for i in range(number)]
		direction = [random.randrange(-1,2,2) for i in range(number)]
		colors = [(random.randrange(1,255), random.randrange(1,255), random.randrange(1,255)) for i in range(number)]

		while not tstop.is_set():
			neopixel.clear()
			for n, sprite in enumerate(sprites):
				if sprite >= 128 or sprite <=0: direction[n]  *= -1
				sprites[n] += direction[n]
				neopixel.setPixelColor(sprite, *colors[n])
			neopixel.show()
			sleep(speed)
		neopixel.clear()
		neopixel.show()
		print 'end'
		self.wait = False

