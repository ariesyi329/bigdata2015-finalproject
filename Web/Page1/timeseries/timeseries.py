import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

def main():
    timeseries_df = pickle.loads(open('data_timeseries','r').read())
    timeseries_df.plot(color=['skyblue','gold'])
    plt.ylim([18.5,21.5])
    plt.xlabel('Pickup Time')
    plt.ylabel('Tip Percentage')
    plt.show()
    #plt.savefig('timeseries.png', dpi=200)

if __name__ == "__main__":
    main()

