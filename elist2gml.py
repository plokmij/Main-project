#This program is written for GNU/Linux systems. 
#INPUT: edglist file; OUTPUT: gml file  

import sys
import os

inputFile = open(sys.argv[1],'r')
nodes = []

fedge = open("edge", "w")
fnode = open("node", "w")
fout  = open("graph.gml","w")

fout.write("graph\n[\n")

for line in inputFile:
	spil = line.split()
#	print "  edge\n  [\n    source "+str(spil[0]) + "\n    target "+str(spil[1])+"\n  ]"
	fedge.write("  edge\n  [\n    source "+str(spil[0]) + "\n    target "+str(spil[1])+"\n  ]\n")
	for node in spil:
		if node not in nodes:
			nodes.append( node )

for node in nodes:
#	print "  node\n  [\n    id "+str(node)+"\n  "+"]"
	fnode.write("  node\n  [\n    id "+str(node)+"\n  "+"]\n")
fedge.close()
fnode.close()
fout.close()

os.system("cat 'node' 'edge' >> graph.gml")

final = open("graph.gml","a")
final.write("]\n")

print "Output file : graph.gml"


