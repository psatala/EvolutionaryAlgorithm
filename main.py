#!/usr/bin/env python3

from operations import *
from linear import *


def main():

    for i in range(N_RUNS):
        
        #generate problem
        problem = np.random.randint(low = 1, high = MAX_GRADE + 1, size = PROBLEM_SIZE)

        #optimal solution
        optimalSolution, solution = linear(problem)
        
        # if validate(problem, solution, optimalSolution):
            # print("OK")


        #evolutionary algorithms methods for operations
        selectionMethod = SELECTION_TOURNAMENT
        crossoverMethod = CROSSOVER_UNIFORM
        mutationMethod = MUTATION_GAUSS
        successionMethod = SUCCESSION_GENERATIONAL

        #initialize population
        stablePopulation = Population()

        iterations = 0
        #main loop
        while iterations < N_ITERATIONS:
            tempPopulation = selection(stablePopulation, selectionMethod)
            tempPopulation = crossover(tempPopulation, crossoverMethod)
            tempPopulation = mutation(tempPopulation, mutationMethod)
            tempPopulation.calculateFitness(problem)
            stablePopulation = succession(stablePopulation, tempPopulation, successionMethod)
            iterations += 1


if __name__ == "__main__":
    main()