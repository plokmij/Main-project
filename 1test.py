#!/usr/bin/python
import sys
import sqlite3
conn = sqlite3.connect(sys.argv[1])
c = conn.cursor()
userepo = {}

c.execute(''' SELECT * FROM HELL LIMIT 10000''')

#userepo contains informations about user - repo relations

while True:
	X = c.fetchone()
	if type(X) == type((3,4)):
		if X[0] in userepo.keys():
			userepo[X[0]].append(X[1])
		else:
			userepo[X[0]] = [X[1]]
	else:
		break;

useruser = {}
for user1 in userepo:
	for user2 in userepo:
		if user1 != user2:
			if list(set(userepo[user1]).intersection(userepo[user2])) != [] :
				if user1 in useruser.keys():
					useruser[user1].append(user2)
				else:
					useruser[user1] = [user2]
f = open("elisgraph",'w')
for thing in useruser:
	f.write('\n')
	f.write( str(thing) + ' ')
	for pthing in useruser[thing]:
		f.write( str(pthing)+ ' ')

		
