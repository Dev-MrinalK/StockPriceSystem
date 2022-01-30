# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 04:57:43 2022

Ansible Script

@author: Mrinal
"""

import pandas as pd
import yfinance as yf
import sqlite3
from sqlalchemy import create_engine, MetaData, Table, Column, Integer,Numeric, String,Date
from ETL import ETL as Query
from ETL import Variables as vb


start=vb.start #'2021-01-01'
end= vb.end    #'2021-12-31'
stock=vb.stock #'AAPL'
database = vb.database # can be use instead of DataDB

Path='C:\\Users\\sneha\\Desktop\\'
engine = create_engine('sqlite:///DataDB.db', echo = False)
conn = sqlite3.connect(Path+'DataDB.db')
meta = MetaData()
fin_df = yf.download(stock, 
                      start, 
                      end, 
                      progress=False,
)

FinanceData = Table(
   'FinanceData', meta, 
   Column('Date', Date), 
   Column('Open', Numeric), 
   Column('High', Numeric),
   Column('Low', Numeric), 
   Column('Close', Numeric),
   Column('Adj Close', Numeric), 
   Column('Volume', Numeric),
   
)
meta.create_all(engine)

fin_df.to_sql(name='FinanceData', con=engine,if_exists='replace' )
db_df = pd.read_sql_query("SELECT * FROM FinanceData LiMIT 100", conn)
db_df.to_csv(Path+'gathered_data.csv', index=False)

    

