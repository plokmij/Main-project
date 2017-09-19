#!/usr/bin/python
import os
import sys

for i in range(1,len(sys.argv)):
	print "Extracting "+str(sys.argv[i]),
	os.system("dtrx "+str(sys.argv[i]))
	print "Done"
	print "Fetching data from "+str(sys.argv[i])[:-3],
	os.system("./fetcher.py "+str(sys.argv[i])[:-3])
	print "Done"
	print "Deleting  "+str(sys.argv[i])[:-3],
	os.system("rm "+str(sys.argv[i])[:-3])
	print "Done"

#27843
