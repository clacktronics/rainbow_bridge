import imp, os
from time import sleep

SEQ_DIR = 'sequences'
IGNORE = ['__init__.py', 'seq_temp.py','randomwalk2.py']


class sequences():
	def __init__(self):
		self.sequences = {}

	def getSequences(self):
		files = os.listdir(SEQ_DIR)
		for i in files:
			if i[-3:] == '.py' and i not in IGNORE:
				i = i [:-3]
				module = imp.find_module(i,[SEQ_DIR])
				self.sequences[i] = imp.load_module(i, *module).pattern()	
		return self.sequences

if __name__ == "__main__":

	import NeoPixel, threading, random

	s = sequences()
	s.getSequences()

	ledstrip = NeoPixel.NeoPixel(129)
	
	print dir(s.sequences['randomwalk'])
	
	tstop = threading.Event()
	t = threading.Thread(target=s.sequences['randomwalk'].sequence, args=(ledstrip, 10, tstop))
	t.start()

	while True:
		print 'a'
		sleep(1)
		tstop.set()
		sleep(1)
		tstop = threading.Event()
		t = threading.Thread(target=s.sequences['randomwalk'].sequence, args=(ledstrip, 10, tstop))
		t.start()
		print threading.enumerate()
