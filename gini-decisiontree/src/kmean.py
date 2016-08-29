'''
   K-mean++ algorithm
   
   Ke reduced dimensions from 2D to 1D
   
   Collected from:
   http://rosettacode.org/wiki/K-means%2B%2B_clustering
'''
from math import pi, sin, cos
from collections import namedtuple
from random import random, choice
from copy import copy
from fileutils import getAbaloneDataset
 
try:
    import psyco
    psyco.full()
except ImportError:
    pass
 
 
FLOAT_MAX = 1e100
 
 
class Point:
    __slots__ = ["x", "v", "group"]
    def __init__(self, x=0.0, v=None, group=0):
        self.x, self.group = x, group
 
 
def generate_points(dataset, dimenid):
    points = [Point() for _ in range(len(dataset))]
 
    # note: this is not a uniform 2-d distribution
    for i, p in enumerate(points):
        p.x = float(dataset[i][dimenid])
        p.v = dataset[i]
    return points
 
 
def nearest_cluster_center(point, cluster_centers):
    """Distance and index of the closest cluster center"""
    def sqr_distance_2D(a, b):
        return (a.x - b.x) ** 2
 
    min_index = point.group
    min_dist = FLOAT_MAX
 
    for i, cc in enumerate(cluster_centers):
        d = sqr_distance_2D(cc, point)
        if min_dist > d:
            min_dist = d
            min_index = i
 
    return (min_index, min_dist)
 
 
def kpp(points, cluster_centers):
    ## random point in points
    cluster_centers[0] = copy(choice(points))
    
    ## same size new list initialized with 0.0
    d = [0.0 for _ in range(len(points))]
 
    ## iterator from cluster centers, note:
    ##   the first cluster center is random from points
    for i in range(1, len(cluster_centers)):
        sum = 0
        for j, p in enumerate(points):
            ## get the distance between cluster center[i] and points[j]
            d[j] = nearest_cluster_center(p, cluster_centers[:i])[1]
            
            ## sum all distance
            sum += d[j]
 
        ## random [0,1)
        sum *= random()
 
        ## now sum is a value from 0 to previous sum
        for j, di in enumerate(d):
            sum -= di
            if sum > 0:
                continue
            
            ## distance[j] let random sum less than 0
            ##  then points[j] is the new cluster center
            cluster_centers[i] = copy(points[j])
            break
 
    for p in points:
        p.group = nearest_cluster_center(p, cluster_centers)[0]
 
 
def lloyd(points, nclusters):
    cluster_centers = [Point() for _ in range(nclusters)]
 
    # call k++ init
    kpp(points, cluster_centers)
 
    lenpts10 = len(points) >> 10
 
    changed = 0
    while True:
        # group element for centroids are used as counters
        ## reset
        for cc in cluster_centers:
            cc.x = 0
            cc.v = None
            cc.group = 0
 
        for p in points:
            cluster_centers[p.group].group += 1
            cluster_centers[p.group].x += p.x
 
        for cc in cluster_centers:
            cc.x /= cc.group
 
        # find closest centroid of each PointPtr
        changed = 0
        for p in points:
            min_i = nearest_cluster_center(p, cluster_centers)[0]
            if min_i != p.group:
                changed += 1
                p.group = min_i
 
        # stop when 99.9% of points are good
        if changed <= lenpts10:
            break
 
    for i, cc in enumerate(cluster_centers):
        cc.group = i
 
    return cluster_centers

def kmean(dataset, dimenid, k):
    points = generate_points(dataset, dimenid)
    cluster_centers = lloyd(points, k)
    return (cluster_centers, points)
    