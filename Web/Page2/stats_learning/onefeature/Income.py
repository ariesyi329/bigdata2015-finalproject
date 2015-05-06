import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import matplotlib.pyplot as plt
import pickle

def main():
    df = pickle.loads(open('OLS_data','r').read())
    df = df.sort(columns='Median household income')
    y = df['Tip Perc']
    X = df[['Median household income','Income2','const']]
    result = sm.OLS(y, X).fit()
    yhat = result.predict(X)
    prstd, iv_l, iv_u = wls_prediction_std(result)
    plt.scatter(X['Median household income'],y,color = 'b', alpha = 0.9)
    plt.plot(X['Median household income'],yhat, color = 'r', alpha = 0.7)
    plt.plot(X['Median household income'], iv_u, '--', color ='r',alpha = 0.7, linewidth = 0.7)
    plt.plot(X['Median household income'], iv_l, '--', color ='r', alpha = 0.7, linewidth = 0.7)
    plt.text(125000, 24.5,'$R^2$=$%.3f$' % result.rsquared, ha='center', va='center')
    plt.xlabel('Median Household Income ($)')
    plt.ylabel('Average Tip Percentage')
    plt.title('Regress Tip Percentage on Median Household Income')
    plt.show()
    #plt.savefig('Income.png', dpi = 200)

if __name__ == "__main__":
    main()



