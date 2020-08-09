# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 11:05:17 2020

@author: yan_y
"""
import os, paddlehub as hub
huseg = hub.Module(name='deeplabv3p_xception65_humanseg')
path = 'D:\Pictures\imgs/' 
files = [path + i for i in os.listdir(path)]
results = huseg.segmentation(data={'image': files})
for result in results:
    print(result)
    

