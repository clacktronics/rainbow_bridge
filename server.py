from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SocketServer import ThreadingMixIn
import threading, NeoPixel
from plugin import sequences
from time import sleep


class LEDHandler(BaseHTTPRequestHandler):

    def do_GET(self):
	
	print self.path

	self.send_response(200)
	self.send_header("Content-type", "text/html")
  	self.end_headers()

	if self.path[1:] in sequences.keys():

		self.wfile.write('yes!')
		
		led.load(self.path[1:])

	for key in sequences.keys():
		self.wfile.write("<a href=\"%s\" />%s</a><br>" % (key, key))
	
	if self.path[1:] == "":
		led.stop()
		print 'root'
		

class LED():
	def __init__(self):
		self.tstop = threading.Event()

	def load(self, target):
		self.tstop.set()
		self.tstop = threading.Event()
		self.t = threading.Thread(target=sequences[target].sequence, args=(ledstrip, 10, self.tstop))
		self.t.start()
	
	def stop(self):
		self.tstop.set()



led = LED()
s = sequences()
sequences = s.getSequences()

ledstrip = NeoPixel.NeoPixel(129)
server = HTTPServer(('',8080),LEDHandler)
server.serve_forever()
