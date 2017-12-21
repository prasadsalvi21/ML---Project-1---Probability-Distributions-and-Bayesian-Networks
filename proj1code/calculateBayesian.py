import numpy as np
import xlrd 

import scipy.stats as sp
import matplotlib.pyplot as plt
from math import log1p, pi 

def calc_logLike(q, p):
    p0 = 1
    x11 = 0 
    x12 = 0
    x21 = 0
    x22 = 0
    
    for i in range(49):
        x11 = x11 + (p0 * p0)
        x12 = x12 + (p[i] * p0)
        x21 = x21 + (p0 * p[i])
        x22 = x22 + (p[i] * p[i])
    x = ([x11, x12],[x21, x22])

    y11 = 0
    y21 = 0
    i = 0
    for i in range(49):
        y11 = y11 + (q[i] * p0)
        y21 = y21 + (q[i] * p[i])
    y = ([y11],[y21])
  
    beta = np.linalg.solve(x,y)

    sigma = 0
    i=0
    for i in range(49):
        term1 = beta[0] * p0
        term2 = beta[1] * p[i]
        sigma = sigma + ((term1+term2-q[i])**2)
    
    sigma = sigma/49; 
    
    loglikelihood = 0
    i = 0
    
    for i in range(49):
        term1 = log1p(2*pi*sigma)
        term2 = (beta[0]*p0)+(beta[1]*p[i])-q[i]
        term2sq = term2**2
        term3 = 2*sigma
        term4 = 1/term3
        loglikelihood = loglikelihood + (((-0.5)*term1)-(term4*term2sq))
    
    return loglikelihood