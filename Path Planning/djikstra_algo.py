#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 03:02:01 2019

@author: MyReservoir
"""

# Djikstra Algorithm

# -----------
# User Instructions:
#
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
#
#
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid 
# you return has the value 0.
# ----------


from heapq import heappop,heappush

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']


def relax(u, v, d, cost, q , parent):
    if d[u[0]][u[1]] + cost < d[v[0]][v[1]]:
        d[v[0]][v[1]]=d[u[0]][u[1]] + cost
        parent[v[0]][v[1]]=u
        heappush(q, (d[v[0]][v[1]],v))
    return d, q, parent
        
def find_neighbours(point,delta):
    neighbor=[]
    for i in range(len(delta)):
        x=point[0]+delta[i][0]
        y=point[1]+delta[i][1]
        if 0<= x <=len(grid)-1 and 0<= y <= len(grid[0])-1:
            if grid[x][y]!=1:
                neighbor.append([x,y])
    return neighbor

def find_action(x, y, delta, source):
    for i in range(len(delta)):
        if x-delta[i][0]==source[0] and y-delta[i][1]==source[1]:
            return delta_name[i]
                      
            
def search(grid,init,goal,cost):
    q=[]
    closed=[]
    node_cost=[]
    
    d=[[1000 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    parent=[[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    expand = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    d[init[0]][init[1]]=0
    
    
    heappush(q,(d[init[0]][init[1]],init))
    count=0
    while q:
        u=heappop(q)
        closed.append(u[1])
        node_cost.append(u[0])
        expand[u[1][0]][u[1][1]]=count
        count+=1
        
        neighbours=find_neighbours(u[1], delta)
        
        for v in neighbours:
            if v not in closed:
                d, q, parent=relax(u[1], v, d, cost, q, parent)

     
        
    # Trace back from the goal to the start to print the path
    policy=[[' ' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    x=goal[0]
    y=goal[1]
    #source=parent[x][y]
    policy[x][y]='*'
    
    while x!=init[0] or y!=init[1]:
        source=parent[x][y]
        policy[source[0]][source[1]]= find_action(x, y, delta, source)
        x=source[0]
        y=source[1]
    
    # prints order in which nodes are expanded
    for i in range(len(expand)):
        print(expand[i])
    
    # prints parent nodes
#    print('\n\n')
#    for i in range(len(parent)):
#        print(parent[i])      
     
    # prints path
    print('\n\n')
    for i in range(len(policy)):
        print(policy[i])
    
    # prints distance cost and dest node 
    for i in range(len(closed)):
        if closed[i]==goal:
            path= [node_cost[i], closed[i][0], closed[i][1]]
            return path    
    
    return 'fail'


search(grid,init,goal,cost)


