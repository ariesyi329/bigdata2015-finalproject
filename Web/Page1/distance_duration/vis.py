#!/usr/bin/python
import sys
import matplotlib.pyplot as plt

ratio_dict = {}

for line in sys.stdin:
    line = line.strip()
    ratio, tip_perc = line.split('\t')

    try:
        ratio = int(ratio) #converts duration from seconds to hour
        tip_perc = float(tip_perc)
    except ValueError:
        pass

    ratio_dict[ratio] = tip_perc
    ratio_dict = dict(sorted(ratio_dict.iteritems()))

plt.figure(figsize=(8,6))
plt.plot(ratio_dict.keys(), ratio_dict.values(),  color = 'skyblue')
plt.title("Tip Percentage VS. TripDistance/Duration")
plt.xlabel("Trip Distance/Duration(mile/hour)")
plt.ylabel("Tip Percentage")
plt.xlim(1, 60) #excludes the noise
plt.ylim(15,25)
plt.grid()
plt.savefig('tips_perc_dist_duration86.png')
# plt.show()