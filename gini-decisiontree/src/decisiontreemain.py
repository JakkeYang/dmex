'''
   Decision tree main utils
   
   Author: Ke Yang
   mailto: jakke.yang@gmail.com
'''
from fileutils import getAbaloneDataset
import commonalgo

def main():
    dataset = getAbaloneDataset()
    print commonalgo.calcGini(dataset)

main()