import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# Getting Price Date
hdfc=yf.download('HDFCBANK.NS',period='5y')
tcs=yf.download('TCS.NS',period='5y')
infosys=yf.download('INFY.NS',period='5y')
reliance=yf.download('RELIANCE.NS',period='5y')

InputPricesPortfolio1=pd.merge(hdfc,tcs,on='Date',how='inner',suffixes=('_hdfc','_tcs'))
InputPricesPortfolio2=pd.merge(infosys,reliance,on='Date',how='inner',suffixes=('_infy','_reliance'))
InputPricesPortfolio1=InputPricesPortfolio1[['Adj Close_hdfc','Adj Close_tcs']]
InputPricesPortfolio2=InputPricesPortfolio2[['Adj Close_infy','Adj Close_reliance']]


dailyReturnsPort1=InputPricesPortfolio1.pct_change()
dailyReturnsPort2=InputPricesPortfolio2.pct_change()

weightPortfolio1=np.array([0.5,0.5])
weightPortfolio2=np.array([0.5,0.5])

dailyReturnsPort1['Portfolio1']=dailyReturnsPort1.dot(weightPortfolio1)
dailyReturnsPort2['Portfolio2']=dailyReturnsPort2.dot(weightPortfolio2)


dailyReturnsPort1['CumulativeReturnPortfolio1']=(1+dailyReturnsPort1['Portfolio1']).cumprod()
dailyReturnsPort1['CumulativeReturnHDFC']=(1+dailyReturnsPort1['Adj Close_hdfc']).cumprod()
dailyReturnsPort1['CumulativeReturnTCS']=(1+dailyReturnsPort1['Adj Close_tcs']).cumprod()

dailyReturnsPort2['CumulativeReturnPortfolio2']=(1+dailyReturnsPort2['Portfolio2']).cumprod()
dailyReturnsPort2['CumulativeReturnInfosys']=(1+dailyReturnsPort2['Adj Close_infy']).cumprod()
dailyReturnsPort2['CumulativeReturnReliance']=(1+dailyReturnsPort2['Adj Close_reliance']).cumprod()

portfolio1variance=dailyReturnsPort1['Portfolio1'].var()
portfolio2variance=dailyReturnsPort2['Portfolio2'].var()
portfolio1stddev=dailyReturnsPort1['Portfolio1'].std()
portfolio2stddev=dailyReturnsPort2['Portfolio2'].std()

plt.figure(figsize=(12,8))
plt.plot(dailyReturnsPort1.index,dailyReturnsPort1['CumulativeReturnPortfolio1'],label='Portfolio 1-HDFC/TCS')
plt.plot(dailyReturnsPort1.index,dailyReturnsPort1['CumulativeReturnHDFC'],label='HDFC')
plt.plot(dailyReturnsPort1.index,dailyReturnsPort1['CumulativeReturnTCS'],label='TCS')

plt.plot(dailyReturnsPort2.index,dailyReturnsPort2['CumulativeReturnPortfolio2'],label='Portfolio 2-INFY/RELIANCE')
plt.plot(dailyReturnsPort2.index,dailyReturnsPort2['CumulativeReturnInfosys'],label='Infosys')
plt.plot(dailyReturnsPort2.index,dailyReturnsPort2['CumulativeReturnReliance'],label='Reliance')
plt.title('Cumulative Returns of Portfolios with Indian Equities')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.grid(True)
plt.show()





