#!/usr/bin/python
import sys

current_month = None
count = 0

for line in sys.stdin:
    line = line.strip()
    month, occurrence = line.split('\t')

    try:
        month = int(month)
    except ValueError:
        pass

    if  month == current_month:
        count += 1
    else:
        if current_month:
            print "%s\t%d" % (current_month, count)

        current_month = month
        count = 1

if current_month == month:
    print "%s\t%d" % (month, count)
