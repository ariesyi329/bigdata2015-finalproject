import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import matplotlib.pyplot as plt
import pickle

def main():
    df = pickle.loads(open('OLS_data','r').read())
    df = df.sort(columns='Public2')
    y = df['Tip Perc']
    X = df[['Public Transportation Rate','Public2','const']]
    result = sm.OLS(y, X).fit()
    yhat = result.predict(X)
    prstd, iv_l, iv_u = wls_prediction_std(result)
    plt.scatter(X['Public Transportation Rate'],y,color = 'b', alpha = 0.9)
    plt.plot(X['Public Transportation Rate'],yhat, color = 'r', alpha = 0.7)
    plt.plot(X['Public Transportation Rate'], iv_u, '--', color ='r',alpha = 0.7, linewidth = 0.7)
    plt.plot(X['Public Transportation Rate'], iv_l, '--', color ='r', alpha = 0.7, linewidth = 0.7)
    plt.text(0.7, 28,'$R^2$=$%.3f$' % result.rsquared, ha='center', va='center')
    plt.xlabel('Public Transportation Rate')
    plt.ylabel('Average Tip Percentage')
    plt.title('Regress Tip Percentage on Public Transportation Rate')
    plt.show()
    #plt.savefig('PublicTrans.png', dpi = 200)

if __name__ == "__main__":
    main()



