#!/usr/bin/env python3
#Petit script python tout simple pour afficher deux iframes côte à côte pour comapraison visuelle de deux sites web
#zf170713.2243
#source: 
#https://gist.github.com/bradmontgomery/2219997
#https://gist.github.com/trungly/5889154

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

hostName = ""
hostPort = 18081
zheader = """<!DOCTYPE html>
<html><head><meta charset="utf-8">
<title>Console de comparaison visuelle V1.0</title></head><body>\n"""
zfooter = "</body></html>"

class MyServer(BaseHTTPRequestHandler):

	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		parsed_path = urllib.parse.urlparse(self.path)
		print(parsed_path)
		query_params = urllib.parse.parse_qs(parsed_path.query)
		if 'url1' in query_params or 'url2' in query_params:
			message = zheader
			message += '<iframe src="'
			message += query_params['url1'][0]
			message += '" width="49%" height="10000" align="left" scrollable="no"></iframe>\n'
			message += '<iframe src="'
			message += query_params['url2'][0]
			message += '" width="50%" height="10000" align="right" scrollable="no"></iframe>\n'
			message += zfooter
		else:
			message = ''
		self._set_headers()
		self.wfile.write(bytes(message, "utf-8"))

if __name__ == '__main__':
	print('Starting server at http://localhost:' + str(hostPort))
	myServer = HTTPServer((hostName, hostPort), MyServer)
	try:
		myServer.serve_forever()
	except KeyboardInterrupt:
		pass
	myServer.server_close()

