'''
   Common Algorithm
   
   Author: Ke Yang
   mailto: jakke.yang@gmail.com
'''
from __future__ import division
import math

def calcGini(branchset):
    '''
    first, calc classification percent
    '''
    datacount = len(branchset)
    pt = [0,0,0]
    for entry in branchset:
        ring = int(entry[-1])
        if (ring > 0 and ring <= 10 ):
            pt[0] = pt[0] + 1
        elif (ring > 10 and ring <=20):
            pt[1] = pt[1] + 1
        else:
            pt[2] = pt[2] + 1
    '''
    second, calc gini impurity
    '''
    gini = 1 - math.pow(pt[0]/datacount, 2) - math.pow(pt[1]/datacount,2) \
    - math.pow(pt[2]/datacount,2)
    
    return round(gini, 3)

def calcGain(trainset, feature):
    return 0