#!/usr/bin/python
import sys

current_time = None
current_tips_sum = 0
current_fares_sum = 0


for line in sys.stdin:
    line = line.strip()
    time, values = line.split('\t')
    tips, fares = values.split(',')

    try:
        tips = float(tips)
        fares = float(fares)
        int_fares = int(fares)

    except ValueError:
        pass

    if time == current_time:
        current_tips_sum += tips
        current_fares_sum += fares
    else:
        if current_time:
            tip_percentage = current_tips_sum/current_fares_sum*100
            print "%s\t%.2f%%" % (current_time, tip_percentage)
        current_time = time
        current_tips_sum = tips
        current_fares_sum = fares

if current_time == time:
    tip_percentage = current_tips_sum/current_fares_sum*100
    print "%s\t%.2f%%" % (current_time, tip_percentage)
