#!/usr/bin/python3

import cgi, psycopg2


conn = psycopg2.connect(host="prdatabase-test.cea3qgtmitwj.us-east-2.rds.amazonaws.com", port = 5432, database="postgres", user="postgres", password="Pylearn79")

cur = conn.cursor()

cur.execute("""SELECT * FROM doctor""")
query_results = cur.fetchall()
print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<body>")
print(query_results)
print ("</body>")
print ("</html>") 
