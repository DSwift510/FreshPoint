# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 00:58:10 2017

@author: Dasani
"""

import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
import pprint as pp
import numpy as np
import pandas as pd
dbconnect = mysql.connector.connect(host='localhost',port='3309',database='ufoods',user='root',password='aggi3pride')
produce_dict = {}   #lookup dictionary for product id
reverse_produce_dict={} #lookup dictionary for description
produce_row_dict ={} #lookup dictionary of product id and matrix rows
Saleshist = [] 
cursor = dbconnect.cursor(buffered=True)
default = 9999

def construct_plural_string(word):
    if word[-1] == 'O':
        return word.upper()+'ES'
    elif word[-1] == 'Y':
        return word.upper()[0:-1]+'IES'
    else:
        return word.upper()+'S'
        
def check_string(word,produce_dict):
    value = produce_dict.get(word.upper(),default)
    if value == default:    
        pluralword = construct_plural_string(word)
        value = produce_dict.get(pluralword,default)
    return value



#TODO: needs own method 
def createDict(cursor):
    cursor.execute("SELECT Food, ProductID FROM ufoods.producemasterlist;")
    rownum=0
    for row in cursor.fetchall():
        #print(row)
        
        produce_dict[str(row[0].strip())] = int(row[1])
        reverse_produce_dict[int(row[1])] = str(row[0].strip())
        produce_row_dict[int(row[1])] = rownum
        rownum += 1
    print("\nProd Dict")    
    #pp.pprint(produce_dict.items())  
    print("\nrProd Dict") 
    #pp.pprint(reverse_produce_dict.items())  
    print("\nProd Row Dict") 
    #pp.pprint(produce_row_dict.items())
    #getSalesHist(cursor)

#TODO: needs own method
def getSalesHist(cursor):
    print('\nFETCHING DATA FROM COMPLETE FRESHPOINT TABLE\n')
    cursor.execute("SELECT Complete_Freshpoint.ID, Complete_Freshpoint.Supplier, Complete_Freshpoint.Description, Complete_Freshpoint.Month_year, Complete_Freshpoint.Cases_Sold, Complete_Freshpoint.Sales_Dollars, Complete_Freshpoint.LocalFlag FROM Complete_Freshpoint")
    for row in cursor.fetchall():
        Saleshist.append(list(row))
        #pp.pprint(Saleshist)

#TODO: needs own method
def setSalesHist(): 
    print('CHECKING DESCRIPTIONS IN PO HISTORY')
    for rowidx, row in enumerate(Saleshist):
        newstr = row[2].strip().split(' ')   #save item description as a list of strings
        for words in newstr:
            value = check_string(words.upper(),produce_dict)
            if value !=default:      #match found
                break
            Saleshist[rowidx].append(value)
            #pp.pprint(Saleshist)

#TODO: needs own method 
def getFVT(cursor):
    A_Matrix = np.zeros((len(produce_dict),12))
    Cases_Matrix = np.zeros((len(produce_dict),12))
    cursor.execute("SELECT * FROM Fruit_Vegetable_Table")
    ctr = 0
    for row in cursor.fetchall():
        results = [int(i) for i in list(row[2:-1])]
        print("""results = """, results)
        A_Matrix[ctr]=results
        ctr+=1
    
    print(A_Matrix)
    getNonLocal(A_Matrix,Cases_Matrix,cursor)
    #getLocal(A_Matrix,Cases_Matrix,cursor)
#TODO: needs own method 
def getNonLocal(A_Matrix, Cases_Matrix,cursor):
    #cursor.execute("SELECT * FROM Complete_Freshpoint WHERE LocalFlag = %s",['NotLocal'])
    cursor.execute("SELECT * FROM Complete_Freshpoint WHERE Not_local = 1")
    for row in cursor.fetchall():
        if row[3] is not None:
            rowid = produce_row_dict.get(row[-1],default) 
            if rowid !=default:
                colid = row[3].month 
                Cases_Matrix[rowid,colid-1] += row[5]
    #setDimensions(Cases_Matrix)
    getLocal(A_Matrix, Cases_Matrix, cursor)
    
#TODO: Create Temporary Table adding Local value to Complete_Freshpoints creating 3d array (dataframe) 
def getLocal(A_Matrix, Cases_Matrix, cursor):
    cursor.execute("SELECT * FROM Complete_Freshpoint WHERE Not_local = 0")
    for row in cursor.fetchall():
        if row[3] is not None:
            rowid = produce_row_dict.get(row[-1],default) 
            if rowid !=default:
                colid = row[3].month 
                Cases_Matrix[rowid,colid-1] += row[5]
    setDimensions(Cases_Matrix)

def setDimensions(Cases_Matrix):                     
    print('Saving Cases Matrix')
    print(Cases_Matrix[0,8])
    np.savetxt('CasesSold',Cases_Matrix,delimiter = ",")
    print(produce_row_dict)
    print('flattening cases matrix')
    CasesFlat = list(Cases_Matrix.flatten('C'))  #convert to 1d array
    Months = ['Jan', 'Feb','Mar','Apr','May','June','Jul', 'Aug','Sep','Oct','Nov','Dec']*len(produce_dict)
    setProductList(Months,CasesFlat)
#TODO: needs own method 
#build product list
def setProductList(Months,CasesFlat):
    Prods=[]

    for key in produce_row_dict:
        print("Key is ", key)
        desc = reverse_produce_dict.get(key,'NONE')
        desclist = [desc]*12
        Prods.extend(desclist)    

    #print(reverse_produce_dict)
    print(Prods)
    df2=pd.DataFrame({'Months':Months,'Prods':Prods,'Values':CasesFlat})
    print("\ndf2\n")
    print(df2)
    #addDimension(df2, cursor)
    
    #saveDataToExel(df2)
    #df2 = df2[1].fillna(0,inplace=True)
    #showGraph(df2)
    #TODO: needs own method

def showGraph(df2):

    ##### print heatmap
    sns.heatmap(df2, annot=True)
    #plt.show()


#TODO: needs own method
def saveDataToExel(df2):
## write data frame to excel file
    writer = pd.ExcelWriter('output.xlsx')
    df2.to_excel(writer,'Sheet1')
    writer.save()


#dbconnect.close()

if __name__ == '__main__':
    createDict(cursor)
    #setSalesHist()
    #getFVT(cursor)
    #getLocal()
dbconnect.close()


