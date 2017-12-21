import numpy as np
import xlrd 

import scipy.stats as sp
import matplotlib.pyplot as plt
import math 

def calc_mean( arr ):
    meanValue= np.round(np.mean(arr),3);
    return meanValue;