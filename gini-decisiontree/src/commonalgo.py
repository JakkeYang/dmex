'''
   Common Algorithm
   
   Author: Ke Yang
   mailto: jakke.yang@gmail.com
'''
from __future__ import division
from kmean import kmean

'''
the classify attribute is ordinal, need to be classified first
'''
def classifyDataset(pt, ring):
    if (ring > 0 and ring <= 10):
        pt[0] = pt[0] + 1
    elif (ring > 10 and ring <= 20):
        pt[1] = pt[1] + 1
    else:
        pt[2] = pt[2] + 1

'''
similar with entropy, much easier to calculate
'''
def calcGini(branchset):

    ## first, calc classification percent

    datacount = len(branchset)
    pt = [0,0,0]
    for entry in branchset:
        ring = int(entry[-1])
        classifyDataset(pt, ring)
        
    ## second, calc gini impurity
    gini = 1 - (pt[0]/datacount) ** 2 - (pt[1]/datacount) ** 2 \
    - (pt[2]/datacount) ** 2
    
    return round(gini, 3)

'''
calcuate info gain, bigger the better
'''
def calcGain(dataset, dimenid):
    ## firstly, calculate parent gini (base gini)
    baseGini = calcGini(dataset)
    baseCount = float(len(dataset))
    ## continuous feature to discrete feature, 3 routes
    ## return value:
    ##  [0] cluster centers list: group boundary
    ##  [1] points: grouped dataset 
    retValues = kmean(dataset, dimenid, 3)
    subSumGini = 0.0
    
    for g in retValues[0]:
        groupedDataset = getGroupedDateset(retValues[1], g.group)
        prcntOf = len(groupedDataset) / baseCount
        print(dimenid, g.group, len(groupedDataset))
        subSumGini += prcntOf * calcGini(groupedDataset)
        
    
    return baseGini - subSumGini

'''
get k-mean grouped dataset
'''
def getGroupedDateset(points, group):
    retList = []
    for p in points:
        if p.group == group:
            retList.append(p.v)
    return retList

def createdNode():
    return

def find_best_split(dataset):
    bestGain = 0.0
    bestGainDimenID = 1
    for dimenid in range(1, len(dataset[0])-1):
        subGain = calcGain(dataset, dimenid)
        
        if subGain > bestGain:
            bestGain = subGain
            bestGainDimenID = dimenid
            
    print (bestGain, bestGainDimenID)

def classify():
    return

def stopping_cond():
    return