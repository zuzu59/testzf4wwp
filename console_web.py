#!/usr/bin/env python3
#Petit script python tout simple pour afficher deux iframes côte à côte pour comapraison visuelle de deux sites web
#zf170713.1558
#source: 
#https://gist.github.com/bradmontgomery/2219997
#https://gist.github.com/trungly/5889154


import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import urllib.parse

hostName = ""
hostPort = 18081

class MyServer(BaseHTTPRequestHandler):

	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()



	def do_GET(self):

		#parsed = urlparse.urlparse(url)
		parsed_path = urllib.parse.urlparse(self.path)
		print(parsed_path)
		query_params = urllib.parse.parse_qs(parsed_path.query)
		if 'url1' in query_params or 'url2' in query_params:
			message = '<iframe src="' 
			message += query_params['url1'][0]
			message += '" width="49%" height="10000" align="left" scrollable="no"></iframe>'
			message += '<iframe src="'
			message += query_params['url2'][0]
			message += '" width="49%" height="10000" align="right" scrollable="no"></iframe>'
		else:
			message = ''
		self._set_headers()
		self.wfile.write(bytes(message, "utf-8"))
#		self._set_headers()
#		self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
	#	POST is for submitting data.

	def do_POST(self):

		print( "incomming http: ", self.path )

		content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
		post_data = self.rfile.read(content_length) # <--- Gets the data itself
		self.send_response(200)

		client.close()


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
	myServer.serve_forever()
except KeyboardInterrupt:
	pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))

