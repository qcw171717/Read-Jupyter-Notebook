#!/usr/bin/env python

import sys
import os
import json

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

if os.path.exists(sys.argv[1]):
	with open(sys.argv[1]) as f:
	    data = json.load(f)
	print()
	for i in range(len(data['cells'])):
		print(OKGREEN + '[' + str(i) + ']' + ENDC) #start with [cell number]
		for line in data['cells'][i]['source']:
			print('    ' + line.strip('\n'))
		print() #end cell
else:
	print(FAIL + "Cannot find file", sys.argv[1] + ENDC)
