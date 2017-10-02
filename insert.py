# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 20:15:08 2017

@author: Dasani
"""

import mysql.connector
import re
import xlrd
import datetime
import csv
from mysql.connector import (connection)

dbconnect = mysql.connector.connect(host='localhost',port='3309',database='ufoods',user='root',password='aggi3pride')
Saleshist = []
cursor = dbconnect.cursor(buffered=True)
#cursor.execute("""INSERT INTO ufoods.foodfight VALUES (%s,%s,%s)""",(3,543,765))
book = xlrd.open_workbook("C:/Users/Dasani/Desktop/output.xlsx")
sheet = book.sheet_by_name("Sheet1")
#current time and day
#timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
for r in range(1, sheet.nrows):
      product      = sheet.cell(r,3).value
      customer = sheet.cell(r,1).value
      rep          = sheet.cell(r,0).value
      re.sub('[^A-Za-z0-9]+', '', product)
      re.sub('[^A-Za-z0-9]+', '', customer)
      re.sub('[^A-Za-z0-9]+', '', rep)
      print("running")

      # Assign values from each row
      values = (product, customer, rep)

      cursor.execute("INSERT INTO ufoods.foodfight VALUES (%s,%s,%s)",(product, customer, rep))

dbconnect.commit()

cursor.execute("SELECT * FROM ufoods.foodfight;")
result=cursor.fetchall()
myfile =open("C:/Users/Dasani/Desktop/test.csv","w")
c = csv.writer(myfile)
for row in result:
    print(row)
    c.writerow(row)
myfile.close()
dbconnect.close()