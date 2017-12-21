import numpy as np
import xlrd 

import scipy.stats as sp
import matplotlib.pyplot as plt
import math 

def calc_variance( arr ):
    varianceValue= np.round(np.var(arr,dtype=np.float64),3);
    return varianceValue;