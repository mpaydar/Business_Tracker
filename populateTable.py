import sqlite3


connection=sqlite3.connect('db.sqlite3')
cursor=connection.cursor()

insert_companies_query='''




INSERT INTO COMPANIES (COMPANYID,NAME) 
VALUES
(1,'Walmart'),
(2,'COSTCO'),
(3, 'TARGET');

'''


#     companies=['Walmart','COSTCO','TARGET']
#     national_holidays=['New Year Day','Easter','Memorial','Independence','Labor','Thanksgiving','Christmas']
insert_holiday_query='''INSERT INTO HOLIDAY (HOLIDAYID,COMPANYID,HOLIDAYNAME) VALUES 
(1,1,'New Year'),
(2,1,'Easter'),
(3,1,'Memorial'),
(4,1,'Independence'),
(5,1,'Labor'),
(6,1,'Thankgiving'),
(7,1,'Christmas'),

(1,2,'New Year'),
(2,2,'Easter'),
(3,2,'Memorial'),
(4,2,'Independence'),
(5,2,'Labor'),
(6,2,'Thankgiving'),
(7,2,'Christmas'),


(1,3,'New Year'),
(2,3,'Easter'),
(3,3,'Memorial'),
(4,3,'Independence'),
(5,3,'Labor'),
(6,3,'Thankgiving'),
(7,3,'Christmas');

'''


# def generate_holiday_query(base_template):
#     revise_holiday=''
#     companies=['Walmart','COSTCO','TARGET']
#     national_holidays=['New Year Day','Easter','Memorial','Independence','Labor','Thanksgiving','Christmas']
#     for companies_index in range(len(companies)):
#         for holiday_index in range(len(national_holidays)):
#             base_template+=f'({holiday_index+1},{companies_index+1},{national_holidays[holiday_index]}),'
#     revise_holiday=base_template[0:len(base_template)-1] + ';'
#     return revise_holiday

# r=generate_holiday_query(insert_holiday_query)

# cursor.execute(insert_companies_query)
# connection.commit()


cursor.execute(insert_holiday_query)
connection.commit()



connection.close()