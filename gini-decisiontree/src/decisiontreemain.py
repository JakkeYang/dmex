'''
   Decision tree main utils
   
   Author: Ke Yang
   mailto: jakke.yang@gmail.com
'''
from fileutils import getAbaloneDataset
from kmean import kmean
import commonalgo as ca

'''
greedy recursive algorithm
'''
def main():
    dataset = getAbaloneDataset()
    
    ca.find_best_split(dataset)
    
main()