import random, threading

class pattern():
	def __init__(self):
		self.wait = False
	
	def sequence(self, neopixel, number, tstop):
		self.wait = True
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
		neopixel.clear()
		neopixel.show()
		print 'end'
		self.wait = False

