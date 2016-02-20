from NeoPixel import NeoPixel
import random

class LedStrip(object):
	def __init__(length):
		self.strip = NeoPixel(length)
	

	
						
if __name__ == "__main__":
	bridge = LedStrip(129)
