

#!/usr/bin/python

import sys


#input comes from STDIN (stream data that goes to the program)
f = open('professors.txt', 'r')
for line in f.readlines():

	#Fill in your map code here. To write to output file, use "print"
    l = line.strip().split(',')
    print l

f.close()
