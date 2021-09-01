# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 22:40:12 2021

@author: yixing
"""

#set up a rectangle grid 
#first build the nodes 
all_nodes=[]
for x in range(20):
    for y in range(10):
        all_nodes.append([x,y])

print(all_nodes)

#second set up the edges 
def neighbors(node):
    dirs=[[1,0],[0,1],[-1,0],[0,-1]]
    result=[]
    for dir in dirs:
        neighbor=[node[0]+dir[0],node[1]+dir[1]]
        if neighbor in all_nodes:  #check if neighbor in graph 
            result.append(neighbor)
    return result 


        