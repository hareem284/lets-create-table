#importing sql
import sqlite3
import pandas as pd
conn=sqlite3.connect("database(1).sqlite")
print('connection is establish')
#inserting tables with constrains
conn.execute('''CREATE TABLE IF NOT EXISTS CLASS4
(SNO INTEGER PRIMARY KEY NOT NULL,
Roll_No INT NOT NULL,
Name TEXT NOT NULL,
AGE INT DEFAULT (15),
GENDER TEXT NOT NULL,
Email_ID TEXT NOT NULL,
Contact_No REAL NOT NULL);''')
print("table is created congratulation")
conn.execute("INSERT INTO CLASS4(SNO,Roll_No,Name,AGE,GENDER,Email_ID,Contact_No)\
VALUES(4, 1, 'Allen', 14, 'Male', 'allen@gmail.com', 8080900 )");
conn.execute("INSERT INTO CLASS4(SNO,Roll_No,Name,AGE,GENDER,Email_ID,Contact_No)\
VALUES(5, 2, 'Aisha', 14, 'Female', 'aish@gmail.com', 9080900)");
conn.execute("INSERT INTO CLASS4(SNO,Roll_No,Name,AGE,GENDER,Email_ID,Contact_No)\
VALUES(6, 3, 'Jeff', 15, 'Male', 'allen@gmail.com', 9900900 )");
conn.commit()
print("done")
reading=pd.read_sql("SELECT * FROM CLASS4",conn)
print(reading.head())