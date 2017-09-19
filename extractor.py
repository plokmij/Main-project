#!/usr/bin/python
import os
import sys

for i in range(1,len(sys.argv)):
	os.system("dtrx "+str(sys.argv[i]))
