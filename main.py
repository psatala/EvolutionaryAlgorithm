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
        selectionMethod = SELECTION_ROULETTE
        crossoverMethod = CROSSOVER_ARITHMETIC
        mutationMethod = MUTATION_GAUSS
        successionMethod = SUCCESSION_ELITE

        #initialize population
        stablePopulation = Population()

        #main loop
        for i in range(N_ITERATIONS):
            print("Iteration "+str(i))
            tempPopulation = selection(stablePopulation, selectionMethod)
            tempPopulation = crossover(tempPopulation, crossoverMethod)
            tempPopulation = mutation(tempPopulation, mutationMethod)
            tempPopulation.calculateFitness(problem)
            stablePopulation = succession(stablePopulation, tempPopulation, successionMethod)
            scores = []
            for x in stablePopulation.individuals:
                scores.append(x.fitness)
            print(min(scores), end="\t")
            print(round(sum(scores)/len(scores)), end="\t")
            print(max(scores))

        print("Optimal solution: "+str(optimalSolution))

if __name__ == "__main__":
    main()