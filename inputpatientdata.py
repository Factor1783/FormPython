#!/usr/bin/python3

import cgi
import psycopg2

form = cgi.FieldStorage()
patfname =  form.getvalue('pfname')
patlname = form.getvalue('plname')
patID = form.getvalue('pid')
pataddress = form.getvalue('paddress')
patemail = form.getvalue('pemail')
docID = form.getvalue('did')

conn = psycopg2.connect(host="prdatabase-test.cea3qgtmitwj.us-east-2.rds.amazonaws.com", port = 5432, database="postgres", user="postgres", password="Pylearn79")

# Create a cursor object
cur = conn.cursor()

#pid, lastname, firstname, address, email, did
postgres_insert_query = """ INSERT INTO patient VALUES (%s,%s,%s,%s,%s,%s)"""
record_to_insert = (pid, patfname, patlname, pataddress, patemail, docID)
cur.execute(postgres_insert_query, record_to_insert)


conn.commit()
count = cur.rowcount

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Patient Output Page</title>")
print ("</head>")
print ("<body>")
print ("<h1>Patient Output</h1>")
print ("<h2>You entered: %s, %s, %s, %s, %s, %s</h2>" % (patfname, patlname, patID, pataddress, patemail, docID))
print ("<br>")
print (count, "Record inserted successfully into patient table")
print ("<br>")
print ("<p>PostgreSQL connection is closed</p>")
print ("</body>")
print ("</html>")


# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cur.close()
conn.close()



