#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# If this page isn't working, try executing `chmod +x [FILE]` in terminal.

import cgitb, cgi; cgitb.enable()

form = cgi.FieldStorage()

print "Content-Type: text/html"
print

print '<h2>Using Get</h2>'
print "<form method=get><input name='myGet' /><input type=submit /></form>"

input = form.getfirst('myGet',None)

if (input != None):
    print input

print '<h2>Using Post</h2>'
print "<form method=post><input name='myPost' /><input type=submit /></form>"

input = form.getvalue('myPost',None)

if (input != None):
    print input