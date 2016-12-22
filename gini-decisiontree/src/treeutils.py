'''
   tree generating utils
   
   Author: Ke Yang
   mailto: jakke.yang@gmail.com
'''
import matplotlib.pyplot as plt
import math

# node style
leafNodeStyle = dict(boxstyle="round4", fc="0.8")

# arrow style
arrow_args = dict(arrowstyle="<-")

# create new graphic
fig = plt.figure(1, facecolor='white')

#  clear draw region
fig.clf()

# subplot(323) equals to subplot(3,2,3)
#ax1 = plt.subplot(111,frameon=False)

# plot one node
def plotNode(Nodename, centerPt, parentPt, nodeType):
    plt.annotate(Nodename, xy=parentPt, xycoords='axes fraction', \
    xytext=centerPt, textcoords='axes fraction', va="center", ha="center", \
    bbox=nodeType, arrowprops=arrow_args)

# plot the whole tree recursively
def plotTreeGraph(node, px, py, width, parentIndex, level):
    # plot parent
    parentLevelCount = math.pow(3, level-1)
    
    if parentLevelCount == 1:
        separator = width / 2 - 0.2
    else:
        separator = (width - parentLevelCount * 0.2) / (parentLevelCount - 1)
        
    if round(separator, 4) == 0:
        separator = 0.2
        
    x = parentIndex * (separator + 0.2)
    y = 1.0 - level * 0.1
    plotNode(node.name, (x,y), (px,py), leafNodeStyle)
    
    #plot children
    if not node.childnode is None and len(node.childnode) > 0:
        i = 0
        for leafNode in node.childnode:
            plotTreeGraph(leafNode, x, y, width, parentIndex*3 + i, level+1)
            i = i + 1
    
# plot start
def genTreeGraph(nodeList):
    node = nodeList[0]
    width = math.pow(3,7) * 0.1
    plotTreeGraph(node, 0., 1.0, width, 0, 1)
    plt.show()

