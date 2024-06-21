


import sqlite3
connection=sqlite3.connect('db.sqlite3')
cursor =  connection.cursor()

companies_table ='''
CREATE TABLE COMPANIES (
    COMPANYID INTEGER PRIMARY KEY,
    NAME VARCHAR (100) NOT NULL
)
'''

holiday_table = '''
CREATE TABLE HOLIDAY (
    HOLIDAYID INTEGER  NOT NULL,
    COMPANYID INTEGER  NOT NULL,
    HOLIDAYNAME VARCHAR (100) NOT NULL, 
    PRIMARY KEY (HOLIDAYID, COMPANYID),
    FOREIGN KEY (COMPANYID) REFERENCES COMPANY (COMPANYID)
)

'''
cursor.execute(companies_table)
connection.commit()
cursor.execute(holiday_table)
connection.commit()
connection.close()
