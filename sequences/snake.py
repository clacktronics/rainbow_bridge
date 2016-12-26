import random, threading
from time import sleep

class pattern():
	def __init__(self):
		self.wait = False
	
	def sequence(self, neopixel, tstop, speed=0,r=255,g=255,b=255,spread=100):
		

		speed /= 50.	
		colours = (0,255,100)
		body = [1,2]
		direction = 1
		length = 2
		ldir = 1
		apple = 128

		
		while not tstop.is_set():
			neopixel.clear()

			body.append(body[-1]+direction)

			if len(body) > length: body.pop(0)
			if length > apple: 
				length = 2
				body = [1,2]
			if body[-1] > apple: 
				body.pop(-1)
				body.reverse()
				direction *= -1
				length += ldir
				apple = 129
			elif body[-1] < 0:
				body.pop(-1)
				body.reverse()
				direction *= -1
				apple = random.randrange(3,128)
			print body
			for x in body: neopixel.setPixelColor(x, *colours)
			neopixel.setPixelColor(apple, 255,0,0)
			neopixel.show()
			sleep(speed)

		neopixel.clear()
		neopixel.show()
		print 'end'
		self.wait = False

