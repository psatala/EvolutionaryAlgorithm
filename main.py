from operations import *
from linear import *


def main():

    for i in range(N_RUNS):
        
        #generate problem
        problem = np.random.randint(low = 1, high = MAX_GRADE + 1, size = PROBLEM_SIZE)

        #optimal solution
        optimalSolution = linear(problem)


        #evolutionary algorithms methods for operations
        selectionMethod = SELECTION_TOURNAMENT
        crossoverMethod = CROSSOVER_UNIFORM
        mutationMethod = MUTATION_GAUSS
        successionMethod = SUCCESSION_GENERATIONAL

        #initialize population
        stablePopulation = Population()

        #main loop
        while True:
            tempPopulation = selection(stablePopulation, selectionMethod)
            tempPopulation = crossover(tempPopulation, crossoverMethod)
            tempPopulation = mutation(tempPopulation, mutationMethod)
            tempPopulation.calculateFitness(problem)
            stablePopulation = succession(stablePopulation, tempPopulation, successionMethod)




if __name__ == "__main__":
    main()