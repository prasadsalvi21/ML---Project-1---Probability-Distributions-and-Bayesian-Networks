import numpy as np
import xlrd 

import scipy.stats as sp
import matplotlib.pyplot as plt
import math 

def calc_std( arr ):
    stdValue= np.round(np.std(arr),3);
    return stdValue;