# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 06:34:07 2017

@author: Dasani
"""
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
import pprint as pp
import numpy as np
import pandas as pd
#bought = {"prodid":{"cases":"local"}}
#dataframe= {}
#for key in bought.iterkeys():
#    print key
#    for values in bought.itervalues():
#        print values
        #dataframe += {key:item} 
        
prodid = 1242
cases = 43
local = 1
dic = {0:1,5:0,44.0:1}
bought = {prodid:dic} #Lookup dictionary of productid, cases, and Not_local
    
availability = []
    #Need to scroll through rows. if cases check local
    ####
    #####
    ######
    #
#for prodid, clList in bought.iteritems():    
    #print prodid
    #print clList
        
 
#availability.append(1)
#availability.append(2)
#print availability
#availability.append(0)
#print availability
#####################

dbconnect = mysql.connector.connect(host='localhost',port='3309',database='ufoods',user='root',password='aggi3pride')
cursor = dbconnect.cursor(buffered=True)

#################################################################################

def setTempTable(cursor):
    cursor.execute("CREATE TEMPORARY TABLE combo as (SELECT complete_freshpoint.Month_Year, complete_freshpoint.Description, complete_freshpoint.Cases_Sold,complete_freshpoint.Not_Local FROM ufoods.complete_freshpoint)")
    cursor.execute("SELECT * FROM combo")
    Locality = []
    Months = []
    Products = []
    casesSold = []
    df = pd.DataFrame({'Months':Months,'Prods':Products,'Values':casesSold,'Locality':Locality})
    for row in cursor.fetchall():
        #print row
        Local = row[3]
        Cases = row[2]
        print Local, Cases
        if Local < 0 or row[2] <0:
                print "error caused by negative locality number"
                # break
        if Cases == 0:
            #locality will be 0
            Locality.append(0)
        if Cases > 0 and Local == 1:
            #locality will be 1
            Locality.append(1)
        if Cases > 0 and Local == 0:
            #locality will be 2 
            Locality.append(2)
            
    print Locality       
    
    
    #TODO: Add 4 needed attributes to dataframe. Add heatmap to dataframe
    df = pd.DataFrame({'Months':Months,'Prods':Products,'Values':casesSold,'Locality':Locality})
    sns.heatmap(df2, annot=True)
    
    
    
            
setTempTable(cursor)
dbconnect.close()