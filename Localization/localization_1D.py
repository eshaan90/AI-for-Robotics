#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 01:15:44 2019

@author: MyReservoir
"""


# Udacity's AI for Robotics Course  Lesson 1: Localization Overview

'''
Summary of the methods involved in Localization:
    
    Belief=Probability
    Sense= Product followed by normalization
    Move= convolution (=addition)

'''


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green','red','red','green','green']
measurements=['red','green']
motions=[1,1]
pHit=0.6    # Prob of seeing the door
pMiss=0.2   # Prob of not seeing the door
pExact=0.8
pOvershoot=0.1
pUndershoot=0.1

def sense(p,Z):
    q=[]
    for i in range(len(p)):
        hit= (Z==world[i])
        q.append(p[i]* (hit*pHit+(1-hit)*pMiss))
    s=sum(q)
    for i in range(len(q)):
        q[i]=q[i]/s
    return q

def move(p,U):
    q=[]
    for i in range(len(p)):
        s=pExact*p[(i-U)% len(p)]
        s=s+pOvershoot*p[(i-U-1)%len(p)]
        s=s+pUndershoot*p[(i-U+1)%len(p)]
        q.append(s)
    return q

for i in range(len(measurements)):
    p=sense(p,measurements[i])
    p=move(p,motions[i])
    
print(p)