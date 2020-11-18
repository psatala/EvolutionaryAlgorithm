from individual import *
from operations import *



def main():

    #constants
    PROBLEM_SIZE = 30
    MAX_GRADE = 6

    myIndividual = Individual(PROBLEM_SIZE)
    
    #TODO
    stablePopulation = init()

    selectionMethod = SELECTION_TOURNAMENT
    crossoverMethod = CROSSOVER_UNIFORM
    mutationMethod = MUTATION_GAUSS
    successionMethod = SUCCESSION_GENERATIONAL

    #main loop
    while(True):
        tempPopulation = selection(stablePopulation, selectionMethod)
        tempPopulation = crossover(tempPopulation, crossoverMethod)
        tempPopulation = mutation(tempPopulation, mutationMethod)
        fitness(tempPopulation)
        stablePopulation = succession(stablePopulation, tempPopulation, successionMethod)
    



if __name__ == "__main__":
    main()