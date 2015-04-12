#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    values = line.split(',')
    if values[0]:
        if values[5] == 'CRD':
            tip = values[9]
            fares = values[6]
            dropoff_zipcode = values[-1]
            print "%s\t%s,%s" % (dropoff_zipcode,tip,fares)
