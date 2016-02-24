from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SocketServer import ThreadingMixIn
import threading, NeoPixel
from plugin import sequences
from time import sleep


class LEDHandler(BaseHTTPRequestHandler):

    def get_fields(self, path):
	print path
        s = path.rfind('?')
        if s == -1 or s+1 == len(path):
            return {}

        path = path[s+1:].split('&')
        properties = {}
        for var in path:
          property = var.split('=')
	  try: property[1] = int(property[1])
	  except: pass
          properties[property[0]] = property[1]

    	return properties

    def do_GET(self):
	
	properties = self.get_fields(self.path)
	print properties
	self.send_response(200)
	self.send_header("Content-type", "text/html")
  	self.end_headers()
	
	if '?' in self.path: s = self.path.rfind('?')
	else: s = len(self.path)
	
	if self.path[1:s] in sequences.keys():
		
		led.load(self.path[1:s], properties)
		#print sequences[self.path[1:s]].getProp()


	for key in sequences.keys():
		self.wfile.write("<a href=\"%s\" />%s</a><br>" % (key, key))
	self.wfile.write("<a href=\"/\" />Clear</a><br>")
	
	if self.path[1:] == "":
		led.stop()
		print 'root'
		

class LED():
	def __init__(self):
		self.tstop = threading.Event()

	def load(self, target, properties):
		self.tstop.set()
		self.tstop = threading.Event()
		self.t = threading.Thread(target=sequences[target].sequence, args=(ledstrip, self.tstop), kwargs=properties)
		self.t.start()
	
	def stop(self):
		self.tstop.set()



led = LED()
s = sequences()
sequences = s.getSequences()

ledstrip = NeoPixel.NeoPixel(129)
server = HTTPServer(('',8080),LEDHandler)

try: server.serve_forever()
except KeyboardInterrupt:
	led.tstop.set()
	
