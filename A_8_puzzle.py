# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:11:37 2022

@author: ussama
"""
#using misplaced tiles , manhattan is due
#9func for formatted output
def print_in_format(matrix):
    for i in range(9):
        if i%3 == 0 and i > 0:
            print("")
        print(str(matrix[i])+" ", end = "")


def count(s):
    c = 0   #6 misplaced tiles number, will be returned after operation
    ideal = [1, 2, 3,
             4, 5, 6,
             7, 8, 0]
    for i in range(9):
        if s[i] != 0 and s[i] != ideal[i]:
            c += 1
    return c
#1 A* algo using misplaced tiles heuristics


def move(ar, p, st):
    rh = 999999
    store_st = st.copy()
    
    for i in range(len(ar)):
        dupl_st = st.copy()
        
        temp = dupl_st[p]
        dupl_st[p] = dupl_st[arr[i]]
        dupl_st[arr[i]] = temp
        
        tmp_rh = count(dupl_st)
        
        if tmp_rh < rh:
            rh = tmp_rh
            store_st = dupl_st.copy()
            
    return store_st, rh


#2create puzzle, will have some random state
state = [1, 2, 3,
         0, 5, 6,
         4, 7, 8]
#3create a function to identify displacment of tile
# 4create a variable to store value resulted from function
#5identify : comapre the change between new and old to count the tiles displacement
h = count(state)
Level = 1 #7keep track of A* search levels

#10to print every level of puzzle search
while h>0:
    pos = int(state.index(0))
    
    Level += 1
    #11 locate blank to make a move
    if pos == 0: #if at index 0 of matrix
        arr = [1, 3]
        state, h = move(arr, pos, state)
    elif pos == 1: #if at index 1 of matrix
        arr = [0, 2, 4]
        state, h = move(arr, pos, state)
    elif pos == 2: #if at index 2 of matrix
        arr = [1, 5]
        state, h = move(arr, pos, state)
    elif pos == 3: #if at index 3 of matrix
        arr = [0, 4, 6]
        state, h = move(arr, pos, state)
    elif pos == 4: #if at index 4 of matrix
        arr = [1, 3, 5, 7]
        state, h = move(arr, pos, state)
    elif pos == 5: #if at index 5 of matrix
        arr = [2, 4, 8]
        state, h = move(arr, pos, state)
    elif pos == 6: #if at index 6 of matrix
        arr = [3, 7]
        state, h = move(arr, pos, state)
    elif pos == 7: #if at index 7 of matrix
        arr = [4, 6, 8]
        state, h = move(arr, pos, state)
    elif pos == 8: #if at index 8 of matrix
        arr = [5, 6]
        state, h = move(arr, pos, state)
        
    print("\n------Level " +str(Level)+"----")
    print_in_format(state) #8 to get the output as puzzle look
    print("\nHeuristic Value(Misplaced) : "+str(h))

  




      