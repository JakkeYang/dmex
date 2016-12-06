'''
   tree generating utils
   
   Author: Ke Yang
   mailto: jakke.yang@gmail.com
'''
import pydot as pd

def genTreeGraph(nodeList):
    graph = pd.Dot(graph_type='graph')
    for node in nodeList:
        if not node.parent is None:
            # print (node.name+node.parent.name)
#             tmpNode = pd.Node(name=node.name, nodehash=hash(node))
#             tmpParentNode = pd.Node(name=node.parent.name, nodehash=hash(node.parent))
            tmpNode = pd.Node(name=hash(node))
            tmpParentNode = pd.Node(name=hash(node.parent))
            tmpEdge = pd.Edge(tmpParentNode,tmpNode, label=3)
            graph.add_edge(tmpEdge)
#             graph.add_node(tmpNode)
    graph.write_jpeg('decisiontree.jpg', prog='dot')
    return True

# graph = pd.Dot(graph_type='graph')
# e1 = pd.Edge('A','B', label=3)
# e2 = pd.Edge('A','C', label=4)
# graph.add_edge(e1)
# graph.add_edge(e2)
# graph.write_jpeg('hellotree.jpg', prog='dot')