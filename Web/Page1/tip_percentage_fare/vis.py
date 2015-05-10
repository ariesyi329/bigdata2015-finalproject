#!/usr/bin/python
import sys
import matplotlib.pyplot as plt

tip_dict = {}

for line in sys.stdin:
    line = line.strip()
    fare, tip_perc = line.split('\t')

    try:
        fare = int(fare)
        tip_perc = float(tip_perc)
    except ValueError:
        pass

    if tip_perc < 50 and tip_perc >0 and fare >0 and fare <= 100:
        tip_dict[fare] = tip_perc

tip_dict = dict(sorted(tip_dict.iteritems()))

#print tip_dict.keys(), tip_dict.values()

# plt.figure(figsize=(8,8))
plt.plot(tip_dict.keys(),tip_dict.values(),
        color = "skyblue", linewidth=1.5)
#plt.grid(b=True, which = 'major', color='grey', linestyle='--')
#plt.grid(b=True, which = 'minor', color='grey', linestyle='--')
plt.grid(True, which='both')
plt.xlim([0,100])
#plt.minorticks_on()
plt.title("Tip Percentage VS. Fare Amounts")
plt.xlabel("Fares Amounts")
plt.ylabel("Tip Percentage")
plt.savefig('tips_perc_vs_fare.png')
plt.close()

