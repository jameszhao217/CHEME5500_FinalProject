import matplotlib.pyplot as plt
import numpy as np
# this is function takes all the inputs and decides what type of conditions
# then outputs deflection vecors
def deflect_output(L,W,H,E,LS,RS,LT,LM,PL):
   # figure out what type of supports
   L = L*12.0
   I = W*(H**3)/12.0
   resolution = 500.0
   interval = L/resolution
   x = np.arange(0,L+1,interval)   
   y = np.zeros(len(x),)
   if LS==1:
      if RS==1: #fixed-fixed
        if LT==1: #point load
            PL = PL*12.0
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -(LM*((L-PL)**2)*(x[i]**2))/(6.0*E*I*(L**3))*(2.0*PL*(L-x[i])+L*(PL-x[i]))
               if x[i]>PL:
                  y[i] = -(LM*((L-x[i])**2)*(PL**2))/(6.0*E*I*(L**3))\
                  *(2.0*(L-PL)*(x[i])+L*(x[i]-PL))
            return y,x/12.0 
        elif LT == 2: #dist load
           LM = LM/12.0
           if PL==1:
               for i in range(len(x)): #const dist
                  y[i] = -((LM*(x[i]**2))/(24.0*E*I))*((L-x[i])**2)
               return y,x/12.0 
           elif PL==2:
               for i in range(len(x)): #triangular dist
                   y[i] = ((LM*L)/(120.0*E*I))*(3.0*(x[i]**3)-(2.0*L)*(x[i]**2)-(x[i]**5)/(L**2))
               return y,x/12.0   
      elif RS==2:#fixed-pinned
         if LT ==1: #point load
            PL = PL*12.0
            m = (L+PL)*(L+L-PL)+PL*L
            n = PL*L*(L+L-PL)
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -((LM*(L-PL)*(x[i]**2))/(12.0*E*I*(L**3)))*(3.0*n-m*x[i])
               if x[i]>PL:
                  y[i] = -((LM*(PL**2)*(L-x[i]))/(12.0*E*I*(L**3)))*(3.0*(L-PL)*(L**2)-((L-x[i])**2)*(3.0*L-PL))
            return y,x/12.0
         elif LT==2: #dist load
            LM=LM/12.0
            if PL==1: #dist constant load
                for i in range(len(x)):
                   y[i] = (LM/(48.0*E*I))*(3.0*L*(x[i]**3)-2.0*(x[i]**4)-(L**3)*x[i]) 
                y = y[::-1]
                return y,x/12.0
            elif PL==2: #dist triangular
                for i in range(len(x)):
                    y[i] = (LM/(240.0*E*I))*(11.0*L*(x[i]**3)-(3.0*x[i]*(L**3))-(10.0*(x[i]**4)) + (2.0*(x[i]**5))/L)
                y = y[::-1]
                return y,x/12.0
      elif RS==3:  #fixed roller 
         if LT ==1: #point load
            PL = PL*12.0
            m = (L+PL)*(L+L-PL)+PL*L
            n = PL*L*(L+L-PL)
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -((LM*(L-PL)*(x[i]**2))/(12.0*E*I*(L**3)))*(3.0*n-m*x[i])
               if x[i]>PL:
                  y[i] = -((LM*(PL**2)*(L-x[i]))/(12.0*E*I*(L**3)))*(3.0*(L-PL)*(L**2)-((L-x[i])**2)*(3.0*L-PL))
            return y,x/12.0
         elif LT==2: #dist load
            LM=LM/12.0
            if PL==1: #dist constant load
                for i in range(len(x)):
                   y[i] = (LM/(48.0*E*I))*(3.0*L*(x[i]**3)-2*(x[i]**4)-(L**3)*x[i]) 
                y = y[::-1]
                return y,x/12.0
            elif PL==2: #dist triangular
                for i in range(len(x)):
                    y[i] = (LM/(240.0*E*I))*(11.0*L*(x[i]**3)-3.0*x[i]*(L**3)-10.0*(x[i]**4) + (2.0*(x[i]**5))/L)
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
            if PL == 1: #const distributed
                for i in range(len(x)):
                   y[i] = -((LM*L*(x[i]**2))/(24.0*E*I*L))*(2.0*(L**2) + (2.0*L-x[i])**2)
                return y,x/12.0
            elif PL==2: #triangular
                for i in range(len(x)):
                    y[i] = -((LM)/(120*E*I*L))*(-(x[i]**5)-15.0*(L**4)*x[i]+5*L*(x[i]**4)+11*(L**5))
                y = y[::-1]
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
            if PL==1:#const dist
                for i in range(len(x)):
                   y[i] = (LM/(48.0*E*I))*(3.0*L*(x[i]**3)-2*(x[i]**4)-(L**3)*x[i]) 
                return y,x/12.0
            elif PL==2:#triangular dist
                for i in range(len(x)):
                    y[i] = ((LM*x[i])/(120*E*I))*(2*L*(x[i]**2)-L**3-(x[i]**4)/L)
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
            LM=LM/12.0
            if PL==1:#const dist
                for i in range(len(x)):
                   y[i] = -((LM*x[i])/(24.0*E*I))*(L**3-2*L*(x[i]**2)+x[i]**3)
                return y,x/12.0
            
            elif PL==2:#triangulalr dist
                for i in range(len(x)):
                    y[i] = -((LM*x[i])/(360*L*E*I))*(7*(L**4)-10*(L**2)*(x[i]**2)+3*(x[i]**4))
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
            LM=LM/12.0
            if PL==1:#const dist
                for i in range(len(x)):
                   y[i] = -((LM*x[i])/(24.0*E*I))*(L**3-2*L*(x[i]**2)+x[i]**3)
                return y,x/12.0
            elif PL==2:#triangulalr dist
                for i in range(len(x)):
                    y[i] = -((LM*x[i])/(360*L*E*I))*(7*(L**4)-10*(L**2)*(x[i]**2)+3*(x[i]**4))
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
            if PL==1:#const dist
                for i in range(len(x)):
                   y[i] = (LM/(48.0*E*I))*(3.0*L*(x[i]**3)-2*(x[i]**4)-(L**3)*x[i]) 
                return y,x/12.0
            elif PL==2:#triangular dist
                for i in range(len(x)):
                    y[i] = ((LM*x[i])/(120*E*I))*(2*L*(x[i]**2)-L**3-(x[i]**4)/L)
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
            LM=LM/12.0
            if PL==1:#const dist
                for i in range(len(x)):
                   y[i] = -((LM*x[i])/(24.0*E*I))*(L**3-2*L*(x[i]**2)+x[i]**3)
                return y,x/12.0
            elif PL==2:#triangulalr dist
                for i in range(len(x)):
                    y[i] = -((LM*x[i])/(360*L*E*I))*(7*(L**4)-10*(L**2)*(x[i]**2)+3*(x[i]**4))
                return y,x/12.0
   elif LS==4 and RS==1: # reveresed cantilever
         if LT==1: #point load
            PL = PL*12.0
            for i in range(len(x)):
               if x[i]<=PL:
                  y[i] = -((LM*(x[i]**2))/(6.0*E*I))*(3.0*PL-x[i])
               elif x[i]>PL:
                  y[i] = -((LM*(PL**2))/(6.0*E*I))*(3.0*x[i]-PL)
            y = y[::-1]
            return y,x/12.0
         if LT==2: #dist loads
            LM = LM/12.0
            if PL==1: #dist const
                for i in range(len(x)):
                   y[i] = -((LM*(x[i]**2))/(24.0*E*I))*(x[i]**2 + 6.0*(L**2)-4.0*L*x[i])
                y = y[::-1]
                return y,x/12.0
            if PL==2: #triagular dist
                for i in range(len(x)):
                    y[i] = -((LM*(x[i]**2))/(120.0*E*I*L))*(10.0*(L**3)-10.0*(L**2)*x[i]+5.0*L*(x[i]**2)-(x[i]**3))
                y = y[::-1]
                return y,x/12.0
            

