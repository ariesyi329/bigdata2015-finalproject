#!/usr/bin/python
import sys
import matplotlib.pyplot as plt

tip_dict = {}

for line in sys.stdin:
    line = line.strip()
    month, count = line.split('\t')

    try:
        month = int(month)
        count = int(count) / 1000000
        tip_dict[month] = count
    except ValueError:
        pass
        

tip_dict = dict(sorted(tip_dict.iteritems()))

#print tip_dict.keys(), tip_dict.values()

plt.figure(figsize = (8,6))
plt.bar(tip_dict.keys(),tip_dict.values(), width = 0.6, color = "skyblue")
# plt.grid(b=True, which = 'major', color='grey', linestyle='--')
# plt.grid(b=True, which = 'minor', color='grey', linestyle='--')
plt.grid(True, which='both')
plt.ylim([0, 10])
# plt.minorticks_on()
plt.title("Trip VS. month")
plt.xlabel("Month")
plt.ylabel("Trip count (million)")
plt.savefig('trip_vs_month86.png')
plt.show()
plt.close()

