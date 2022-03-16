# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:26:14 2022

@author: ussama
"""

#list of tuple(name,profit value,weight)
items = [('avacado',2.2,170),('pomelo',8,1500),('durian',22,1500),('cucamelon',0.26,15),
         ('lychee',0.4,20),('star apple',1,200)]

#bruteforce algo
def brute_fruit(items, capacity):
    bag = []
    weight = 0
    value = 0
    for item in range(len(items)):
        w = sum([item[1] for item in items])
        v = sum([item[2] for item in items])
        if v > value and w <= capacity:
            value = v
            weight = w
            bag = item
    return bag, weight, value

print(brute_fruit(items, 2000))