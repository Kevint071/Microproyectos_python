M = [2,5,6,8,7]  
fy = 4200  
h = 30  
b = 20  
d = 0.90*h  

Asx = []
for i in M:  
   Asx.append((i*100000)/(0.81*fy*d))
   print(Asx)