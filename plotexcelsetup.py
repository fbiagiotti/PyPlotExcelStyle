# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 10:57:45 2021

@author: fbiagiotti

Excel Style Plot in Python
"""

import matplotlib.pyplot as pl

def cm2inch(x):
    if isinstance(x, (list, tuple)):
        return [i/2.54 for i in x]
    return x/2.54

dpi = 800
font = {  #'family' : 'serif',
    'weight': 'bold',
    'size': 7}
size = cm2inch([9.5, 6.33])
label_color = '#595959'
pl.rcdefaults()
params = {
    'axes.titlecolor': label_color,
    'axes.labelweight':font['weight'],
    'axes.labelcolor': label_color,
    'axes.edgecolor': label_color,
    'axes.titleweight': font['weight'],
    'font.weight': font['weight'],
    'font.size': font['size'],
    #'font.family' : font['family'],
    'figure.dpi': dpi,
    'figure.figsize': size,
    'savefig.dpi': dpi,
    'savefig.format': 'svg',
    'savefig.bbox': 'tight',
    'lines.markersize': 2,    
    'xtick.color': label_color,
    'ytick.color': label_color,
    'text.color': label_color,
    'grid.color': '#BFBFBF',
    }

pl.rcParams.update(params)
