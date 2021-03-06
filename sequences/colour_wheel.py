import random, threading
from time import sleep


gamma = [
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,
    1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2,
    2,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  5,  5,  5,
    5,  6,  6,  6,  6,  7,  7,  7,  7,  8,  8,  8,  9,  9,  9, 10,
   10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16,
   17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 24, 24, 25,
   25, 26, 27, 27, 28, 29, 29, 30, 31, 32, 32, 33, 34, 35, 35, 36,
   37, 38, 39, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50,
   51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 68,
   69, 70, 72, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89,
   90, 92, 93, 95, 96, 98, 99,101,102,104,105,107,109,110,112,114,
  115,117,119,120,122,124,126,127,129,131,133,135,137,138,140,142,
  144,146,148,150,152,154,156,158,160,162,164,167,169,171,173,175,
  177,180,182,184,186,189,191,193,196,198,200,203,205,208,210,213,
  215,218,220,223,225,228,231,233,236,239,241,244,247,249,252,255 ]

def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;



class pattern():
	def __init__(self):
		self.wait = False
	
	def sequence(self, neopixel, tstop, speed=0,r=255,g=255,b=255,spread=100):
		

		speed /= 1000.	

		colours = [0, 0, 0]	
		focus = 0
		
		while not tstop.is_set():
			for o in range(129):
				neopixel.clear()
				print "@"
				for x in range(129): 
					out = x + o
					if out > 129: out = 258 - out
					if out > 64: out = 129 - out

					r = map(out,0,64,0,255)
					r = gamma[b]

					g = out + 43
					if g > 64: g = 129 - g
					g = map(g,0,64,0,255)
					g = gamma[g]

					b = out + 86 
					if b > 43: b = 129 - b
					b = map(b,0,64,0,255)
					b = gamma[b]

					neopixel.setPixelColor(x,r,g,b)
				#sleep(.01)
				neopixel.show()

		neopixel.clear()
		neopixel.show()
		print 'end'
		self.wait = False

