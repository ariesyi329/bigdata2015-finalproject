#!/usr/bin/python
import sys
from datetime import datetime

for line in sys.stdin:
    line = line.strip()
    values = line.split(',')
    if values[0]:
        tip_perc = values[-3]
        pickup_time = values[2]
        try:
            date, time = pickup_time.split(' ')
            time = time[:2]
            date = datetime.strptime(date, '%Y-%m-%d')
            weekday = date.weekday()
            if weekday == 5 or weekday == 6:
                workday = 0
            else:
                workday = 1
        except:
            pass
        print "%d,%s\t%s" % (workday, time,tip_perc)
