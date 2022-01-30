# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 00:40:31 2022

@author: Mrinal
"""
import sqlite3

class DBConnector:
    
        
    def __init__(self,dbFile):
        self.dbFile=dbFile
        
        
    def createConn(self):
        conn = sqlite3.connect(self.dbFile)
        return conn
    
    def executeQuery(self,query):
        self.createConn().cursor()
        cursor = self.createConn()
        values=cursor.execute(query)
        return list(values)
  
     
        
    
    """
    print("-------------------------------------------")
    print(" \t\t TotalRecords :\t "+str(TotalRecords[0][0]))
    print(" \t\t BestDay for  :\t "+BestDay[0][0])
    print(" \t\t WorstDay for :\t "+WorstDay[0][0])
    print("-------------------------------------------")
    """        