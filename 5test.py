fin = open("sherikkumout",'r')
fout = open("realsherikkumout.csv", 'w')

for line in fin:
	tlis = line.split()
	fout.write(str(tlis[0])+";"+str(tlis[1])+"\n")
