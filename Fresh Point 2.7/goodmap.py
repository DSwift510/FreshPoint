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
dbconnect = mysql.connector.connect(host='localhost',port='3309',database='ufoods',user='root',password='aggi3pride')
cursor = dbconnect.cursor(buffered=True)

#################################################################################
statement = """select cbo3.MY, cbo3.Cases_Sold, cbo3.Food from ufoods.cbo3 GROUP BY cbo3.Food, cbo3.SProductID, cbo3.MY;"""


def setGoodMap(cursor):
    cursor.execute("""DROP TEMPORARY TABLE IF EXISTS cbo3;""")
    cursor.execute(statement)
    
    rows = cursor.fetchall()   
    goodMap = pd.DataFrame( [[ij for ij in i] for i in rows] )  
    #NIFVT.rename(columns={0: 'Date Purchased', 1: 'Cases Sold', 2: 'Product', 3: 'ProductID'}, inplace=True);
    goodMap.rename(columns={ 0:'Month',1: 'Cases Sold', 2: 'Product'}, inplace=True);
    print goodMap
    
    cursor.execute("""select fruit_vegetable_table.Food, fruit_vegetable_table.January, fruit_vegetable_table.February, fruit_vegetable_table.March, fruit_vegetable_table.April, fruit_vegetable_table.May, fruit_vegetable_table.June, fruit_vegetable_table.July, fruit_vegetable_table.August, fruit_vegetable_table.September, fruit_vegetable_table.October, fruit_vegetable_table.November, fruit_vegetable_table.December from ufoods.fruit_vegetable_table order by fruit_vegetable_table.Food""")
    rows2 = cursor.fetchall()
    FVT = pd.DataFrame( [[ij for ij in i] for i in rows2] )
    FVT.rename(columns={ 0:'', 1:'January', 2:'February', 3: 'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}, inplace=True);
    transFVT = FVT.set_index('').T
    print transFVT
    
    for fvtindex, fvtrow in transFVT.iterrows():
        
        for product in fvtrow.index:
             #print 'fvtindex: ',fvtindex,'|product: ', product,'|fvtrow[product]: ', fvtrow[product]
             fvtProduct = product
             fvtMonth = fvtindex
             #print fvtProduct, ' / ', fvtMonth
             
             outer = matchFVT2FP(fvtProduct,fvtMonth,fvtrow,goodMap,transFVT)
             if outer == 0:
                 available.append(0)
    
    #print available
    hm = pd.DataFrame(np.array(available).reshape(12,59), columns =list(transFVT.columns),index=list(transFVT.index))
    #print hm
    plt.figure(figsize=(20,10))
    hmFinish = sns.heatmap(hm,linecolor='white',linewidth=.5)
    #hmFinish.xaxis.tick_top()
    cbar = hmFinish.collections[0].colorbar
    cbar.set_ticks([0,1,2,3])
    cbar.set_ticklabels(['None Purchased When Not Local','None Purchased When Local','Purchased When Not Local','Purchased When Local'])
    plt.savefig("""C:/Users/Dasani/Desktop/f_p_goodmap.png""")
    
def matchFVT2FP(fvtProduct,fvtMonth,fvtrow,goodMap,transFVT):
    inner=0
    for fpindex, fprow in goodMap.iterrows():
        fpMonth = fprow['Month']
        fpCases = fprow['Cases Sold']
        fpProduct = fprow['Product']
        #print 'fvtProduct: ', fvtProduct, ' fpProduct: ', fpProduct, '| fpMonth: ', fpMonth, ' fvtMonth: ', fvtMonth, '| fpCases: ', fpCases, '\n'
        
        if fpMonth == fvtMonth and fpProduct == fvtProduct:
            inner+=1
            if fpCases > 0.0:     
                    
                    if fvtrow[fvtProduct] == 0.0:
                        available.append(0)
                            
                    elif fvtrow[fvtProduct] == 1.0:
                            available.append(3)
                            
                    else:        
                        break
                          
                        #available.append(0)
            elif fvtrow[fvtProduct] == 1.0:
                print fprow
                available.append(1)
            else:                     
                available.append(0)
    #print available, '|' 
    return inner    







setGoodMap(cursor)
dbconnect.close()