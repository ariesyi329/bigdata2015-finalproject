#!/usr/bin/python
import sys

current_zipcode = None
current_tips_sum = 0
current_fares_sum = 0


for line in sys.stdin:
    line = line.strip()
    zipcode, values = line.split('\t')
    tips, fares = values.split(',')

    try:
        tips = float(tips)
        fares = float(fares)

    except ValueError:
        pass

    if zipcode == current_zipcode:
        current_tips_sum += tips
        current_fares_sum += fares
    else:
        if current_zipcode:
            tip_percentage = current_tips_sum/current_fares_sum*100
            print "%s\t%.2f%%" % (current_zipcode, tip_percentage)
        current_zipcode = zipcode
        current_tips_sum = tips
        current_fares_sum = fares

if current_zipcode == zipcode:
    tip_percentage = current_tips_sum/current_fares_sum*100
    print "%s\t%.2f%%" % (current_zipcode, tip_percentage)
