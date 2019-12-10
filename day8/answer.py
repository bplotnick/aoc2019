#!/usr/bin/env python3
import numpy as np

shape = (-1, 6, 25)
#shape = (-1, 2, 3)
with open('input.txt') as f:
    vals = f.read().strip()
#vals = "123456789012"
a = np.array([int(x) for x in vals])
a = np.reshape(a, shape)
minlayer = np.argmin(np.sum(a==0, axis=(1,2)))
b = a[minlayer,:,:]
print(np.sum(b==1)*np.sum(b==2))
