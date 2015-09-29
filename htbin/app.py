#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# If this page isn't working, try executing `chmod +x app.py` in terminal.

# enable debugging
import cgitb; cgitb.enable()
from classes import Factory

factory = Factory.Factory()
webApp = factory.makeWebApp()

print "Content-Type: text/html"
print
print webApp.getOutput()