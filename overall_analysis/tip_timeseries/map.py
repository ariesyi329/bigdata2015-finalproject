#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    values = line.split(',')
    if values[0]:
        if values[5] == 'CRD':
            tip = values[9]
            fares = values[6]
            pickup_time = values[4]
            try:
                date, time = pickup_time.split(' ')
                time = time[:2]
            except:
                pass
            print "%s\t%s,%s" % (time,tip,fares)
