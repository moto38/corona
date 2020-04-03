#!python

import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
import random

msize = 10
viruslife = 14
infectrate = 1.7/8  # tokyo's number of infection from a man
level1 = 10
level2 = 10
initialrate= 0.02   # initial infected rate 2%
initialinfected = msize*msize*initialrate
# Cells state
#
# 0 noinfect
# 10 recovered type 1
# 19 infect type 1
# 20 recovered type 2
# 29 infect type 2

Ug = np.zeros((msize, msize), float)

def infectp(c):
    return 1 if (c % 10) != 0 else 0

def infecttrial(neighborsList):
    for c in range(neighborsList):
        if c 
    
    return 0.1
   
def transarray(U,f):
    U_next = np.zeros_like(U)
    f(U_next)
    return U_next


def neighbor(U, x, y):
    dxL = dxR = dyU = dyD = 1
    
    #
    # cyclic boundary condition
    #
    if x == 0 :
        dxL = -(msize-1)  # cyclic
        dxR = 1
    elif x == msize-1 :
        dxL = 1
        dxR = -(msize-1)

    if y == 0 :
        dyU = -(msize-1)  # cyclic
        dyD = 1
    elif x == msize-1 :
        dyU = 1
        dyD = -(msize-1)

    
    #U_neighbor = np.array([[U[x-1, y-1], U[x-1, y], U[x-1, y+1]],
    #                       [U[x  , y-1], U[x  , y], U[x  , y+1]],
    #                       [U[x+1, y-1], U[x+1, y], U[x+1, y+1]]])

    U_neighbor = np.array([[U[x-dxL, y-dyU], U[x-dxL, y], U[x-dxL, y+dyD]],
                           [U[x    , y-dyU], U[x    , y], U[x    , y+dyD]],
                           [U[x+dxR, y-dyU], U[x+dxR, y], U[x+dxR, y+dyD]]])
    return U_neighbor

def neighborList(U, x, y):
    dxL = dxR = dyU = dyD = 1
    
    #
    # cyclic boundary condition
    #
    if x == 0 :
        dxL = -(msize-1)  # cyclic
        dxR = 1
    elif x == msize-1 :
        dxL = 1
        dxR = -(msize-1)

    if y == 0 :
        dyU = -(msize-1)  # cyclic
        dyD = 1
    elif x == msize-1 :
        dyU = 1
        dyD = -(msize-1)

    
    #U_neighbor = np.array([[U[x-1, y-1], U[x-1, y], U[x-1, y+1]],
    #                       [U[x  , y-1], U[x  , y], U[x  , y+1]],
    #                       [U[x+1, y-1], U[x+1, y], U[x+1, y+1]]])

    U_neighborList = [U[x-dxL, y-dyU], U[x-dxL, y], U[x-dxL, y+dyD],
                      U[x    , y-dyU],              U[x    , y+dyD],
                      U[x+dxR, y-dyU], U[x+dxR, y], U[x+dxR, y+dyD]]
    return U_neighborList


def infect(U, mx, my):
    U_next = np.zeros_like(U)
    v = 1
    for i in range(mx):
        for j in range(my):
            neighbors = neighbor(U , i, j)
            p = infecttrial(neighbors)
            if p < infectrate :
                U_next[i][j] = level1
            else:
                U_next[i][j] = U[i][j]
    return U_next


def initcells(U, mx, my , rate , initv ):
    for i in range(mx):
        for j in range(my):
            r = random.random()
            print(rate,r,initv , initv if rate > r  else 0)
            U[i][j] = initv if rate > r  else 0
    return U


def testinit(U, mx , my):
    v = 1
    for i in range(mx):
        for j in range(my):
            U[i][j] = v
            v+=1
    return U



testfunc = np.frompyfunc(lambda x : 0 , 1 , 1)

Ug = testinit(Ug,msize,msize)
Ug = initcells(Ug, msize, msize, initialrate , level1)

print(Ug)
print(neighbor(Ug,1,1))
#U = transarray(Ug, testfunc)
print(neighbor(Ug,0,0))
print(neighborList(Ug,0,0))
print(neighbor(Ug,msize-1,msize-1))
