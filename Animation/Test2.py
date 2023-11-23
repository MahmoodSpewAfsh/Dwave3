from __future__ import division
from vpython import *

L = 2
R = 3

even = []
odd = []

for i in range(-L,L+1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

for i in even:
    for j in even:
        for k in even:
            ball = sphere(pos=vector(i,j+1,k+1),radius=R,color=color.green)

for i in odd:
    for j in odd:
        for k in odd:
            ball = sphere(pos=vector(i,j,k),radius=R,color=color.yellow)