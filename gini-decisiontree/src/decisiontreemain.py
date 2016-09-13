'''
   Decision tree main utils
   
   Author: Ke Yang
   mailto: jakke.yang@gmail.com
'''
from fileutils import getAbaloneDataset
from kmean import kmean
from treeutils import genTreeGraph
import commonalgo as ca

GLOBAL_ATTRIB_NAME_LIST = ['Sex', 'Length', 'Diameter','Height' \
                    ,'Whole weight', 'Shucked weight' \
                    ,'Viscera weight', 'Shell weight', 'Rings']

GLOBAL_ATTRIB_TYPE_LIST = ['n', 'c', 'c', 'c', 'c'
                           , 'c', 'c', 'c', 'i']

'''
greedy recursive algorithm
'''
def main():
    dataset = getAbaloneDataset()
    ca.treeGrowth(dataset, GLOBAL_ATTRIB_NAME_LIST, GLOBAL_ATTRIB_TYPE_LIST, None)
    genTreeGraph (ca.GLOBAL_NODES)
main()