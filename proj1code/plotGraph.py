import numpy as np
import xlrd 

import scipy.stats as sp
import matplotlib.pyplot as plt
import math 


def plot_graph(i,mainarray,names):
    fig=plt.figure();
    fig.canvas.set_window_title(names[i]+' Graph Plot ')
    fig.suptitle(names[i]+' Graph Plot ',color='b')
    count = 0 
    for j in range(0,4):    
        count+=1
        ax1 = fig.add_subplot(2,2,count) 
        ax1.set_title(names[i]+' VS ' +names[j],color='r')
        ax1.scatter(mainarray[i],mainarray[j]) 
        ax1.set_xlabel(names[i],color='b')
        ax1.set_ylabel(names[j],color='b')
        
    plt.show() 
    return  