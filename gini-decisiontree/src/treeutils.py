'''
   tree generating utils
   
   Author: Ke Yang
   mailto: jakke.yang@gmail.com
'''
import matplotlib.pyplot as plt

# node style
leafNodeStyle = dict(boxstyle="round4", fc="0.8")

# arrow style
arrow_args = dict(arrowstyle="<-")

# create new graphic
fig = plt.figure(1, facecolor='white')

#  clear draw region
fig.clf()

# subplot(323) equals to subplot(3,2,3)
ax1 = plt.subplot(111,frameon=False)

# plot one node
def plotNode(Nodename, centerPt, parentPt, nodeType):
    ax1.annotate(Nodename, xy=parentPt, xycoords='axes fraction', \
    xytext=centerPt, textcoords='axes fraction', va="center", ha="center", \
    bbox=nodeType, arrowprops=arrow_args)

# plot the whole tree recursively
def plotTreeGraph(node, x, y, px, py):
    plotNode(node.name, (x,y), (px,py), leafNodeStyle)
    if not node.childnode is None and len(node.childnode) > 0:
        # calculate chilren's start width
        count = len(node.childnode)
        startX = x - 0.04 * count
        i = 0
        for leafNode in node.childnode:
            sx = startX + i * 0.2
            sy = y - 0.1
            i = i + 1
            plotTreeGraph(leafNode, sx, sy, x, y)
    
# plot start
def genTreeGraph(nodeList):
    node = nodeList[0]
    plotTreeGraph(node, 0.5, 1.0, 0.5, 1.0)
    plt.show()

