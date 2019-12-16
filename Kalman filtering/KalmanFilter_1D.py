#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 04:00:05 2019

@author: MyReservoir
"""

# 1-D Kalman Filter Implementation

from math import *

def gaussian(mu, sigma2, X):
    f=1/(sqrt(2 * pi * sigma2))* exp(-0.5*((X-mu)**2)/sigma2)
    return f

def update(mean1, var1, mean2, var2):
    # Measurement Update Function
    new_mean = (mean1*var2 + mean2*var1)/(var1+var2)
    new_var =1/((1/var1)+(1/var2))
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    # Motion Update Function
    new_mean= mean1 + mean2
    new_var= var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.     # Initial mean
sig = 10000.  # Initial Sigma (very high- highly uncertain)


for i in range(len(measurements)):
    [mu, sig]= update(measurements[i],measurement_sig, mu, sig)
    [mu, sig]= predict(motion[i],motion_sig,mu,sig)
    
print([mu,sig])

print(gaussian(10,4,10))
print(update(10.,4.,12., 4.))
print(predict(10,4,12,4))