#!/usr/bin/python3

import cgi, psycopg2

form = cgi.FieldStorage()
patfname =  form.getvalue('pfname')
patlname = form.getvalue('plname')
patID = form.getvalue('pid')
pataddress = form.getvalue('paddress')
patemail = form.getvalue('pemail')
docID = form.getvalue('did')

conn = psycopg2.connect(host="prdatabase-test.cea3qgtmitwj.us-east-2.rds.amazonaws.com", port = 5432, database="postgres", user="postgres", password="Pylearn79")

cur = conn.cursor()

cur.execute("""SELECT * FROM doctor""")
query_results = cur.fetchall()
print(query_results)

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Patient Output Page</title>")
print ("</head>")
print ("<body>")
print ("<h1>Patient Output</h1>")
print ("<h2>You entered: %s, %s, %s, %s, %s, %s</h2>" % (patfname, patlname, patID, pataddress, patemail, docID))
print ("<br>")
print (query_results)
print ("</body>")
print ("</html>")
