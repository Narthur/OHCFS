#!/usr/bin/env python

# If double-clicking doesn't work:
# - Execute `chmod +x launchWebApp.pyw`
# - Make sure `.pyw` files are associated with Python Launcher on Unix or Python.exe on Windows

import BaseHTTPServer, CGIHTTPServer, cgitb, webbrowser
cgitb.enable()

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
PORT = 8000
serverAddress = ("", PORT)

print "serving at port", PORT

webbrowser.open('localhost:{}/htbin/app.py'.format(PORT))

httpd = server(serverAddress, handler)
httpd.serve_forever()