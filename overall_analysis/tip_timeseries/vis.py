#!/usr/bin/python
import sys
import matplotlib.pyplot as plt

time_list=[]
tip_list=[]

for line in sys.stdin:
    line = line.strip()
    time, tips_perc = line.split('\t')

    try:
        tips_perc = float(tips_perc[:-1])
        time = int(time)
    except ValueError:
        pass

    time_list.append(time)
    tip_list.append(tips_perc)

plt.plot(time_list,tip_list,
        color = "skyblue",linewidth=1.5)
plt.title("Tip Percentage VS. Pickup Time")
plt.xlabel("Pickup Time")
plt.ylabel("Tip Percentage")
plt.xlim(0,23)
plt.grid()
plt.savefig('../results/tips_perc_pickuptime.png')
#plt.show()

