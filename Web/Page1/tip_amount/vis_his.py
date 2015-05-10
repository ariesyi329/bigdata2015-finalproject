#!/usr/bin/python
import sys
import matplotlib.pyplot as plt
import pickle

tip_list = []

for line in sys.stdin:
    line = line.strip()
    tip, amount = line.split('\t')

    try:
        tip = float(tip)
    except ValueError:
        pass
    
    #if tip < 15:
    tip_list.append(tip)


plt.hist(tip_list,bins=5000, color='skyblue',edgecolor='w',alpha=0.7)
plt.title("Tip Amount Distribution")
plt.xlim([0,10])
plt.xlabel('Amount')
plt.ylabel('Count')

plt.savefig('tip_hist.png')

