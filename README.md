# StockPriceSystem

StockPriceSystem is usecase implementation related to 'AAPL Stock Data' using yahoo finance Api.
in this usecase below mentioned files are there
  1. usecase.py
  2. DBConnector.py
  3. ETL.py
  4. AnsibleTask.py
  5. Apidata.py
  
1.usecase.py
---------------------
This is a main file and program flow we need to run this file. it will create graph with all entry
    Records 
    Best Day 
    Worst Day 
    Higest Price 
    Lowest Price on the graph plot.

2. DBConnector.py
-----------------------------
Mentioned file responsible for DB connections and cursors

3. ETL.py
------------------------------
Mentioned file responsible for all kind of variables like Sql Queries and others variable.

4. AnsibleTask.py
------------------------------
Mentioned file responsible for All kind of ansible task this file should be trigger by Playbook.yml (an Ansible Playbook) and done below task.
    1.  to create table, generate sample data in database
    2.  to execute code to retrieve subset (first 100 rows) of generated data from database thought "app-server" in CVS format
    3.  store gathered data on ansible server file /tmp/gathered_data.csv
    
5. Apidata.py
------------------------------
if we want we can use apidata.py file for taking data for analysis but I haven use in my usecase.



-----------------------------How to Run program--------------------------------
Set all required variable in ETL.py
cmd> python -m usecase

Result:
      plotted graph with     
    Records 
    Best Day 
    Worst Day 
    Higest Price 
    Lowest Price on the graph plot.






