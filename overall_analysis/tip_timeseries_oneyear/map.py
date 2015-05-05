#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    values = line.split(',')
    if values[0]:
        tip_perc = values[-3]
        pickup_time = values[2]
        try:
            date, time = pickup_time.split(' ')
            time = time[:2]
        except:
            pass
        print "%s\t%s" % (time,tip_perc)
