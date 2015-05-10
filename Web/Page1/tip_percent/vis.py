#!/usr/bin/python
import sys
import matplotlib.pyplot as plt

tip_perc_list = []

for line in sys.stdin:
    line = line.strip()
    tip_perc, amount = line.split('\t')

    try:
        tip_perc = float(tip_perc)
        tip_perc_list.append(tip_perc)
    except ValueError:
        pass

	

plt.hist(tip_perc_list,bins=100000,color='skyblue',edgecolor='w',alpha=0.7)
plt.title("Tip Percentage Distribution")
plt.xlim([0,50])
plt.xlabel('Tip Percentage')
plt.ylabel('Count')

plt.savefig('tip_perc_hist.png')

