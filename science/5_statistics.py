
from __future__ import division
from collections import Counter

num_friends = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def mean(x):
    return sum(x) / len(x)

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1: # odd
        return sorted_v[midpoint]
    else: # even
        lo, hi = midpoint - 1, midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

# returns a value that belongs to the p-quartile of the x value
def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]

quantile(num_friends, 0.10) # 1
quantile(num_friends, 0.90) # 13

# return list if there is more than one mode
# mode is most frequent value in the data
def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x for x, count in counts.iteritems()
            if count == max_count]

def data_range(x):
    return max(x) - min(x)

# substract the average at all data points in x.
# to make the average zero 
def de_mean(x):
    x_bar = mean(x)
    return [x - x_bar for x in x]

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

# variance is the calculation of how far one variable is from the average.
# assume that there are two or more data points in x
def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviation) / (n - 1)

import math
def standard_deviation(x):
    return math.sqrt(variance(x)) # 9.03

# the more stable method is to calculate the difference value between upper 25% and lower 25%
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25) # 6

# covariance is used to calculate how far two variable are from the average.
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1) # 22.43

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y # 0.25
    else:
        return 0 # if there is no deviation, correlation is 0
