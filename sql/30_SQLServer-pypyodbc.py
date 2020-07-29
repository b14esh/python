# ставим модуль pypyodbc
# ставим SQL Server 2016 express edition(бесплатная версия)
# https://github.com/Microsoft/sql-server-samples/tree/master/samples/databases/northwind-pubs
# https://docs.microsoft.com/ru-ru/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases
# https://www.woinfo.ru/soft/ustanovka-i-podklyuchenie-k-baze-dannyx-northwind.html
# https://visualstudio.microsoft.com/ru/downloads/
# MYWIN\SQLEXPRESS - мой тестовый сервер(MYWIN) и имя инстанс SQL (SQLEXPRESS)
# northwind - база данных для обучения
# https://docs.microsoft.com/ru-ru/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver15

import pypyodbc

mySQLServer = "MYWIN\SQLEXPRESS"
myDatabase = "northwind"

#connection = pypyodbc.connect(driver='{SQL Server}', server='localhost', database='test', uid='user', pwd='password')
# Если не указываем uid и pwd будут использоватся учетные данные пользователя запустившего скрипт
#connection = pypyodbc.connect(driver='{SQL Server}', server='MYWIN\SQLEXPRESS', database='Northwind')

connection = pypyodbc.connect(driver='{SQL Server}', server= mySQLServer, database= myDatabase)


cursor = connection.cursor()

mySQLQuery = (""" 
                 SELECT CompanyName, ContactName, country
                 FROM dbo.Customers
                 WHERE country = 'USA'
              """)

cursor.execute(mySQLQuery)
results = cursor.fetchall()

#print(results)
for row in results:
    companyname = row[0]
    contactname = row[1]
    contryname  = row[2]
    #print("Welcome: " + str(companyname) + "User:" + str(contactname) + "Frome: " + str(contryname))
    print(f"Welcome: {companyname} User: {contactname} From: {contryname} ")



connection.close