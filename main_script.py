# -*- coding: utf-8 -*-
"""
Created on Thu May 03 12:19:46 2018

@author: terre
"""
import matplotlib.pyplot as plt
import numpy as np
from deflection import deflect_output
import operator

from pygame_script import pygame_plot

supports = np.arange(1, 5, dtype=int) #range of possible support conditions
er=True

print('Welcome to simply supported Euler Beam Deflection calculator')
print('********Geometry/Material Properties********')
L = input("What is the length of your beam (ft): ")
W = input("What is the width of your beam (in): ")
H = input("What is the height of your beam (in): ")
E = input("What is the young's modulus of your beam (ksi): ")
while er: # reasks the question if incorrect inputs
   er = False
   print('*****************Supports*****************')
   LS = input("What is the left support [1] fixed,[2] pinned,[3] roller,[4] cantilever: ")
   RS = input("What is the right support [1] fixed,[2] pinned,[3] roller,[4] cantilever: ")
   print(LS)
   if LS not in supports[:]:
      print('ERROR: incorrect left  boundary conditions selection\
\nplease select new conditions')
      er = True
   if RS not in supports[:] :
      print('ERROR: incorrect right boundary conditions selection\
      \nplease select new conditions')
      er = True
   if RS==2 and LS==2 or RS==4 and LS!=1 or LS==4 and RS!=1:
      print('ERROR: this is an indeterminate beam\
\nplease select new conditions')
      er = True
er = True
while er:# reasks the question if incorrect inputs
    print('***********Loading Conditions***********')
    er = False
    Load_type = input("What type of loading conditions [1] Point (kips),[2] Distributed(kips/ft): ")
    if Load_type==1:
        Location=input("Where is the location (m) of your point source x=: ")
        P_mag = input('what is the magnitude of the point load (kips): ')
        if Location>L:
            print('ERROR: point load out of domain of beam')
            er = True 
    elif Load_type==2:
        #loaction variable is used to determine type of distribution 
        Location = input("What type of distributed loading:[1] Constant (kips/ft);[2] Triangular (kips/ft): ")
        if Location==1:
            P_mag = input('what is the magnitude of the constant distributed load (kips/ft): ')
            break
        elif Location==2:
            P_mag = input('what is the magnitude of the triangular load at x=L (kips): ') #maybe do trapezoidal loading
            break
        elif Location!=1 and Location!=2:
            print('ERROR: incorrect choice for loading conditions')
            er = True
    elif Load_type!=1 and Load_type!=2:
        print('ERROR: incorrect choice for loading conditions')
        er = True
# Run script with user input
Y,X = deflect_output(L,W,H,E,LS,RS,Load_type,P_mag,Location) #to plot deflection
Y = np.absolute(Y) # Y-axis is always negative
plt.plot(X,Y)
plt.title('BEAM DEFLECTION PLOT')
plt.xlabel('BEAM LENGTH (ft)')
plt.ylabel('DEFLECTION (in)')
ax = plt.gca()
ax.invert_yaxis()
plt.savefig('deflection.png')
# plt.show()
index, y_max = max(enumerate(Y), key=operator.itemgetter(1)) #find max deflection and index
print 'MAX DEFLECTION = %f (in) at x = %f (ft)' % (y_max,X[index])
print'********************Delflection at a specified point**********************'
er = True
while er:# reasks the question if incorrect inputs
    def find_nearest(array,value):
        idx = (np.abs(array-value)).argmin()
        return array[idx],idx
    x_val = input("Where do you want to know the deflection: x=: ")
    if x_val<=L:
        er=False
    else:
        print('ERROR: x location out of domain of beam')
x_approx,x_index = find_nearest(X,x_val)
print ('DEFLECTION AT x = %f (ft) IS %f (in)' % (x_val,Y[x_index]))
print('thanks for playing!!!!!!!')


# MZ Added: Pygame Plot GUI
pygame_plot()

