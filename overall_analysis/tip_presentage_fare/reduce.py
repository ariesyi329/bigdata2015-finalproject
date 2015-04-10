#!/usr/bin/python
import sys

current_fares = None
current_tips_sum = 0
current_fares_sum = 0


for line in sys.stdin:
    line = line.strip()
    fares, tips = line.split('\t')

    try:
        tips = float(tips)
        fares = float(fares)
        int_fares = int(fares)
    except ValueError:
        pass

    if int_fares == current_fares:
        current_tips_sum += tips
        current_fares_sum += fares
    else:
        if current_fares:
            tip_percentage = current_tips_sum/current_fares_sum*100
            print "%d\t%.2f%%" % (current_fares, tip_percentage)
        current_fares = int_fares
        current_tips_sum = tips
        current_fares_sum = fares

if current_fares == int_fares:
    tip_percentage = current_tips_sum/current_fares_sum*100
    print "%d\t%.2f%%" % (current_fares, tip_percentage)
