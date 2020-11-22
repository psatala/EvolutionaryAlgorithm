#!/usr/bin/env python3

from operations import *
from linear import *
import copy


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
            tempPopulation = copy.deepcopy(stablePopulation)
            tempPopulation = selection(tempPopulation, selectionMethod)
            tempPopulation = crossover(tempPopulation, crossoverMethod)
            tempPopulation = mutation(tempPopulation, mutationMethod)
            tempPopulation.calculateFitness(problem)
            stablePopulation = succession(stablePopulation, tempPopulation, successionMethod)
            scores = []
            bestChromosome = []
            bestFit = 1e9
            for x in stablePopulation.individuals:
                scores.append(x.fitness)
                if x.fitness < bestFit:
                    bestFit = x.fitness
                    bestChromosome = x.chromosome
            print(min(scores), end="\t")
            print(round(sum(scores)/len(scores)), end="\t")
            print(max(scores))
            print(bestChromosome)

        print("Optimal solution: "+str(optimalSolution))
        print(solution)

if __name__ == "__main__":
    main()