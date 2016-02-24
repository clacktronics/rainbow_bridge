
                sprites = [60 for i in range(number)]
                direction = [random.randrange(-1,2,2) for i in range(number)]
                colors = [(random.randrange(1,255), random.randrange(1,255), random.rand$

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

