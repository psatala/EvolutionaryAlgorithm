from selection import *



#constants

#selection
SELECTION_ROULETTE = 1
SELECTION_TOURNAMENT = 2
#crossover
CROSSOVER_SINGLE_POINT = 1
CROSSOVER_UNIFORM = 2
CROSSOVER_ARITHMETIC = 3
CROSSOVER_NONE = 4
#mutation
MUTATION_GAUSS = 1
MUTATION_RANDOM = 2
#succession
SUCCESSION_GENERATIONAL = 1
SUCCESSION_ELITE = 2



def selection(stablePopulation, selectionMethod):
    if(selectionMethod == SELECTION_ROULETTE):
        return selectionRoulette
    else:
        return selectionTournament



def crossover(tempPopulation, crossoverMethod):
    pass

def mutation(tempPopulation, mutationMethod):
    pass

def succession(stablePopulation, tempPopulation, successionMethod):
    pass