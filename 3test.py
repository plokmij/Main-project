#!/usr/bin/python
f = open('elisgraph','r')
fout = open('outegraph','w')
for line in f:
    tlist = line.split()
    for i in range(2,len(tlist)):
        fout.write(str(tlist[0])+" "+str(tlist[i])+'\n')
    