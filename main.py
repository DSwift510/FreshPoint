# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import inheritance.py
#import heatmap.py
#import insert.py
import mysql.connector
from mysql.connector import (connection, errorcode)
# mysql.connector.connect(host='localhost',port='3309',database='ufoods',user='root',password='aggi3pride')


def query_with_fetchone():
    try:
        dbconnect = mysql.connector.connect(host='localhost',port='3309',database='ufoods',user='root',password='aggi3pride')
        # print("hello")
        cursor = dbconnect.cursor(buffered=True)
        cursor.execute("SELECT * FROM ufoods.producemasterlist LIMIT 100")
        # print("hello")
        for col in cursor:
            print(col)
            
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
     cursor.close()
     dbconnect.close()

    #finally:
    
        
if __name__ == '__main__':
    query_with_fetchone()