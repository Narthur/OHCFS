#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# If this page isn't working, try executing `chmod +x [FILE]` in terminal.

import cgitb
import cgi

cgitb.enable()

form = cgi.FieldStorage()

print "Content-Type: text/html"
print

print '<h2>Using Get</h2>'
print "<form method=get><input name='myGet' /><input type=submit /></form>"

val = form.getfirst('myGet', None)

if val:
    print val

print '<h2>Using Post</h2>'
print "<form method=post><input name='myPost' /><input type=submit /></form>"

val = form.getvalue('myPost', None)

if val:
    print val
