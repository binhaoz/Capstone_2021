# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 03:59:17 2017

@author:  zhuowenlin
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# the os is not used

#data = open("last_5_frames.txt","r") what is the meaning of it??
x = []
y = []
#atomnumber = 785

# 方法一
atomnumber= 18102 #number of atoms shown in the last five frames

# 方法二
count = 0
f = open("last_5_frames.txt", "r")
for line in f.readlines():
    count += 1
atomnumber = count
# 注意txt中不要有空行

frame = 1 #  multi-frame is not necessary 


def atom_dis(r, skip=0):
  

    i = 1
    for i in range(atomnumber):
        i +=1
        s = r.readline().strip().split()
        #print(s)
        Type = s[2]
        x_co = float(s[4])
        y_co = float(s[5])
        if Type =='O': 
            x.append(x_co)
            y.append(y_co)
            #print(Type)
            #print(s)
    return 

def cycle(frame):
    r = open("last_5_frames.txt","r")
    #j = 1
    #for j in range(frame):
    #    j +=1
    atom_dis(r, skip=0) #调用函数atom_dis
    x_array = np.array(x)
    y_array = np.array(y)
        #z_array = x_array
        #z_array += z_array
    return x_array, y_array



#atomnum(file)
#cycle(frame)
#hist2,bins2=np.histogram(cycle(frame=69),bins=100)
#print(hist2)
#print(bins2) 
np.z = cycle(frame)
H, xedges, yedges=np.histogram2d(np.z[0], np.z[1], bins=80)
                                 
                                



xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
#im.set_data(xcenters, ycenters, H)
#ax.images.append(im)

#######################################################
cp = plt.contourf(H/5,cmap='rainbow')
plt.colorbar(cp)
plt.savefig("fig-B-1.28.eps", format='eps', dpi=2000)
#plt.imshow(H)
