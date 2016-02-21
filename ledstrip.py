import NeoPixel

def ledStrip():
	def __init__(self):
		self.strip = NeoPixel.NeoPixel(129)

	def play(self, sequence):

	def write(self, input):
	'''expects dictionary input of pixel:(R,G,B)'''
		self.strip.clear()
		for pixel in input:
			self.setPixelColor(pixel *input[pixel])
		self.strip.show()
