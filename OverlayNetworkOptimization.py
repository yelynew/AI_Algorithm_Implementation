# -*- coding: utf-8 -*-

#########################################################
#                                                       #
#       Assignment 2: GENETIC ALGORITHM APPLIED TO      #
#       OVERLAY NETWORK OPTIMIZATION                    #    
#                                                       #
# 		Author:                                         #
#                                                       #
#       Student ID:                                     #
#                                                       #
#		Please DO NOT publish your implemented code     #
#       for example on GitHub							#
#                                                       #
#########################################################

import random
import numpy as np
import matplotlib.pyplot as plt


#########################################################
# PARAMETERS                                            #
#########################################################
popSize = 100
chromLength = 300
iteration_max = 1000   
crossover_rate = 0.7
mutation_rate = 0.001 

fitness = np.empty([popSize])                               
costVector = np.empty([chromLength])


#########################################################
# Load network                                          #
#########################################################
def loadNetwork():
    fname = "C:\\Users\\yyoo2\\OneDrive\\바탕 화면\\강의자료\\AI\\network.txt"
    input = np.loadtxt(fname)
    for i in range(0,chromLength):
        costVector[i]=input[i][2]
        #print(costVector[i])
  

#########################################################
# FITNESS EVALUATION                                    #
#########################################################         
def evaluateFitness(chromosome,best):
    costFullyConnectedNetwork=30098.059999999983
    fitness_total=0.0;
    fitness_average=0.0;
    
    for i in range(0,popSize):
        fitness[i]=0

    for i in range(0,popSize):
        cost=0
        for j in range(0,chromLength):        
            if chromosome[i,j]==1:
                cost=cost+costVector[j]
        fitness[i]=1-(cost/costFullyConnectedNetwork)
        print(fitness[i])
        fitness_total=fitness_total+fitness[i]
    fitness_average=fitness_total/popSize

    for i in range(0,popSize):
        if fitness[i]>=best:
            best = fitness[i]
            
    return best, fitness_average
    
        
#########################################################
# PERFORMANCE GRAPH                                     #
#########################################################
def plotChart(best,avg):
    plt.plot(best,label='best')
    plt.plot(avg,label='average')
    plt.ylabel('Fitness')
    plt.xlabel('Iterations')
    plt.legend()
    plt.xlim(1,iteration_max-1)    
    plt.ylim(0.0, 1.0)
    plt.show()
#########################################################
# GENETIC CHROMOSOME                                    #
#########################################################

def genetic():
    chromosome = []
    alist=[]
    for i in range(24):
        a=random.randint(0,chromLength)
        while a in alist:
            a=random.randint(0,chromLength)
        alist.append(a)
    for i in range(0, popSize):
        for j in range(0,chromLength):
            if j in alist:
                chromosome[i][j]=1
            else:
                chromosome[i][j]=0
    return chromosome


#########################################################
# MAIN                                                  #
#########################################################
if __name__ == '__main__':
    best=0.0
    average=0.0
    iteration=0
    loadNetwork
    c=genetic
    evaluateFitness(c,0)
    
    bestM = np.empty([iteration_max],dtype=np.float32);
    averageM = np.empty([iteration_max],dtype=np.float32);
    print("GENETIC ALGORITHM APPLIED TO OVERLAY NETWORK OPTIMIZATION")
    # ... to be implemented
    bestM[iteration] = best
    averageM[iteration] = average
    while (iteration<iteration_max-1):
        #... to be implemented
        bestM[iteration] = best
        averageM[iteration] = average
        iteration=iteration+1
    


    print("best fitness: ", best)   
    print("average fitness: ", average)
    
    plotChart(bestM,averageM)
        
