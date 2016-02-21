from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SocketServer import ThreadingMixIn
import threading, NeoPixel
from plugin import sequences
from time import sleep


class LEDHandler(BaseHTTPRequestHandler):
    def getSequences(self):
	self.s = sequences()
	self.sequences = self.s.getSequences()


    def do_GET(self):
	print threading.enumerate()
	self.getSequences()
	print self.path

	self.send_response(200)
	self.send_header("Content-type", "text/html")
  	self.end_headers()

	if self.path[1:] in self.sequences.keys():

		self.wfile.write('yes!')
		
		try: self.tstop.set()
		except: print 'tstop not set'
		self.tstop = threading.Event()
		self.t = threading.Thread(target=self.sequences[self.path[1:]].sequence, args=(ledstrip, 10, self.tstop))
		self.t.start()

	for key in self.sequences.keys():
		self.wfile.write("<a href=\"%s\" />%s</a><br>" % (key, key))
	
	if self.path[1:] == "":
		try: self.tstop.set()
		except:pass
		print 'root'
		


ledstrip = NeoPixel.NeoPixel(129)
server = HTTPServer(('',8080),LEDHandler)
server.serve_forever()
