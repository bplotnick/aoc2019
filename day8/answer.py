#!/usr/bin/env python3
import numpy as np

# Part 1
shape = (-1, 6, 25)
with open('input.txt') as f:
    vals = f.read().strip()
a = np.array([int(x) for x in vals])
a = np.reshape(a, shape)
minlayer = np.argmin(np.sum(a==0, axis=(1,2)))
b = a[minlayer,:,:]
print(np.sum(b==1)*np.sum(b==2))

# Part 2
result = np.full_like(a[0,:,:], 2)
# Can probably use ufuncs to do this loop entirely in C
for i in range(a.shape[0]):
    layer = a[i,:,:]
    result = np.where(np.logical_and(result == 2, layer != 2), layer, result)
print(result)
