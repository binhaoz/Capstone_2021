# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 03:59:17 2017

@author: Pale and zwl
"""
import numpy as np
import os


#data = open("atom.lammpstrj","r")
x = []
atomnumber = 785
frame = 550
def atom_dis(r, skip=9):
    i = 1
    for i in range(skip):
        r.readline()
        i +=1
    i = 1
    for i in range(atomnumber):
        i +=1
        s = r.readline().strip().split()
        #print(s)
        Type = int(s[1])
        xs = float(s[2]) % 1
        xe = float(s[3]) % 1
        if Type ==7: 
            x.append([xs,xe])
            #print(Type)
            #print(s)
    return 

def cycle(frame):
    r = open("80-atom.lammpstrj","r")
    j = 1
    for j in range(frame):
        j +=1
        atom_dis(r, skip=9)
        x_array = np.array(x)
        #z_array = x_array
        #z_array += z_array
    return x_array

#atomnum(file)
cycle(frame)
#hist2,bins2=np.histogram(cycle(frame=69),bins=100)
#print(hist2)
#print(bins2) 
#test
#test22222222
