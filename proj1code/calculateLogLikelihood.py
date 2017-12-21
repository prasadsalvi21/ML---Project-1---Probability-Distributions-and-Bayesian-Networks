import numpy as np
import xlrd 

import scipy.stats as sp
import matplotlib.pyplot as plt
import math 

def calc_logLike(mean,sigma,data):
    ll=[0.0,0.0,0.0,0.0];
    logLikelihood=0;
    for i in range(0,4):
        temp=data[i];
        for j in temp:
            ll[i]+=sp.norm.logpdf(j,mean[i],sigma[i]);
    
    #ll=np.array(ll);
    #print("Ind Log likelihood");
    #print(ll);
    for k in ll:
        logLikelihood+=k;
    #print(logLikelihood);
    
    ll.append(logLikelihood)
    ll=np.array(ll);
    #print(ll);
    return ll
                
            
    