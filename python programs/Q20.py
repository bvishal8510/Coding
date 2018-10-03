import os
import cx_Oracle
import csv
 
SQL="SELECT * FROM SOME_TABLE"
 
# Network drive somewhere
filename="E:\Output.csv"
FILE=open(filename,"w");
output=csv.writer(FILE, dialect='excel')
 
# You can set these in system variables but just in case you didnt
os.putenv('ORACLE_HOME', '/oracle/product/10.2.0/db_1') 
os.putenv('LD_LIBRARY_PATH', '/oracle/product/10.2.0/db_1/lib') 
 
connection = cx_Oracle.connect('userid/password@127.0.0.1:PORT/SID')
 
cursor = connection.cursor()
cursor.execute(SQL)
for row in cursor:
    output.writerow(row)
cursor.close()
connection.close()
FILE.close()