import random, threading
from time import sleep

class pattern():
	def __init__(self):
		self.wait = False
	
	def sequence(self, neopixel, tstop, speed=0,r=255,g=255,b=255,spread=100):
		

		speed /= 1000.	

		colours = [0, 0, 0]	
		focus = 0
		
		while not tstop.is_set():
			neopixel.clear()

			colours[focus] += 1


			if colours[focus] == 255:
				if focus == 2 :
					focus = 0
				else:
					focus +=1


			if focus == 0:
				prev = 2
			else:
				prev = focus - 1

			
			colours[prev] -= 1

			if colours[prev] < 0:
				colours[prev] = 0

			for x in range(129): neopixel.setPixelColor(x, *colours)
			print colours
			neopixel.show()
			sleep(speed)
		neopixel.clear()
		neopixel.show()
		print 'end'
		self.wait = False

