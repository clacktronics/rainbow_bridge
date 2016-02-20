import imp, os

SEQ_DIR = 'sequences'
IGNORE = ['__init__.py']


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




s = sequences()
s.getSequences()
