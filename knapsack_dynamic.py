# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 14:31:02 2022

@author: ussama
"""
#optimal value
#list of tuple(name,profit value,weight)
items = [('avacado',2.2,170),('pomelo',8,1500),('durian',22,1500),('cucamelon',0.26,15),
         ('lychee',0.4,20),('star apple',1,200)]

#Dynamic Programming technique
def dynamic_fruit(items,capacity):
    bag = [0 for i in range(capacity+1)] #construct bag
    for i in range(capacity+1):          #preparation of main loop,declaration of loop
        for j in range(len(items)):      # 1st check all the fruits
            _,value,weight = items[j]    # unpack items list tuple with a prespective/info of profit and weight
            if (weight < i):
                bag[i] = max(bag[i],bag[i-weight]+value) 
                                        #while checking every fruit ,only 2 choices are left
                                        # Min or Max.we pick MAX. Max will work by comparing two situations
                                        #with fruit not added, with fruit and its effect added
    return round(bag[capacity])
        
        
print(dynamic_fruit(items, 2000))        