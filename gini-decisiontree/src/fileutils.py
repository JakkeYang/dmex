'''
   File utilities
   
   Author: Ke Yang
   mailto: jakke.yang@gmail.com
'''

def getAbaloneDataset():
    dataset = []
    file_obj = open('../dataset/abalone.data')
    for line in file_obj:
        dataset.append(line.strip().split(','))
    return dataset