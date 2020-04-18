#!python

import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
import random
import time


msize = 100
viruslife = 14
Nreproduction = 1.7  # tokyo's number of infection from a man
isolationRate = 0.1
preventtime = 30  #isolationRate change timing
preventrate = 0.1   #preventrate 1==unchange
infectrate = Nreproduction*isolationRate
rod=0.02 # rate of die
initialrate= 0.001   # 0.0005 initial infected rate0.5%

recovered = viruslife+1
death = recovered * 10
level1 = recovered + viruslife

initialinfected = msize*msize*initialrate
# Cells state
#
# 0 noinfect
# 15 recovered
# 29 infect
# 150 death

Ug = np.zeros((msize, msize), float)

def infectp(c):
    return 1 if (c % recovered ) != 0 else 0

def infecttrial(neighborsList):
        #print(neighborsList)
        p = 0
        for c in neighborsList:
                if c % recovered != 0 :
                        if infectrate > random.random():
                                p = p + 1
        #print("{}  ".format(p))
        return  p
   
   
def transarray(U,f):
    U_next = f(U)
    return U_next

def countarray(U,f):
        c = 0
        return c

def neighborList(U, x, y):
    dxL = dxR = dyU = dyD = 1
    msize = len(U)
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
    elif y == msize-1 :
        dyU = 1
        dyD = -(msize-1)

    #print(x,y, dxL,dxR,dyU,dyD)
    #U_neighbor = np.array([[U[x-1, y-1], U[x-1, y], U[x-1, y+1]],
    #                       [U[x  , y-1], U[x  , y], U[x  , y+1]],
    #                       [U[x+1, y-1], U[x+1, y], U[x+1, y+1]]])

    U_neighborList = [U[x-dxL, y-dyU], U[x-dxL, y], U[x-dxL, y+dyD],
                      U[x    , y-dyU],              U[x    , y+dyD],
                      U[x+dxR, y-dyU], U[x+dxR, y], U[x+dxR, y+dyD]]
                      
     #U_neighbor = np.array([[U[x-dxL, y-dyU], U[x-dxL, y], U[x-dxL, y+dyD]],
     #                                          [U[x    , y-dyU], U[x    , y], U[x    , y+dyD]],
     #                                          [U[x+dxR, y-dyU], U[x+dxR, y], U[x+dxR, y+dyD]]])
    return U_neighborList


def infect(U):
    mx = len(U)
    U_next = np.zeros_like(U)
    for i in range(mx):
        my = len(U[i])
        for j in range(my):
            cell = U[i][j]
            if cell % recovered == 0 :
                if cell < recovered: # no infected
                    neighbors = neighborList(U , i, j)
                    p = infecttrial(neighbors)
                    if p  >= 1:
                        U_next[i][j] = level1
                    else:
                        U_next[i][j] = cell
                else: ## death
                    U_next[i][j] = cell
            else : # infected
                if cell != recovered:
                    if rod > random.random() :
                        U_next[i][j] = death
                    else:
                        U_next[i][j] = cell - 1
                else:
                    U_next[i][j] = cell
    return U_next


def initcells(U, rate , initv ):
    for i in range(len(U)):
        for j in range(len(U[i])):
            r = random.random()
            #print(rate,r,initv , initv if rate > r  else 0)
            U[i][j] = initv if rate > r  else 0
    return U



def testinit(U):
    v = 1
    mx = len(U)
    for i in range(mx):
        my = len(U[i])
        for j in range(my):
                U[i][j] = v
                v+=1
    return U


#infected = np.frompyfunc(lambda x: 1 if x >= recovered else 0, 1, 1)
#noinfected = np.frompyfunc(lambda x: 1 if x == 0 else 0, 1, 1)
#testfunc = np.frompyfunc(lambda x : 0 , 1 , 1)

Ug = initcells(Ug, initialrate , level1)

## reference
## https://qiita.com/krrka/items/e5c0720ac6382e61dc60
##
fig = plt.figure()
ax = fig.add_subplot(111)
img = ax.imshow(Ug, interpolation="nearest") #, cmap=plt.cm.gray)

def plotgraph(plt, time, noinfect, infected, recovered, death):
    plt.plot(time, noinfect)
    plt.plot(time, infected)
    plt.plot(time, recovered)
    plt.plot(time, death)
    plt.show()
    
elapsed = 0
print('time,no infect,total infected, recovered, death, infectrate')

N_time=[]
N_noinfect=[]
N_infected=[]
#N_infected_today=[]
N_recovered=[]
#N_recovered_today=[]
N_death=[]

n_noinfect = np.count_nonzero(Ug == 0)
n_recovered = np.count_nonzero(Ug == recovered)

while True:
        Ug=infect(Ug)
        #print(Ug)
        img.set_data(Ug)
        ax.set_title("t = {}".format(elapsed))

        #n_pre_noinfect = n_noinfect
        #n_pre_recovered = n_recovered
        
        n_noinfect = np.count_nonzero(Ug == 0)
        n_infected = np.count_nonzero(Ug % recovered > 0)
        #n_infected_today = n_noinfect - n_pre_noinfect
        
        n_recovered = np.count_nonzero(Ug == recovered)
        #n_recovered_today = n_recovered - n_pre_recovered
        
        n_death = np.count_nonzero(Ug == death)
        
        N_time.append( elapsed )
        N_noinfect.append( n_noinfect )
        N_infected.append( n_infected )
        N_recovered.append( n_recovered )
        N_death.append( n_death )
        #N_infected_today.append( n_infected_today )
        #N_recovered_today.append( n_recovered_today )

        print('{},{},{},{},{},{}'.format(elapsed, n_noinfect, n_infected, n_recovered, n_death, infectrate))

        if n_infected == 0:
            break

        if elapsed == preventtime :
            infectrate = infectrate * preventrate
        
        #time.sleep(1)
        plt.pause(0.01)
        elapsed += 1

input("Close Figure Window.")        
plt.plot(N_time, N_infected, N_death)
plt.show()
#plotgraph(plt , N_time, N_noinfect, N_infected, N_recovered)
