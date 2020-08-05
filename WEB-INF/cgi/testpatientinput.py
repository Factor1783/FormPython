#!/usr/bin/python3

import cgi
form = cgi.FieldStorage()
patfname =  form.getvalue('pfname')
patlname = form.getvalue('plname')
patID = form.getvalue('pid')
pataddress = form.getvalue('paddress')
patemail = form.getvalue('pemail')
docID = form.getvalue('did')


print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Patient Output Page</title>")
print ("</head>")
print ("<body>")
print ("<h1>Patient Output</h1>")
print ("<h2>You entered: %s, %s, %s, %s, %s, %s</h2>" % (patfname, patlname, patID, pataddress, patemail, docID))
print ("</body>")
print ("</html>")
