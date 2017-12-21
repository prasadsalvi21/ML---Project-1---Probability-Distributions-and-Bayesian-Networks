import numpy as np
import xlrd 

import scipy.stats as sp
import matplotlib.pyplot as plt
import math 

def calc_MGD(p,q,y):
    temp = 0
    X = np.empty([q,q])
    ymod = np.zeros(shape=(1,q)) 
    for j in range(0,q):
        for i in range(0,q):
            temp = 0            
            for  s in range(0,49):
                temp += (p[i][s] *p[j][s])
            X[i][j] = temp
        
    for u in range(0,q):
        temp = 0
        for  s in range(0,49):            
             temp+= y[s]*p[u][s]          
        ymod[0][u] = temp          
    ymod2 = np.transpose(ymod)    
            
    beta = np.linalg.solve(X,ymod2)        
       
    sigma11 = 0
    sigma21 = 0    
    for s in range(0,49):
      sigma11 = 0  
      for i in range(0,q): 
          sigma11+= beta[i][0]*p[i][s]          
      sigma21+=(sigma11-y[s])**2         
    sigmasqr =sigma21/49         
     
    theta = 0
           
        
    for s in range(0,49):    
        sigma11= 0       
        for i in range(0,q):
            sigma11+= beta[i][0]*p[i][s]  
        theta +=-0.5*(math.log(2*math.pi*sigmasqr))-((0.5 *((sigma11-y[s])**2))/sigmasqr)    
    
        
    return theta