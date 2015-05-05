#!/usr/bin/python
import sys

current_time = None
current_tips_perc_sum = 0
count = 0

for line in sys.stdin:
    line = line.strip()
    keys, tips_perc = line.split('\t')
    workday, time = keys.split(',')

    try:
        tips_perc = float(tips_perc)

    except ValueError:
        pass

    if time == current_time:
        current_tips_perc_sum += tips_perc
        count += 1
    else:
        if current_time:
            avg_tips_perc = current_tips_perc_sum/count
            print "%s,%s\t%.2f" % (workday, current_time, avg_tips_perc)
        current_time = time
        current_tips_perc_sum = tips_perc
        count = 1

if current_time == time:
    avg_tips_perc = current_tips_perc_sum/count
    print "%s,%s\t%.2f" % (workday, current_time, avg_tips_perc)
