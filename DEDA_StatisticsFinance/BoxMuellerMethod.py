#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:44:44 2019

@author: haerdle and the students of the St Gallen SDA class 2019
"""

# Using the Box-Mueller Method to generate 2-dim normally distributed variables

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)  # Set seed from comparability

# For mu = (0,0), covariance matrix Sigma = identity matrix
n = 500  # Number of random numbers
msize = 2  # determines the size of the plotted points
# a good size might be msize=5 for n=500 pts and msize=0.1 for n>50K  
a = np.random.exponential(scale=1, size=n)
phi = np.random.uniform(low=0, high=2 * np.pi, size=n)

# change to cartesian coordinates
x = a * np.cos(phi)
y = a * np.sin(phi)

plt.figure(figsize=(7, 7))
plt.plot(x, y, '.r', markersize=msize)
plt.savefig('2dimnormal.png', dpi = 300, transparent = True)

# for covariance matrix Sigma = A: Y = X/sqrt(Sigma) ~ N(0,I) => Y*sqrt(Sigma)

# Calculate sqrt(A) with Jordan decomposition
A = [[3, 1], [1, 1]]
A_eig = np.linalg.eig(A)
E_val = A_eig[0]
Gamma = A_eig[1]
Lambda = np.diag(E_val)
np.sqrt(Lambda)
Lambda12 = np.sqrt(Lambda)
A12 = np.dot(np.dot(Gamma, Lambda12), np.transpose(Gamma))

# Solve with matrix multiplication
c = [x, y]
tfxy = np.dot(A12, c)

# print(N)
plt.figure(2, figsize=(8, 6))
plt.plot(tfxy[0], tfxy[1], '.r', markersize=msize)
plt.savefig('2dimnormalwithcov.png', dpi = 300, transparent = True)