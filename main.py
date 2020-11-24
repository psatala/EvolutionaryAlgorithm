#!/usr/bin/env python3

from operations import *
from linear import *
import copy
from plot import *


def main():

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
        
        # if validate(problem, solution, optimalSolution):
            # print("OK")

        #evolutionary algorithms methods for operations
        selectionMethod = SELECTION_ROULETTE
        crossoverMethod = CROSSOVER_UNIFORM
        mutationMethod = MUTATION_GAUSS
        successionMethod = SUCCESSION_ELITE

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
            tempPopulation.calculateFitness(problem)
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
    
    createSummary(minFitness, avgFitness, maxFitness, optimalSolution, selectionMethod, crossoverMethod, mutationMethod, successionMethod)


if __name__ == "__main__":
    main()