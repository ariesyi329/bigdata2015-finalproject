#!/usr/bin/python
import sys
from datetime import datetime

for line in sys.stdin:
    line = line.strip()
    values = line.split(',')
    if values[0]:
        pickup_time = values[1]
        try:
            date, time = pickup_time.split(' ')
            date = datetime.strptime(date, '%Y-%m-%d')
            month = date.month
        except:
            pass

        print "%d\t%d" % (month,1)
