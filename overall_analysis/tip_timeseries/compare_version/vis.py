#!/usr/bin/python
import sys
import matplotlib.pyplot as plt

time_list_wed=[]
tip_list_wed=[]
time_list_sun=[]
tip_list_sun=[]

for line in sys.stdin:
    line = line.strip()
    datetime, tips_perc = line.split('\t')

    try:
        tips_perc = float(tips_perc[:-1])
        date = datetime[-5:-3]
        time = datetime[-2:]
        time = int(time)
    except ValueError:
        pass

    if date == '04':
        time_list_sun.append(time)
        tip_list_sun.append(tips_perc)
    else:
        time_list_wed.append(time)
        tip_list_wed.append(tips_perc)

plt.plot(time_list_sun,tip_list_sun,
        color = "skyblue",linewidth=1.5,
        label='Sunday')
plt.plot(time_list_wed,tip_list_wed,
        color = 'gold', linewidth=1.5,
        label='Wednesday')
plt.title("Tip Percentage VS. Pickup Time")
plt.xlabel("Pickup Time")
plt.ylabel("Tip Percentage")
plt.xlim(0,23)
plt.grid()
plt.legend(loc=2)
plt.savefig('../../results/tips_perc_pickuptime_twodays.png')
#plt.show()

