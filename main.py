#!/usr/bin/env python3

from operations import *
from linear import *
import copy
from plot import *
import time



def main():

    # Use current Unix time as seed
    seed = int(round(time.time()))
    np.random.seed(seed)

    minFitness = []
    avgFitness = []
    maxFitness = []
    optimalSolution = []

    for n in range(N_RUNS):
        print('Run '+str(n))
        
        #generate problem
        problem = np.random.randint(low = 1, high = MAX_GRADE + 1, size = PROBLEM_SIZE)

        #optimal solution
        solutionVal, solution = linear(problem)
        optimalSolution.append(solutionVal)
        
        #evolutionary algorithms methods for operations
        selectionMethod = SELECTION_TOURNAMENT
        crossoverMethod = CROSSOVER_NONE
        mutationMethod = MUTATION_GAUSS
        successionMethod = SUCCESSION_ELITE
        feasibilityMethod = INFEASIBLE_ALLOWED

        #initialize population
        stablePopulation = Population()

        mins = []
        avgs = []
        maxs = []

        #main loop
        for i in range(N_EPOCHS):
            if i % 100 == 0:
                print("Epoch "+str(i)+"/"+str(N_EPOCHS))
            tempPopulation = copy.deepcopy(stablePopulation)
            tempPopulation = selection(tempPopulation, selectionMethod)
            tempPopulation = crossover(tempPopulation, crossoverMethod)
            tempPopulation = mutation(tempPopulation, mutationMethod)
            tempPopulation.calculateFitness(problem, feasibilityMethod)
            stablePopulation = succession(stablePopulation, tempPopulation, successionMethod)
            scores = []
            for x in stablePopulation.individuals:
                scores.append(x.fitness)
            mins.append(min(scores))
            avgs.append(round(sum(scores)/len(scores)))
            maxs.append(max(scores))

        
        minFitness.append(mins)
        avgFitness.append(avgs)
        maxFitness.append(maxs)
    
    createSummary(minFitness, avgFitness, maxFitness, optimalSolution, selectionMethod, crossoverMethod, mutationMethod, successionMethod, feasibilityMethod, seed)


if __name__ == "__main__":
    main()

