import matplotlib.pyplot as plt
import numpy as np
Length = 20 #ft
Width = 8 #in
Height = 12 #in
Stiffness = 100000 #ksi
Left_support = 1 # [1] fixed,[2] pinned,[3] roller,[4] cantilever:
Right_support = 1 #[1] fixed,[2] pinned,[3] roller,[4] cantilever:
Load_type =1 # [1] Point (kips),[2] Distributed(kips/ft)
Load_magnitude = 10 #kips
Location = 15# coord for point, 1/2 means distributed type

def deflect_vector(L,W,H,E,LS,RS,LT,LM,PL):
   # figure out what type of supports
   L = L*12
   I = W*(H**3)/12.0
   resolution = 100
   interval = L/resolution
   x = np.arange(0,L+1,interval)   
   y = np.zeros(len(x),)
   if LS==1:
      if RS==1: #fixed-fixed
        if LT==1: #point load
            PL = PL*12
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -(LM*((L-PL)**2)*(x[i]**2))/(6.0*E*I*(L**3))*(2.0*PL*(L-x[i])+L*(PL-x[i]))
               if x[i]>PL:
                  y[i] = -(LM*((L-x[i])**2)*(PL**2))/(6.0*E*I*(L**3))\
                  *(2.0*(L-PL)*(x[i])+L*(x[i]-PL))
            print('a')
            return y,x/12.0 
        elif LT == 2: #dist load
           LM = LM/12.0
           if PL==1:
               for i in range(len(x)): #const dist
                  y[i] = -((LM*(x[i]**2))/(24.0*E*I))*((L-x[i])**2)
               print('b')
               return y,x/12.0 
           elif PL==2:
               for i in range(len(x)): #triangular dist
                   print(x[i])
                   y[i] = -((LM*L)/(120.0*E*I))*(3.0*(x[i]**3)-(2.0*L)*(x[i]**2)-(x[i]**5)/(L**2))
               print(len(y))
               print(len(x))
               print('c')
               return y,x/12.0   
      elif RS==2:#fixed-pinned
         if LT ==1: #point load
            PL = PL*12.0
            m = (L+PL)*(L+L-PL)+PL*L
            n = PL*L*(L+L-PL)
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -((LM*(L-PL)*(x[i]**2))/(12.0*E*I*(L**3)))*(3*n-m*x[i])
               if x[i]>PL:
                  y[i] = -((LM*(PL**2)*(L-x[i]))/(12.0*E*I*(L**3)))*(3.0*(L-PL)*(L**2)-((L-x[i])**2)*(3*L-PL))
            print('d')
            return y,x/12.0
         elif LT==2: #dist load
            LM=LM/12.0
            if PL==1: #dist constant load
                for i in range(len(x)):
                   y[i] = (LM/(48.0*E*I))*(3.0*L*(x[i]**3)-2*(x[i]**4)-(L**3)*x[i]) 
                y = y[::-1]
                print('e')
                return y,x/12.0
            elif PL==2: #dist triangular
                for i in range(len(x)):
                    y[i] = -(LM/(240*E*I))*(11*L*(x[i]**2)+3*x[i]*(L**3)-10*(x[i]**4) + (2*(x[i]**5))/L)
                y = y[::-1]
                print('f')
                return y,x/12.0
      elif RS==3:  #fixed roller 
         if LT ==1: #point load
            PL = PL*12.0
            m = (L+PL)*(L+L-PL)+PL*L
            n = PL*L*(L+L-PL)
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -((LM*(L-PL)*(x[i]**2))/(12.0*E*I*(L**3)))*(3*n-m*x[i])
               if x[i]>PL:
                  y[i] = -((LM*(PL**2)*(L-x[i]))/(12.0*E*I*(L**3)))*(3.0*(L-PL)*(L**2)-((L-x[i])**2)*(3*L-PL))
            print('g')
            return y,x/12.0
         elif LT==2: #dist load
            LM=LM/12.0
            if PL==1: #dist constant load
                for i in range(len(x)):
                   y[i] = (LM/(48.0*E*I))*(3.0*L*(x[i]**3)-2*(x[i]**4)-(L**3)*x[i]) 
                y = y[::-1]
                print('h')
                return y,x/12.0
            elif PL==2: #dist triangular
                for i in range(len(x)):
                    y[i] = -(LM/(240*E*I))*(11*L*(x[i]**2)+3*x[i]*(L**3)-10*(x[i]**4) + (2*(x[i]**5))/L)
                y = y[::-1]
                print('i')
                return y,x/12.0
      elif RS==4:  # cantilever
         if LT==1: #point load
            PL = PL*12
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -((LM*(x[i]**2))/(6.0*E*I))*(3.0*PL-x[i])
               elif x[i]>PL:
                  y[i] = -((LM*(PL**2))/(6.0*E*I))*(3.0*x[i]-PL)
            print('j')
            return y,x/12.0
         if LT==2: #dist loads
            LM = LM/12.0
            if PL == 1: #const distributed
                for i in range(len(x)):
                   y[i] = -((LM*(x[i]**2))/(24.0*E*I))*(x[i]**2 + 6.0*(L**2)-4.0*L*x[i])
                print('k')
                return y,x/12.0
            elif PL==2: #triangular
                for i in range(len(x)):
                    y[i] = -((LM)/(120*E*I*L))*(-(x[i]**5)-15*(L**4)*x[i]+5*L*(x[i]**4)+11*(L**5))
                y = y[::-1]
                print('l')
                return y,x/12.0
                
   elif LS==2:       
      if RS==1:#pinned-fixed
         if LT ==1: #point load
            PL = PL*12.0
            m = (L+PL)*(L+L-PL)+PL*L
            n = PL*L*(L+L-PL)
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -((LM*(L-PL)*(x[i]**2))/(12.0*E*I*(L**3)))*(3*n-m*x[i])
               if x[i]>PL:
                  y[i] = -((LM*(PL**2)*(L-x[i]))/(12.0*E*I*(L**3)))*(3.0*(L-PL)*(L**2)-((L-x[i])**2)*(3*L-PL))
            y = y[::-1]
            print('m')
            return y,x/12.0
         elif LT==2: #dist load
            LM=LM/12.0
            if PL==1:#const dist
                for i in range(len(x)):
                   y[i] = (LM/(48.0*E*I))*(3.0*L*(x[i]**3)-2*(x[i]**4)-(L**3)*x[i]) 
                print('n')
                return y,x/12.0
            elif PL==2:#triangular dist
                for i in range(len(x)):
                    y[i] = -((LM*x[i])/(120*E*I))*(2*L*(x[i]**2)-L**3-(x[i]**4)/L)
                print('o')
                return y,x/12.0    
      elif RS==2: #pinned-pinned
         if LT==1: #point load
            PL=PL*12
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -((LM*(L-PL)*x[i])/(6*L*E*I))*(L**2 - x[i]**2 -(L-PL)**2)
               if x[i]>PL:
                  y[i] = -((LM*PL*(L-x[i]))/(6.0*L*E*I))*(2*L*x[i]-(x[i]**2)-PL**2)
            print('p')
            return y,x/12.0
         if LT==2: #dist load
            LM=LM/12.0
            if PL==1:#const dist
                for i in range(len(x)):
                   y[i] = -((LM*x[i])/(24.0*E*I))*(L**3-2*L*(x[i]**2)+x[i]**3)
                print('q')
                return y,x/12.0
            
            elif PL==2:#triangulalr dist
                for i in range(len(x)):
                    y[i] = -((LM*x[i])/(360*L*E*I))*(7*(L**4)-10*(L**2)*(x[i]**2)+3*(x[i]**4))
                print('r')
                return y,x/12.0
      elif RS==3:#pinned roller maybe indeterminate
         if LT==1: #point load
            PL=PL*12
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -((LM*(L-PL)*x[i])/(6*L*E*I))*(L**2 - x[i]**2 -(L-PL)**2)
               if x[i]>PL:
                  y[i] = -((LM*PL*(L-x[i]))/(6.0*L*E*I))*(2*L*x[i]-(x[i]**2)-PL**2)
            print('s')
            return y,x/12.0
         if LT==2: #dist load
            LM=LM/12.0
            if PL==1:#const dist
                for i in range(len(x)):
                   y[i] = -((LM*x[i])/(24.0*E*I))*(L**3-2*L*(x[i]**2)+x[i]**3)
                print('t')
                return y,x/12.0
            elif PL==2:#triangulalr dist
                for i in range(len(x)):
                    y[i] = -((LM*x[i])/(360*L*E*I))*(7*(L**4)-10*(L**2)*(x[i]**2)+3*(x[i]**4))
                print('u')
                return y,x/12.0
   elif LS==3:
      if RS==1: #roller-fixed
         if LT ==1: #point load
            PL = PL*12.0
            m = (L+PL)*(L+L-PL)+PL*L
            n = PL*L*(L+L-PL)
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -((LM*(L-PL)*(x[i]**2))/(12.0*E*I*(L**3)))*(3*n-m*x[i])
               if x[i]>PL:
                  y[i] = -((LM*(PL**2)*(L-x[i]))/(12.0*E*I*(L**3)))*(3.0*(L-PL)*(L**2)-((L-x[i])**2)*(3*L-PL))
            y = y[::-1]
            print('v')
            return y,x/12.0
         elif LT==2: #dist load
            LM=LM/12.0
            if PL==1:#const dist
                for i in range(len(x)):
                   y[i] = (LM/(48.0*E*I))*(3.0*L*(x[i]**3)-2*(x[i]**4)-(L**3)*x[i]) 
                print('w')
                return y,x/12.0
            elif PL==2:#triangular dist
                for i in range(len(x)):
                    y[i] = -((LM*x[i])/(120*E*I))*(2*L*(x[i]**2)-L**3-(x[i]**4)/L)
                print('x')
                return y,x/12.0    
      elif RS==2: #roller-pinned
         if LT==1: #point load
            PL=PL*12
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -((LM*(L-PL)*x[i])/(6*L*E*I))*(L**2 - x[i]**2 -(L-PL)**2)
               if x[i]>PL:
                  y[i] = -((LM*PL*(L-x[i]))/(6.0*L*E*I))*(2*L*x[i]-(x[i]**2)-PL**2)
            print('y')
            return y,x/12.0
         if LT==2: #dist load
            LM=LM/12.0
            if PL==1:#const dist
                for i in range(len(x)):
                   y[i] = -((LM*x[i])/(24.0*E*I))*(L**3-2*L*(x[i]**2)+x[i]**3)
                print('z')
                return y,x/12.0
            elif PL==2:#triangulalr dist
                for i in range(len(x)):
                    y[i] = -((LM*x[i])/(360*L*E*I))*(7*(L**4)-10*(L**2)*(x[i]**2)+3*(x[i]**4))
                print('aa')
                return y,x/12.0
   elif LS==4 and RS==1: # reveresed cantilever
         if LT==1: #point load
            PL = PL*12
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -((LM*(x[i]**2))/(6.0*E*I))*(3.0*PL-x[i])
               elif x[i]>PL:
                  y[i] = -((LM*(PL**2))/(6.0*E*I))*(3.0*x[i]-PL)
            print('bb')
            return y,x/12.0
         if LT==2: #dist loads
            LM = LM/12.0
            if PL==1: #dist const
                for i in range(len(x)):
                   y[i] = -((LM*(x[i]**2))/(24.0*E*I))*(x[i]**2 + 6.0*(L**2)-4.0*L*x[i])
                print('cc')
                return y,x/12.0
            if PL==1: #triagular dist
                for i in range(len(x)):
                    y[i] = -((LM)/(120*E*I*L))*((x[i]**5)-5(L**5)*x[i]+4*(L**5))
                print('dd')
                return y,x/12.0
            
# this is to test results
# def deflect_vector(L,W,H,E,LS,RS,LT,LM,PL):

Y,X = deflect_vector(Length,Width,Height,Stiffness, 1,1,2,Load_magnitude,2)
plt.plot(X,Y)
plt.show()
