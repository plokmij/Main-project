fin = open('outegraph','r')
fout = open('sherikkumout','w')

listoflis = []

for line in fin:
    djanlist = line.split()
    djanlist.sort()
    listoflis.append((djanlist[0], djanlist[1]))

mset = set(listoflis)

for tup in mset:
    fout.write(str(tup[0])+" "+str(tup[1])+"\n")