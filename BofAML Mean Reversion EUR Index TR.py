import yfinance as yf
import pandas_market_calendars
import datetime as dt
import pandas as pd

#Undl Prices
SP500=yf.download('^GSPC',start='1994-10-26')
NASDAQ100=yf.download('^NDX',start='1994-10-26')
EUROSTOXX50=yf.download('^STOXX50E',start='1994-10-26')
FX=yf.download('EURUSD=X',start='1994-10-26')

#Get Calendar
startDate=dt.datetime(1994,10,26)
endDate=dt.datetime.now()
NASDAQ100Calendar=pandas_market_calendars.get_calendar('NYSE')
EUROSTOXX50Calendar=pandas_market_calendars.get_calendar('XSTO')
NASDAQ100Calendar=NASDAQ100Calendar.schedule(startDate,endDate)
NASDAQ100Calendar=pandas_market_calendars.date_range(NASDAQ100Calendar,frequency='1D').strftime('%Y-%m-%d')
EUROSTOXX50Calendar=EUROSTOXX50Calendar.schedule(startDate,endDate)
EUROSTOXX50Calendar=pandas_market_calendars.date_range(EUROSTOXX50Calendar,frequency='1D').strftime('%Y-%m-%d')
AllDays=pd.date_range(start=startDate,end=endDate,freq='B')
BusinessMonthEnd=pd.date_range(start=startDate,end=endDate,freq='BME')
#Intermediate Calculation
weight=1/3
NormalizationFactorSP500=100/SP500['Close'].iloc[0]
NormalizedSP500=SP500['Close']*NormalizationFactorSP500
NormalizationFactorNASDAQ100=100/NASDAQ100['Close'].iloc[0]
NormalizedNASDAQ100=NASDAQ100['Close']*NormalizationFactorNASDAQ100
NormalizationFactorEUROSTOXX50=100/EUROSTOXX50['Close'].iloc[0]
NormalizedEUROSTOXX50=EUROSTOXX50['Close']*NormalizationFactorEUROSTOXX50

NASDAQ100Calendar=pd.to_datetime(NASDAQ100Calendar)
EUROSTOXX50Calendar=pd.to_datetime(EUROSTOXX50Calendar)

for i in AllDays:
    print(i)
    if i in NASDAQ100Calendar:
        if i in EUROSTOXX50Calendar:
            pass
        else:
            print('EUROSTOXX in holiday for '+str(i))
    else:
        print('SP500/Nasdaq in holiday for '+str(i))