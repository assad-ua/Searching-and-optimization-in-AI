# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 11:28:22 2022

@author: ussama
"""

#list of tuple(name,profit value,weight)
items = [('avacado',2.2,170),('pomelo',8,1500),('durian',22,1500),('cucamelon',0.26,15),
         ('lychee',0.4,20),('star apple',1,200)]

#Greedy approximation
def greedy_fruit(items,capacity):
    items =  sorted(items,key=lambda item:item[1],reverse=True)
    chosen_frutis = {}
    profit = 0
    for i in range(len(items)):
        name,value,weight = items[i] #final arrangment after applying algo
        num_of_fruit = (capacity - capacity % weight) / weight #quantify fruits
        chosen_frutis[name] = num_of_fruit #key for dictionary
        capacity = capacity % weight #remainder of capacity by weight
        profit += num_of_fruit*value
    return round(profit,2),chosen_frutis



print(greedy_fruit(items, 2000))
