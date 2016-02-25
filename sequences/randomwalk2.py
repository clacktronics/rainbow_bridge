import random

class pattern():
        def __init__(self):
                self.wait = False

        def sequence(self, neopixel, tstop, number=10, speed=1):

                sprites = [60 for i in range(number)]
                direction = [random.randrange(-1,2,2) for i in range(number)]
                colors = [(random.randrange(1,255), random.randrange(1,255), random.randrange(1,255)) for i in range(number)]


                while not tstop.is_set():
                        for n, sprite in enumerate(sprites):
                                sprites[n] += random.randrange(-1,2,2)
                                if sprites[n] >= 128: sprites[n] = 0
                                if sprites[n] <=0: sprites[n] = 128
                                neopixel.setPixelColor(sprite, *colors[n])
                        neopixel.show()
                        neopixel.clear()
		neopixel.clear()
		neopixel.show()

