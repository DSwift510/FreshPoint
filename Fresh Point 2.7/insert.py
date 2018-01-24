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



filename = raw_input("Enter Excel file class path to be added to Complete Freshpoint: ")
book = xlrd.open_workbook(filename)
sheetname = raw_input("Enter the name of the Excel Sheet to be used: ")
sheet = book.sheet_by_name(sheetname)


for r in range(1, sheet.nrows):
      supplier      = sheet.cell(r,0).value
      description   = sheet.cell(r,1).value
      year          = sheet.cell(r,2).value
      month         = sheet.cell(r,3).value
      casessold     = sheet.cell(r,4).value
      salesdollars  = sheet.cell(r,5).value
      local         = sheet.cell(r,6).value
      seasonality   = sheet.cell(r,7).value
      
      
      
      print("running")

      # Assign values from each row
      #values = (product, customer, rep)

#      cursor.execute("INSERT INTO ufoods.foodfight VALUES (%s,%s,%s,%s,%s,%s)",(product, customer, rep))

dbconnect.commit()

cursor.execute("SELECT * FROM ufoods.foodfight;")
#result=cursor.fetchall()
#myfile =open("C:/Users/Dasani/Desktop/test.csv","w")
#c = csv.writer(myfile)
#for row in result:
#    print(row)
#    c.writerow(row)
#myfile.close()
dbconnect.close()