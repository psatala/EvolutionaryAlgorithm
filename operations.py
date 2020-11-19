from selection import *
from crossover import *
from mutation import *
from succession import *



def selection(stablePopulation, selectionMethod):
    if selectionMethod == SELECTION_ROULETTE:
        return selectionRoulette(stablePopulation)
    else:
        return selectionTournament(stablePopulation)



def crossover(tempPopulation, crossoverMethod):
    if crossoverMethod == CROSSOVER_SINGLE_POINT:
        return crossoverSinglePoint(tempPopulation)
    elif crossoverMethod == CROSSOVER_UNIFORM:
        return crossoverUniform(tempPopulation)
    elif crossoverMethod == CROSSOVER_ARITHMETIC:
        return crossoverArithmetic(tempPopulation)
    else:
        return tempPopulation



def mutation(tempPopulation, mutationMethod):
    if mutationMethod == MUTATION_GAUSS:
        return mutationGauss(tempPopulation)
    else:
        return mutationRandom(tempPopulation)



def succession(stablePopulation, tempPopulation, successionMethod):
    if successionMethod == SUCCESSION_GENERATIONAL:
        return successionGenerational(stablePopulation, tempPopulation)
    else:
        return successionElite(stablePopulation, tempPopulation)