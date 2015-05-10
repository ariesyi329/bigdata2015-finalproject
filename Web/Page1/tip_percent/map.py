#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    values = line.split(',')
    if values[0]:
        tip_perc = values[-3]

        try:
        	tip_perc = float(tip_perc)
        except: 
        	pass

        if tip_perc >= 0:
            print "%.2f\t%d" % (tip_perc,1)
