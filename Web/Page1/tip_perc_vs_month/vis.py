#!/usr/bin/python
import sys
import matplotlib.pyplot as plt

tip_dict = {}

for line in sys.stdin:
    line = line.strip()
    month, tip_perc = line.split('\t')

    try:
        month = int(month)
        tip_perc = float(tip_perc)
    except ValueError:
        pass

    if tip_perc < 50 and tip_perc >0:
        tip_dict[month] = tip_perc

tip_dict = dict(sorted(tip_dict.iteritems()))

#print tip_dict.keys(), tip_dict.values()

plt.figure(figsize=(8,8))
plt.plot(tip_dict.keys(),tip_dict.values(),'-o', ms=8, color = 'skyblue')
# plt.grid(b=True, which = 'major', color='grey', linestyle='--')
# plt.grid(b=True, which = 'minor', color='grey', linestyle='--')
plt.grid(True, which='both')
plt.ylim([19,21])
# plt.minorticks_on()
plt.title("Tip Percentage VS. month")
plt.xlabel("month")
plt.ylabel("Tip Percentage %")
plt.savefig('tips_perc_vs_month88.png')
plt.close()

