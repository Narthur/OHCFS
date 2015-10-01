#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# If this page isn't working, try executing `chmod +x app.py` in terminal.

# enable debugging
import cgitb, cgi; cgitb.enable()
from classes import Factory

factory = Factory.Factory()
webApp = factory.makeWebApp()
fieldStorage = cgi.FieldStorage()

def outputHeaders():
    print "Content-Type: text/html"
    print  # signals end of headers

outputHeaders()

print webApp.getOutput(fieldStorage)
