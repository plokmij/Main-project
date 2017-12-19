import json
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE gitopi
             (userid text, reposid text, type text)''')
table = []
tab = {}
with open('2015-03-30-13.json', 'r') as f:
    for line in f:
        table.append(json.loads(line))

for i in range(len(table)):
		tab[table[i]["actor"]["id"]] = (table[i]["repo"]["id"],table[i]["type"])
		c.execute("INSERT INTO gitopi VALUES (?,?,?)",(table[i]["actor"]["id"],table[i]["repo"]["id"],table[i]["type"]))
print tab
#for row in table:
 #   print(row)
conn.commit()
conn.close()
