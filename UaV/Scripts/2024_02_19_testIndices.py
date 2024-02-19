# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 21:31:49 2024

With PS VARI works best!

@author: lgxsv2
"""

import skimage.io as IO
import numpy as np 
import os


fn = r"D:\Gravelbox\UaV\Data\PSim.tif"





#%% indices 

def RGI(R, G, B):
    return R / G

def RGBVI(R, G, B):
    return (G * G - R * B) / (G * G + R * B)

def GLI(R, G, B):
    return (2 * G - R - B) / (2 * G + R + B)

def VARI(R, G, B):
    return (G - R) / (G + R - B)

def NGRDI(R, G, B):
    return (G - R) / (G + R)

def ERGBVE(R, G, B):
    return np.pi * ((G**2 - R * B) / (G**2 + R * B))
#%%
def saveFunc(data, op):
    # Define your save function here
    IO.imsave(op, data)
    
#%%

def testIndices(fn, index='all', op=r"D:\Gravelbox\UaV\Data\indexTestPS"):
    
    im = IO.imread(fn)
    B, G, R = im[:, :, 0], im[:, :, 1], im[:, :, 2]
    
    indices_functions = {
        'RGI': RGI,
        'RGBVI': RGBVI,
        'GLI': GLI,
        'VARI': VARI,
        'NGRDI': NGRDI,
        'ERGBVE': ERGBVE
    }
    
    if index != 'all':
        if index in indices_functions:
            ind = indices_functions[index](R, G, B)
            saveFunc(ind, os.path.join(op, f"{index}.tif"))
            return ind
        else:
            raise ValueError("Invalid index specified.")
    else:
        for index_name, index_function in indices_functions.items():
            ind = index_function(R, G, B)
            saveFunc(ind, os.path.join(op, f"{index_name}.tif"))
            
    return ind

#%% usage:
testIndices(fn)
