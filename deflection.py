Length = 20 #in
Width = 8 #in
Height = 12 #in
Stiffness = 100000 #ksi
Left_support = 1 # [1] fixed,[2] pinned,[3] roller,[4] cantilever:
Right_support = 1 #[1] fixed,[2] pinned,[3] roller,[4] cantilever:
Load_type =1 # [1] Point (kips),[2] Distributed(kips/ft)
Load_magnitude = 10 #kips
Location = 5 # x coord for point, 1/2 means distributed type
def deflect_vector(L,W,H,E,LS,RS,LT,LM,PL=0):
   # figure out what type of supports
   if LS==1:
      if RS==1:
        #fixed-fixed
      elif RS==2:
        #fixed-pinned
      elif RS==3:
        #fixed roller maybe indeterminate
      elif RS==4:
        # cantilever
   elif LS==2:       
      if RS==1:
        #fixed-fixed
      elif RS==2:
        #fixed-pinned
      elif RS==3:
        #fixed roller maybe indeterminate
   elif LS==3:
      if RS==1:
        #fixed-fixed
      elif RS==2:
        #fixed-pinned
   elif LS==4 and RS==1:
      # reveresed cantilever
c = deflect_vector(Length,Width,Height, Left_support,Right_support,Load_type,Load_magnitude,Location)
print(c)
