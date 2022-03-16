# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 11:16:48 2022

@author: ussama
"""
#list of tuple(name,profit value,weight)
items = [('avacado',2.2,170),('pomelo',8,1500),('durian',22,1500),('cucamelon',0.26,15),
         ('lychee',0.4,20),('star apple',1,200)]

#Greedy approximation
def greedy_fruit(items,capacity):
    items =  sorted(items,key=lambda item:item[1],reverse=True)
    print(items)
    
    
greedy_fruit(items, 2000 )
    