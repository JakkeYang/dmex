'''
   tree generating utils
   
   Author: Ke Yang
   mailto: jakke.yang@gmail.com
'''
import pydot as pd

def genTreeGraph(nodeList):
    for node in nodeList:
        if not node.parent is None:
            print (node.name+node.parent.name)
    return True

# graph = pd.Dot(graph_type='graph')
# e1 = pd.Edge('A','B', label=3)
# e2 = pd.Edge('A','C', label=4)
# graph.add_edge(e1)
# graph.add_edge(e2)
# graph.write_jpeg('hellotree.jpg', prog='dot')