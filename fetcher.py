import sys
import json
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
table = []
tab = {}

c.execute('''CREATE TABLE IF NOT EXISTS gitopi(userid text, reposid text, type text)''')
for i in range(1,len(sys.argv)):
	print "Processing : ",str(sys.argv[i])
	with open(str(sys.argv[i]), 'r') as f:
    		for line in f:
        		table.append(json.loads(line))
	print "Completed"
	print str(sys.argv[i])+" is closing ...",
	f.close();
	print(" Done");
for i in range(len(table)):
		tab[table[i]["actor"]["id"]] = (table[i]["repo"]["id"],table[i]["type"])
		c.execute("INSERT INTO gitopi VALUES (?,?,?)",(table[i]["actor"]["id"],table[i]["repo"]["id"],table[i]["type"]))
		

conn.commit()
conn.close()
