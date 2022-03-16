# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:49:26 2022

@author: ussama
"""
graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
        }
#traversing thorugh graph
visited_node = [] #list for visited node
queue = []        # initialize a queue
def bfs(visited_node, graph, node):
    visited_node.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print (m,end = " ")
        for neighbours in graph[m]:
            if neighbours not in visited_node:
                visited_node.append(neighbours)
                queue.append(neighbours)


print("Following is the BFS")
bfs(visited_node, graph, '5')    







                