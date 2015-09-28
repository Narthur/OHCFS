#!/usr/bin/env python

import BaseHTTPServer, CGIHTTPServer, cgitb
cgitb.enable()

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
PORT = 8000
serverAddress = ("", PORT)

print "serving at port", PORT

httpd = server(serverAddress, handler)
httpd.serve_forever()