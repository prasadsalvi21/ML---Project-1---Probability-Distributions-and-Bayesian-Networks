# -*- coding: utf-8 -*-

import numpy as np
import xlrd 

import scipy.stats as sp
import matplotlib.pyplot as plt
import math
import calculateMean
import calculateVariance
import calculateSTD 
import calculateCovariance
import calculateCorrelation
import plotGraph
import calculateLogLikelihood
import calculateMGD
import calculateBNPGraph
import calculateBayesian

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 15),
         'axes.labelsize': 'x-small',
         'axes.titlesize':'x-small',
         'xtick.labelsize':'x-small',
         'ytick.labelsize':'x-small'}
plt.rcParams.update(params)
 
wb = xlrd.open_workbook('university data.xlsx')
ws = wb.sheet_by_index(0)
 
 
print("UBitName:prasadde")
print("personNumber:50207353")
 
'''Task 1: Compute for each variable ((CS Score, Research Overhead, Admin Base Pay, Tuition))
its sample mean, variance and standard deviation''' 
csscore = [] 
for row in range (1,50) :
    csscore.append(ws.cell(row,2).value)
    
researchoverhead = [] 
for row in range (1,50):
   researchoverhead.append(ws.cell(row,3).value)
   
adminbasepay = []
for row in range (1,50):
    adminbasepay.append(ws.cell(row,4).value)

tuition = []
for row in range (1,50):
     tuition.append(ws.cell(row,5).value)

mu1=calculateMean.calc_mean(csscore);
print('mu1='+ str(mu1))
mu2=calculateMean.calc_mean(researchoverhead);
print('mu2='+ str(mu2))
mu3=calculateMean.calc_mean(adminbasepay);
print('mu3='+ str(mu3))
mu4=calculateMean.calc_mean(tuition);
print('mu4='+ str(mu4))

var1=calculateVariance.calc_variance(csscore);
print('var1='+ str(var1))
var2=calculateVariance.calc_variance(researchoverhead);
print('var2='+ str(var2))
var3=calculateVariance.calc_variance(adminbasepay);
print('var3='+ str(var3))
var4=calculateVariance.calc_variance(tuition);
print('var4='+ str(var4))

sigma1=calculateSTD.calc_std(csscore);
print('sigma1='+ str(sigma1))
sigma2=calculateSTD.calc_std(researchoverhead);
print('sigma2='+ str(sigma2))
sigma3=calculateSTD.calc_std(adminbasepay);
print('sigma3='+ str(sigma3))
sigma4=calculateSTD.calc_std(tuition);
print('sigma4='+ str(sigma4))

'''Task 2.a: Compute for each pair of variables their covariance and correlation''' 
stack = np.vstack([csscore,researchoverhead,adminbasepay,tuition])

covarianceMat = []
covarianceMat=calculateCovariance.calc_covariance(stack);
print("covarianceMat=")
print(covarianceMat)
 

correlationMat = []
correlationMat=calculateCorrelation.calc_corr(stack);
print("correlationMat=")
print(correlationMat)

  
'''Task 2.b: Plot of the pairwise data showing the label associated with each data point'''
names = ['csscore','researchoverhead','adminbasepay','tuition'];
mainarray = [csscore,researchoverhead,adminbasepay,tuition]
   
#===============================================================================
# for i in range(0,4):
#     plotGraph.plot_graph(i,mainarray,names);
#===============================================================================

'''Task 3: Determine the log-likelihood of the data'''
mean = [mu1,mu2,mu3,mu4];
sigma=[sigma1,sigma2,sigma3,sigma4];
data=[csscore,researchoverhead,adminbasepay,tuition];
ll=calculateLogLikelihood.calc_logLike(mean,sigma,data);

logLikelihood = round(ll[4],3)
print("LogLikelihood=");
print(logLikelihood);

'''Task 4.a: BNPGraph'''       
calculateBNPGraph.calc_BNP();
 
'''Task4.b: BNlogLikelihood'''
likelihood1 = calculateBayesian.calc_logLike(adminbasepay, tuition);
likelihood2 = calculateBayesian.calc_logLike(tuition, csscore);
likelihood3 = calculateBayesian.calc_logLike(researchoverhead, csscore);
BNlogLikelihood = ll[0] + likelihood1 + likelihood2 + likelihood3;
BNlogLikelihood=np.round(BNlogLikelihood,3);
    
print('BNlogLikelihood=')
print(BNlogLikelihood) 
