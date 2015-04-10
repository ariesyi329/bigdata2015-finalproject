#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    values = line.split(',')
    if values[0]:
        if values[5] == 'CRD':
            tip = values[9]
            fare = values[6]
            print "%s\t%s" % (fare,tip)
