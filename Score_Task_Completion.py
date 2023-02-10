#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 08:49:52 2023

@author: Aaron
"""
import statistics
from scipy.stats import sem
import scipy.stats
import pandas as pd

# References:
# Sauro, J., &; Lewis, J. R. (2016). 
# In Quantifying the user experience: Practical statistics for user research 
# (pp. 19–60). essay, Morgan Kaufmann. 

def get_Num_Scores(scores):
    """Reads in a list of scores. Counts the number of values in the list.
    Returns the length of the list."""
    
    numScores = len(scores)
    #print('numScores:', numScores)
    
    return numScores

def get_SF_Cnt(scores):
    """Reads in a list of scores. Evaluates each list item for 0, 1 values.
    Builds a count of 0, 1 list values and calculates the 0, 1 proportions.
    Returns sfProp."""
    
    numScores = get_Num_Scores(scores)
        
    p_Cnt = 0 # Successes
    q_Cnt = 0 # Failures
    
    for item in range(numScores):
        if scores[item] == 1:
            p_Cnt = p_Cnt + 1
        else:
            q_Cnt = q_Cnt + 1
           
    sf_Cnt = [p_Cnt, q_Cnt]
    #print('sf_Cnt:', sf_Cnt)
    
    return sf_Cnt

def get_Conf_Int_Dec(confIntPct):    
    """Reads in the confidence interval percentage. Converts it to decimal
    form. Returns confidence interval as a decimal."""
    
    confIntDec = round((confIntPct / 100), 2)

    return confIntDec

def get_Alpha(confIntDec):
    """Reads in a confidence interval decimal and calculates alpha.
    Returns alpha value."""

    alpha = round((1 - confIntDec), 2)
    
    return alpha    

def get_Z_Val(confIntPct):
    """Reads in a percentile value. Calls to calculate the alpha value.
    Calculates the z-value.
    Returns a list object containing the z-value and alpha."""
    
    confIntDec = get_Conf_Int_Dec(confIntPct)
    alpha = get_Alpha(confIntDec)
          
    zVal = round((scipy.stats.norm.ppf(1 - (alpha / 2))), 2)
    #print(zVal)
    
    zVals = [zVal, alpha]
               
    return zVals

def get_p_n_Adj(scores, confIntPct):
    """Reads in a list of scores. Calls the functions necessary for 
    calculating p_Adj for the Adjusted Wald Binomial Confidence interval.
    Returns a list object containing adjusted p and n values as p_n_Adj."""
    
    numScores = get_Num_Scores(scores)
    
    sf_Cnt = get_SF_Cnt(scores)
    p_Cnt = sf_Cnt[0]
    
    zVals = get_Z_Val(confIntPct)
    zVal = zVals[0]
    zSqd = round((zVal ** 2), 2)
    
    n_Adj = (numScores + zSqd)
    
    p_Adj_Num = (p_Cnt + ((zSqd) / 2))
    p_Adj = round((p_Adj_Num / n_Adj), 3)
        
    p_n_Adj = [p_Adj, n_Adj]
    #print(p_n_Adj)
      
    return p_n_Adj

def get_Conf_Int_Val(scores, confIntPct):
    """Reads in the list of scores, and the confidence interval percentile
    and calculates the confidence interval values.
    Returns the confidence interval values as adj_Wald_CI."""
    
    p_n_Adj = get_p_n_Adj(scores, confIntPct)
    p_Adj = p_n_Adj[0]
    n_Adj = p_n_Adj[1]
    
    zVals = get_Z_Val(confIntPct)
    zVal = zVals[0]
    
    adj_Wald_Num = (p_Adj * (1 - p_Adj))
    adj_Wald_Den = n_Adj
    adj_Wald_CI_Adj = zVal * ((adj_Wald_Num / adj_Wald_Den) ** 0.5)
    
    raw_adj_Wald_LCL = (p_Adj - adj_Wald_CI_Adj)
    raw_adj_Wald_UCL = (p_Adj + adj_Wald_CI_Adj)
    
    adj_Wald_LCL = round((raw_adj_Wald_LCL), 3)
    adj_Wald_UCL = round((raw_adj_Wald_UCL), 3)
    
    adj_Wald_CI = [adj_Wald_LCL, adj_Wald_UCL]
    #print('adj_Wald_CI:', adj_Wald_CI)
        
    return adj_Wald_CI

def get_CI_Val_Conv(adj_Wald_CI):
    """Reads in the adjusted-Wald confidence interval values as decimals.
    Converts values to percentages.
    Returns confidence interval list object as percentages."""
    
    aw_LCL_Pct = int(adj_Wald_CI[0] * 100)
    aw_UCL_Pct = int(adj_Wald_CI[1] * 100)
    
    aw_CI_Pct = [aw_LCL_Pct, aw_UCL_Pct]
    
    return aw_CI_Pct
        
def rpt_Conf_Int(confIntVals):
    """Reads the upper and lower confidence interval along with the mean.
    Prints the interval. 
    Return a list object with the LCL and UCL values."""
    
    LCL = (confIntVals[0])
    UCL = (confIntVals[1])
      
    print('\n** Confidence Interval **\n')
   
    print('The population success rate for this task is between', LCL,'%', 'and', UCL,'%.')
    
    rptConfIntVals = [LCL, UCL]
    
    return rptConfIntVals

def calc_CI_Values(scores, confIntPct):

    confIntVals = get_Conf_Int_Val(scores, confIntPct)
    confIntPct = get_CI_Val_Conv(confIntVals)
    rpt_ConfInts = rpt_Conf_Int(confIntPct)

### *******************************************************
### Use this block if you have data as a list of values. 
### *******************************************************
# If you have a list of values, enter them in these brackets. 

#scores = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
#scores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
#scores = [0, 0, 0, 0, 0, 0, 1, 1]

### *******************************************************


### *******************************************************
### Use this block if you have data in a .csv file.
### *******************************************************
# If you have a data table to score, use this block to score each column.
# Place your .csv file in the same directory as this file. 
# File Name Example: 'Fake_Task_Completion_Data.csv'

inFile = 'Fake_Task_Completion_Data.csv'
df = pd.read_csv(inFile, index_col=False)

# Include the column name you wish to calculate the scores on.
# Example: 'Task_1_Completion'

scores = df['Task_1_Completion'] 

# The confidence interval you would like values for, as a percent (without %).
confIntPct = 95

calc_CI_Values(scores, confIntPct)



    
    
