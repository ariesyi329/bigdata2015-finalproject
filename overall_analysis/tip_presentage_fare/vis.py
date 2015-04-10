#!/usr/bin/python
import sys
import matplotlib.pyplot as plt

tip_dict = {}

for line in sys.stdin:
    line = line.strip()
    fares, tips_perc = line.split('\t')

    try:
        fares = int(fares)
        tips_perc = float(tips_perc[:-1])
    except ValueError:
        pass

    if tips_perc < 50 and fares < 101:
        
        tip_dict[fares] = tips_perc

#tip_dict = dict(sorted(tip_dict.iteritems()))

#print tip_dict.keys(), tip_dict.values()

plt.plot(tip_dict.keys(),tip_dict.values(),
        color = "skyblue", linewidth=1.5)
#plt.grid(b=True, which = 'major', color='grey', linestyle='--')
#plt.grid(b=True, which = 'minor', color='grey', linestyle='--')
plt.grid(True, which='both')
#plt.minorticks_on()
plt.title("Tip Percentage VS. Fares Amounts")
plt.xlabel("Fares Amounts")
plt.ylabel("Tip Percentage")
plt.savefig('../results/tips_perc.png')

