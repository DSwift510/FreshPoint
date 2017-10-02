# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 00:29:02 2017

@author: Dasani
"""
import heatmap.py
import insert.py
import main.py
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
import pprint as pp
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from matplotlib import colors




class Database(object):

    def __init__(
            self, 
                 prodList, 
                 freshpoint, 
                 fvTable, 
                 produceML, 
                 dbconnect = mysql.connector.connect(host='localhost',port='3309',database='ufoods',user='root',password='aggi3pride'
                 
                 )):
        
        self.pl = prodList
        self.fp = freshpoint
        self.fv = fvTable
        self.pml = produceML

class Table(Database):

    def __init__(self, db, table):
        Database.__init__(self, db)
        self.tbl = table

class Data(Table):
    
    def _init_(self,db, table, column, row, data):
        Table._init_(self, db, table)
        self.col = column
        self.row = row
        self.data = data
        

        