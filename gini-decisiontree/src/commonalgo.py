'''
   Common Algorithm
   
   Author: Ke Yang
   mailto: jakke.yang@gmail.com
'''
from __future__ import division
from kmean import kmean
from copy import copy

class Root:
    __slots__ = ('name', 'attrib', 'attribtypes', 'child', 'childnode','parent')
    def __init__(self, name, attr, types, splittedChildLists, p):
        self.name = name
        self.child = splittedChildLists
        self.childnode = []
        self.attrib = attr
        self.attribtypes = types
        self.parent = p
    
    # once child find its best split dimen, set its name as the best attr name
    def addChildNode(self, node):
        self.childnode.append(node)
        
GLOBAL_NODES = []


# the classify attribute is ordinal, need to be classified first
def classifyDataset(pt, ring):
    if ring > 0 and ring <= 10:
        pt[0] = pt[0] + 1
    elif ring > 10 and ring <= 20:
        pt[1] = pt[1] + 1
    else:
        pt[2] = pt[2] + 1

# similar with entropy, much easier to calculate
def calcGini(branchset):
    ## first, calc classification percent
    datacount = len(branchset)
    
    if datacount == 0:
        return 0.0
    
    pt = [0,0,0]
    for entry in branchset:
        ring = int(entry[-1])
        classifyDataset(pt, ring)
        
    ## second, calc gini impurity
    gini = 1 - (pt[0]/datacount) ** 2 - (pt[1]/datacount) ** 2 \
    - (pt[2]/datacount) ** 2
    
    return round(gini, 3)

def calcNominalGain(dataset, dimenid, nominal, tmpDict):
    baseGini = calcGini(dataset)
    baseCount = float(len(dataset))
    subSumGini = 0.0
    
    subDatasetList = []
    for n in nominal:
        subDataset = []
        for d in dataset:
            v = copy(d)
            del(v[dimenid])
            if d[dimenid] == n:
                subDataset.append(v)
                
        subDatasetList.append(subDataset)
        prcntOf = len(subDataset) / baseCount
        subSumGini += prcntOf * calcGini(subDataset)
    
    tmpDict[dimenid] = subDatasetList
    return round(baseGini - subSumGini, 3)

# calcuate info gain, bigger the better
def calcContinuousGain(dataset, dimenid, tmpDict):
    ## firstly, calculate parent gini (base gini)
    baseGini = calcGini(dataset)
    baseCount = float(len(dataset))
    ## continuous feature to discrete feature, 3 routes
    ## return value:
    ##  [0] cluster centers list: group boundary
    ##  [1] points: grouped dataset 
    retValues = kmean(dataset, dimenid, 3)
    subSumGini = 0.0
    
    subDatasetList = []
    for g in retValues[0]:
        groupedDataset = getGroupedDateset(retValues[1], g.group)
        prcntOf = len(groupedDataset) / baseCount
        subSumGini += prcntOf * calcGini(groupedDataset)
        subDatasetList.append(groupedDataset)
    
    tmpDict[dimenid] = subDatasetList
    return round(baseGini - subSumGini, 3)

# get k-mean grouped dataset
def getGroupedDateset(points, group):
    retList = []
    for p in points:
        if p.group == group:
            retList.append(p.v)
    return retList

def createdNode(dimenid, children, attrib, types, parentNode):
    name = attrib[dimenid]
    del (attrib[dimenid])
    del (types[dimenid])
    
    node = Root(name, attrib, types, children, parentNode)
    return node

# find the biggest gain, which split considered as the best
def find_best_split(dataset, types):
    tempDict = {}
    bestGain = 0.0
    bestGainDimenID = 0
    
    for dimenid, t in enumerate(types):
        if t == 'n':
            ## dimen is a classify attribute
            subGain = calcNominalGain(dataset, dimenid, ['M','F','I'], tempDict)
#             print (subGain)
            if subGain > bestGain:
                bestGain = subGain
                bestGainDimenID = dimenid
        elif t == 'c':
            ## dimens is continuous attribute
            subGain = calcContinuousGain(dataset, dimenid, tempDict)
#             print (subGain)
            if subGain > bestGain:
                bestGain = subGain
                bestGainDimenID = dimenid
        else:
            if len(dataset[0]) > 1:
                break
            else:
                bestGain = 0.0
                bestGainDimenID = dimenid

    if bestGain != 0.0:
        indics = tempDict.keys()
        for indx in indics:
            if indx != bestGainDimenID:
                tempDict.pop(indx)
    else:
#         print ('best split:')
#         print (bestGain, bestGainDimenID, len(dataset))
        return (bestGain, bestGainDimenID, dataset)   
          
#     print ('best split:')
#     print (bestGain, bestGainDimenID, len(tempDict[bestGainDimenID]))
    return (bestGain, bestGainDimenID, tempDict[bestGainDimenID])

def classify():
    return

def stopping_cond(dataset):
    if len(dataset) == 0 or len(dataset[0]) == 2:
        return True
    else:
        return False

def treeGrowth(dataset, attribset, attribtype, parentN):
    if (stopping_cond(dataset)):
        return

    b = find_best_split(dataset, attribtype)
    node = createdNode(b[1], b[2], copy(attribset), copy(attribtype), parentN)
    
    if not parentN is None:
        parentN.addChildNode(node)
        
    GLOBAL_NODES.append(node)
    
    if b[0] == 0.0:
        return

    for subDataset in node.child:
        treeGrowth(subDataset, node.attrib, node.attribtypes, node)


    