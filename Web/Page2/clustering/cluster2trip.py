import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
plt.style.use('dark_background')

def main():
    c0 = pickle.loads(open('cluster2dist','r').read())
    c0=c0.drop(['weekend','workday'],1)
    c0.columns = ['weekend','workday']
    c0.plot(kind='area',color=['orange','deepskyblue'],alpha=0.6, figsize=(18,6), stacked=False)
    plt.xticks(rotation=0)
    plt.xlabel('Pickup Time')
    plt.ylabel('Daily Trip Amount')
    #plt.show()
    plt.savefig('cluster2trip-black.png',dpi=200)

if __name__ == "__main__":
    main()
