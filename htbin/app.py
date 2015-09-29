#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# If this page isn't working, try executing `chmod +x app.py` in terminal.

# enable debugging
import cgitb, cgi; cgitb.enable()
from classes import Factory

factory = Factory.Factory()
webApp = factory.makeWebApp()

print "Content-Type: text/html"
print
print webApp.getOutput()

print "<form method=get><input name='myField' /><input type=submit /></form>"

form = cgi.FieldStorage()
input = form.getfirst('myField',None)

if (input != None):
    print input