import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pickle

def main():
    df = pickle.loads(open('threefactors','r').read())
    f = plt.figure(figsize=(8, 5)) 
    df.plot(ax=f.gca(), kind='scatter', x='Median household income', y='Tip Perc', c='White', edgecolor=df['Clusters'], s=df['Public Transportation Rate']*300)
    plt.text(167500, 19, 'White Rate', ha='center', va='center',rotation=-90)
    plt.text(102000, 14.8, '0.2', ha='center', va='center')
    plt.text(115000, 14.8, '0.5', ha='center', va='center')
    plt.text(128000, 14.8, '0.8', ha='center', va='center')
    plt.text(115000, 13, 'Public Trans Rate', ha='center', va='center')
    plt.ylabel('Tip Percentage')
    plt.xlabel('Median Household Income ($)')
    plt.show()
    #plt.savefig('threefactors.png', dpi=200)

if __name__ == "__main__":
    main()

