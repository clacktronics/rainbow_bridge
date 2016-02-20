from NeoPixel import NeoPixel
import random

class pattern():
	def __init__(self):
		print 'yay randomwalk works'


class LedStrip():
	def __init__(self):
		self.strip = NeoPixel(129)
	def sprites(self, number):

		sprites = [random.randint(1,128) for i in range(number)]
		direction = [random.randrange(-1,2,2) for i in range(number)]
		colors = [(random.randrange(1,255), random.randrange(1,255), random.randrange(1,255)) for i in range(number)]

		print sprites
		print direction

		while True:
			for n, sprite in enumerate(sprites):
				if sprite >= 128 or sprite <=0: direction[n]  *= -1
				sprites[n] += direction[n]
				self.strip.setPixelColor(sprite, *colors[n])
			self.strip.show()
			self.strip.clear()

        def sprites_randomwalk(self, number):

                sprites = [60 for i in range(number)]
                direction = [random.randrange(-1,2,2) for i in range(number)]
                colors = [(random.randrange(1,255), random.randrange(1,255), random.randrange(1,255)) for i in range(number)]

                print sprites  
                print direction

                while True:   
                        for n, sprite in enumerate(sprites):
                                sprites[n] += random.randrange(-1,2,2)
                                if sprites[n] >= 128: sprites[n] = 0
				if sprites[n] <=0: sprites[n] = 128 
                                self.strip.setPixelColor(sprite, *colors[n])
                        self.strip.show()
			self.strip.clear()
				
						
if __name__ == "__main__":
	bridge = LedStrip()
	bridge.sprites_randomwalk(10)
