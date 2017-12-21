import numpy as np
import xlrd 

import scipy.stats as sp
import matplotlib.pyplot as plt
import math 

def calc_covariance( stack ):
    covarianceMat= np.matrix.round(np.cov(stack),3)
    return covarianceMat;