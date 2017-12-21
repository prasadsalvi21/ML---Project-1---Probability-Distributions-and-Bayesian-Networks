import numpy as np
import xlrd 

import scipy.stats as sp
import matplotlib.pyplot as plt
import math 

def calc_BNP():
    BNgraph = np.empty([4,4])
    
    for i in range(0,4):
        for j in range(0,4):
            BNgraph[i][j] = 0   
    
    BNgraph[0][1] = 1
    BNgraph[0][3] = 1
    BNgraph[3][2] = 1
    
    print("BNgraph=")
    print(BNgraph)