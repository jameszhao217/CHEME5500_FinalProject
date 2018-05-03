# -*- coding: utf-8 -*-
"""
Created on Thu May 03 12:19:46 2018

@author: terre
"""
import numpy as np
from deflection import a
supports = np.arange(1, 5, dtype=int)
er=True

print('Welcome to simply supported Euler Beam Deflection calculator')
print('********Geometry/Material Properties********')
L = input("What is the length of your beam (ft): ")
W = input("What is the width of your beam (in): ")#may ant to consider plate theory warning
h = input("What is the height of your beam (in): ")
E = input("What is the young's modulus of your beam (ksi): ")
while er:
   er = False
   print('********Supports********')
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
   if RS==2 and LS==2 or RS==4 and LS!=2 or LS==4 and LS!=2:
      print('ERROR: this is an indeterminate beam\
\nplease select new conditions')
      er = True
er = True
while er:
    print('********Loading Conditions********')
    er = False
    Load_type = input("What type of loading conditions [1] Point (kips),[2] Distributed(lbs/ft): ")
    if Load_type==1:
        Location=input("Where is the location (m) of your point source x=: ")
        P_mag = input('what is the magnitude of the point load (lbs): ')
        if Location>L:
            print('ERROR: point load out of domain of beam')
            er = True 
    elif Load_type==2:
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
# calulate deflection with deflection.py 
l = a()
print(l)
