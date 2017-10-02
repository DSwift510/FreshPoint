# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:39:45 2017

@author: Dasani
"""

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from random import randint

# x and y coordinates
x = np.array(range(10))
y = np.array(range(10,15))
data = np.zeros((len(y),len(x)))

# Generate some discrete data (1, 2 or 3) for each (x, y) pair
for i,yy in enumerate(y):
    for j, xx in enumerate(x):
        data[i,j] = randint(1,3)

# Map 1, 2 and 3 to 'Red', 'Green' qnd 'Blue', respectively
colormap = colors.ListedColormap(['Red', 'Green', 'Blue'])
colorbar_ticklabels = ['1', '2', '3']

# Use matshow to create a heatmap
fig, ax = plt.subplots()
ms = ax.matshow(data, cmap = colormap, vmin=data.min() - 0.5, vmax=data.max() + 0.5, origin = 'lower')

# x and y axis ticks
ax.set_xticklabels([str(xx) for xx in x])
ax.set_yticklabels([str(yy) for yy in y])
ax.xaxis.tick_bottom()

# Put the x- qnd y-axis ticks at the middle of each cell 
ax.set_xticks(np.arange(data.shape[1]), minor = False)
ax.set_yticks(np.arange(data.shape[0]), minor = False)

# Set custom ticks and ticklabels for color bar
cbar = fig.colorbar(ms,ticks = np.arange(np.min(data),np.max(data)+1))
cbar.ax.set_yticklabels(colorbar_ticklabels)

plt.show()

def show3d():
    #Need productid, cases, and Not_local
    prodid = 1242
    cases = 43
    local = 1
    bought = {prodid:{month,local}} #Lookup dictionary of productid, cases, and Not_local
    
    availability = []
    betterBuy = {}
    #Need to scroll through rows. if cases check local
    ####
    #####
    ######
    #
    for prodid, clList in bought.iteritems():    
        for lcases, lolocal in clList.iteritems():
            if lcases < 0:
                print "error caused by negative productID number"
                break
            if lcases == 0:
                availability.append(0)
            if lcases > 0 and lolocal == 1:
                availability.append(1)
            if lcases > 0 and lolocal == 0:
                availability.append(2)    
        betterBuy[prodid]=availability[-1]
    
    