# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 10:29:43 2017

@author: Dasani
"""

"""CREATE TEMPORARY TABLE combo
SELECT complete_freshpoint.SProductID,complete_freshpoint.Not_Local, monthname(complete_freshpoint.Month_Year) as Month, complete_freshpoint.Cases_Sold, fruit_vegetable_table.Food, fruit_vegetable_table.January, fruit_vegetable_table.February, fruit_vegetable_table.March, fruit_vegetable_table.April, fruit_vegetable_table.May, fruit_vegetable_table.June, fruit_vegetable_table.July, fruit_vegetable_table.August, fruit_vegetable_table.September, fruit_vegetable_table.October, fruit_vegetable_table.November, fruit_vegetable_table.December
FROM complete_freshpoint
INNER JOIN fruit_vegetable_table ON complete_freshpoint.SProductID = fruit_vegetable_table.ProductID
WHERE complete_freshpoint.Not_Local = 0
ORDER BY fruit_vegetable_table.Food;"""

"""statement = CREATE TEMPORARY TABLE combo
SELECT complete_freshpoint.SProductID,complete_freshpoint.Not_Local, monthname(complete_freshpoint.Month_Year) as Month, complete_freshpoint.Cases_Sold
FROM complete_freshpoint
WHERE complete_freshpoint.Not_Local = 0;"""


import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns
import numpy as np
import pandas as pd


fpCases = 0
fvtCases = 0
locality = 0
available=[]
fpMonth=''
fpProduct=''
fvtMonth=''
fvtProduct=''
ind=0
dbconnect = mysql.connector.connect(host='localhost',port='3306',database='warrenwilson',user='django',password='aggieprid3')
cursor = dbconnect.cursor(buffered=True)

#################################################################################
statement = """select warrenwilson.wwgoodmapfull.MY, warrenwilson.wwgoodmapfull.Cases, warrenwilson.wwgoodmapfull.foodtype, warrenwilson.wwgoodmapfull.Local from warrenwilson.wwgoodmapfull GROUP BY warrenwilson.wwgoodmapfull.foodtype, warrenwilson.wwgoodmapfull.productid, warrenwilson.wwgoodmapfull.MY;"""


def setGoodMap(cursor):
    cursor.execute("""DROP TEMPORARY TABLE IF EXISTS warrenwilson.wwgoodmapfull;""")
    cursor.execute(statement)

    rows = cursor.fetchall()
    goodMap = pd.DataFrame( [[ij for ij in i] for i in rows] )
    #NIFVT.rename(columns={0: 'Date Purchased', 1: 'Cases Sold', 2: 'Product', 3: 'ProductID'}, inplace=True);
    goodMap.rename(columns={ 0:'Month',1: 'Cases Sold', 2: 'Product', 3: 'Locality'}, inplace=True);
    #print (goodMap)

    cursor.execute("""select fruit_vegetable_table.Food, fruit_vegetable_table.January, fruit_vegetable_table.February, fruit_vegetable_table.March, fruit_vegetable_table.April, fruit_vegetable_table.May, fruit_vegetable_table.June, fruit_vegetable_table.July, fruit_vegetable_table.August, fruit_vegetable_table.September, fruit_vegetable_table.October, fruit_vegetable_table.November, fruit_vegetable_table.December from ufoods.fruit_vegetable_table order by fruit_vegetable_table.Food""")
    rows2 = cursor.fetchall()
    FVT = pd.DataFrame( [[ij for ij in i] for i in rows2] )
    FVT.rename(columns={ 0:'', 1:'January', 2:'February', 3: 'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}, inplace=True);
    transFVT = FVT.set_index('').T
    #print transFVT

    for fvtindex, fvtrow in transFVT.iterrows():

        for product in fvtrow.index:
             #print 'fvtindex: ',fvtindex,'|product: ', product,'|fvtrow[product]: ', fvtrow[product]
             fvtProduct = product
             fvtMonth = fvtindex
             fvtAvailability = fvtrow[product]
             #print fvtProduct, ' / ', fvtMonth

             outer = matchFVT2FP(fvtProduct,fvtMonth,fvtrow,goodMap,transFVT)
             if outer == 0 and fvtAvailability == 0:
                #print (";") 
                available.append(0)
             if outer == 0 and fvtAvailability == 1:
                #print("+")
                available.append(1)

    #print available
    hm = pd.DataFrame(np.array(available).reshape(12,59), columns =list(transFVT.columns),index=list(transFVT.index))
    #print hm
    plt.figure(figsize=(20,8))
    plt.ylabel('y',rotation='vertical')
    hmFinish = sns.heatmap(hm,linecolor='black',cmap=ListedColormap(['None', 'grey','green','pink']),square=True,linewidth=.5)
    loc, labels = plt.xticks(fontsize=8, rotation=75)    #hmFinish.xaxis.tick_top()
    cbar = hmFinish.collections[0].colorbar
    cbar.set_ticks([.4,1.15,1.85,2.62])
    cbar.set_ticklabels(['Seasonally Unavailable, No purchase','Seasonally Available, No Purchase','Seasonally Available, Local Purchase','Seasonally Unavailable, Azonic Purchase'])
    plt.suptitle('Seasonal Improvement Opportunities', fontsize=16, x=.45)
    plt.savefig("""/Users/Dasani/Desktop/WW_goodmap.png""", dpi = 200)
    plt.tight_layout()
    plt.show()



def matchFVT2FP(fvtProduct,fvtMonth,fvtrow,goodMap,transFVT):
    inner=0
    global localCount
    for fpindex, fprow in goodMap.iterrows():
        fpMonth = fprow['Month']
        fpCases = fprow['Cases Sold']
        fpProduct = fprow['Product']
        fpLocality = fprow['Locality']
        #print ('fvtProduct: ', fvtProduct, ' fpProduct: ', fpProduct, '| fpMonth: ', fpMonth, ' fvtMonth: ', fvtMonth, '| fpCases: ', fpCases, '\n')

        if fpMonth == fvtMonth and fpProduct == fvtProduct:
            inner+=1
            if fpCases > 0.0:

                    if fvtrow[fvtProduct] == 0.0 and fpLocality == 1:
                        available.append(3)
                        #print ("/")
                    elif fvtrow[fvtProduct] == 1.0 and fpLocality == 0:
                        available.append(2)
                        #print (".")
                    else:
                        available.append(0)
                        break

                        
            elif fvtrow[fvtProduct] == 1.0:
                #print fprow
                print (fpCases)
                available.append(1)
            else:
                #print(",")
                available.append(0)
    #print available, '|'
    return inner







setGoodMap(cursor)
dbconnect.close()
