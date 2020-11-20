from population import *

#TODO faster mutation?


def mutationGauss(tempPopulation):
    for i in range(POPULATION_SIZE):
        for j in range(PROBLEM_SIZE):
            if np.random.rand() < MUTATION_PROBABILITY:
                tempPopulation.individuals[i].chromosome[j] += round(np.random.normal(loc=0.0, scale=1.0))
                tempPopulation.individuals[i].chromosome[j] = min(tempPopulation.individuals[i].chromosome[j], MAX_GRADE)
                tempPopulation.individuals[i].chromosome[j] = max(tempPopulation.individuals[i].chromosome[j], 0)    
    
    return tempPopulation




def mutationRandom(tempPopulation):
    for i in range(POPULATION_SIZE):
        for j in range(PROBLEM_SIZE):
            if np.random.rand() < MUTATION_PROBABILITY:
                tempPopulation.individuals[i].chromosome[j] = np.random.randint(1, MAX_GRADE + 1)
    
    return tempPopulation
