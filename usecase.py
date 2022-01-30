import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from DBConnector import DBConnector
from ETL import ETL as Query
from ETL import Variables as vb
#from Apidata import Apidata #Can be use Api Data for Dataframe

start=vb.start #'2021-01-01'
end= vb.end    #'2021-12-31'
stock=vb.stock #'AAPL'
database = vb.database #"C:\\Users\\sneha\\Desktop\\findata.db"



DC=DBConnector(database)


fin_df = yf.download(stock, 
                      start, 
                      end, 
                      progress=False,
)



fin_df.to_sql(name='findata', con=DC.createConn(),if_exists='replace' )



plotData = pd.read_sql_query("SELECT * from findata", DC.createConn())
plotData.set_index("Date",inplace=True)
TotalRecords=DC.executeQuery(Query.TotalRecs)
BestDay=DC.executeQuery(Query.BestDay)
WorstDay=DC.executeQuery(Query.WorstDay)



try:
    rng=pd.date_range(start,periods=12,freq="M")
    plt.ylabel('Price')
    plt.title(stock+' STOCKS PLOT')
    plt.figtext(.3, .8, "Records : "+str(TotalRecords[0][0]))
    plt.figtext(.4, .8, "Best Day : "+str(BestDay[0][0]))
    plt.figtext(.54, .8, "Worst Day : "+str(WorstDay[0][0]))
    plt.figtext(.4, .7, "Higest Price : "+str(BestDay[0][1]))
    plt.figtext(.4, .65, "Lowest Price : "+str(WorstDay[0][1]))
    
    plotData.truncate(before=start, after=end)['Open'].plot(legend=True,figsize=(17,10))
    plotData.truncate(before=start, after=end)['Low'].plot(legend=True,figsize=(17,10))
    plotData.truncate(before=start, after=end)['High'].plot(legend=True,figsize=(17,10))    
    plotData.truncate(before=start, after=end)['Close'].plot(legend=True,figsize=(17,10))
    plotData.truncate(before=start, after=end)['Adj Close'].plot(legend=True,figsize=(17,10))
except:
    print("error occured")












