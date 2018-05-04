import matplotlib.pyplot as plt
import numpy as np
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
            return y,x/12.0     
        elif LT == 2: #dist load
           LM = LM/12.0
           for i in range(len(x)):
              y[i] = -((LM*(x[i]**2))/(24.0*E*I))*((L-x[i])**2)
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
            return y,x/12.0
         elif LT==2: #dist load
            LM=LM/12.0
            for i in range(len(x)):
               y[i] = (LM/(48.0*E*I))*(3.0*L*(x[i]**3)-2*(x[i]**4)-(L**3)*x[i]) 
            y = y[::-1]
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
            return y,x/12.0
         elif LT==2: #dist load
            LM=LM/12.0
            for i in range(len(x)):
               y[i] = (LM/(48.0*E*I))*(3.0*L*(x[i]**3)-2*(x[i]**4)-(L**3)*x[i]) 
            y = y[::-1]
            return y,x/12.0
      elif RS==4:  # cantilever
         if LT==1: #point load
            PL = PL*12
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -((LM*(x[i]**2))/(6.0*E*I))*(3.0*PL-x[i])
               elif x[i]>PL:
                  y[i] = -((LM*(PL**2))/(6.0*E*I))*(3.0*x[i]-PL)
            return y,x/12.0
         if LT==2: #dist loads
            LM = LM/12.0
            for i in range(len(x)):
               y[i] = -((LM*(x[i]**2))/(24.0*E*I))*(x[i]**2 + 6.0*(L**2)-4.0*L*x[i])
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
            return y,x/12.0
         elif LT==2: #dist load
            LM=LM/12.0
            for i in range(len(x)):
               y[i] = (LM/(48.0*E*I))*(3.0*L*(x[i]**3)-2*(x[i]**4)-(L**3)*x[i]) 
            return y,x/12.0
      elif RS==2: #pinned-pinned
         if LT==1: #point load
            PL=PL*12
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -((LM*(L-PL)*x[i])/(6*L*E*I))*(L**2 - x[i]**2 -(L-PL)**2)
               if x[i]>PL:
                  y[i] = -((LM*PL*(L-x[i]))/(6.0*L*E*I))*(2*L*x[i]-(x[i]**2)-PL**2)
            return y,x/12.0
         if LT==2: #dist load
            PL=PL/12.0
            for i in range(len(x)):
               y[i] = -((LM*x[i])/(24.0*E*I))*(L**3-2*L*(x[i]**2)+x[i]**3)
            return y,x/12.0
      elif RS==3:#pinned roller maybe indeterminate
         if LT==1: #point load
            PL=PL*12
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -((LM*(L-PL)*x[i])/(6*L*E*I))*(L**2 - x[i]**2 -(L-PL)**2)
               if x[i]>PL:
                  y[i] = -((LM*PL*(L-x[i]))/(6.0*L*E*I))*(2*L*x[i]-(x[i]**2)-PL**2)
            return y,x/12.0
         if LT==2: #dist load
            PL=PL/12.0
            for i in range(len(x)):
               y[i] = -((LM*x[i])/(24.0*E*I))*(L**3-2*L*(x[i]**2)+x[i]**3)
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
            return y,x/12.0
         elif LT==2: #dist load
            LM=LM/12.0
            for i in range(len(x)):
               y[i] = (LM/(48.0*E*I))*(3.0*L*(x[i]**3)-2*(x[i]**4)-(L**3)*x[i]) 
            return y,x/12.0
      elif RS==2: #roller-pinned
         if LT==1: #point load
            PL=PL*12
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -((LM*(L-PL)*x[i])/(6*L*E*I))*(L**2 - x[i]**2 -(L-PL)**2)
               if x[i]>PL:
                  y[i] = -((LM*PL*(L-x[i]))/(6.0*L*E*I))*(2*L*x[i]-(x[i]**2)-PL**2)
            return y,x/12.0
         if LT==2: #dist load
            PL=PL/12.0
            for i in range(len(x)):
               y[i] = -((LM*x[i])/(24.0*E*I))*(L**3-2*L*(x[i]**2)+x[i]**3)
            return y,x/12.0
   elif LS==4 and RS==1: # reveresed cantilever
         if LT==1: #point load
            PL = PL*12
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -((LM*(x[i]**2))/(6.0*E*I))*(3.0*PL-x[i])
               elif x[i]>PL:
                  y[i] = -((LM*(PL**2))/(6.0*E*I))*(3.0*x[i]-PL)
            return y,x/12.0
         if LT==2: #dist loads
            LM = LM/12.0
            for i in range(len(x)):
               y[i] = -((LM*(x[i]**2))/(24.0*E*I))*(x[i]**2 + 6.0*(L**2)-4.0*L*x[i])
            return y,x/12.0
# this is to test results
#Y,X = deflect_vector(Length,Width,Height,Stiffness, 2,2,2,Load_magnitude,Location)
#plt.plot(X,Y)
#plt.show()
