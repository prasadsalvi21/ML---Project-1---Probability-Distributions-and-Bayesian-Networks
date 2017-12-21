import numpy as np
import xlrd 

import scipy.stats as sp
import matplotlib.pyplot as plt
import math 

def calc_corr( stack ):
    correlationMat = np.matrix.round(np.corrcoef(stack),3)
    return correlationMat;