

class ETL:
    
    TotalRecs='''
                select count(*) from findata
             '''
    BestDay='''
                select date(Date),HIGH as BestDay from findata 
                where HIGH=(select max(HIGH) from  findata)
            '''
    WorstDay='''
                select date(Date),LOW as WorstDay from findata 
                   where LOW=(select max(LOW) from  findata)
            '''



class Variables:
    start='2010-01-01'
    end='2021-12-31'
    stock='AAPL'
    database = "..\\findata.db"









