from population import *
from individual import *
import math

def crossoverSinglePoint(a, b):
    cut = math.floor(np.random.rand()*PROBLEM_SIZE)
    offspring = Individual(PROBLEM_SIZE, MAX_GRADE)
    offspring.chromosome = np.concatenate((a.chromosome[:cut], b.chromosome[cut:]))
    return offspring


def crossoverUniform(a, b):
    offspring = Individual(PROBLEM_SIZE, MAX_GRADE)
    Pe = np.random.rand()
    for i in range(PROBLEM_SIZE):
        if np.random.rand() < Pe:
            offspring.chromosome[i] = a.chromosome[i]
        else:
            offspring.chromosome[i] = b.chromosome[i]
    return offspring
    

def crossoverArithmetic(a, b):
    offspring = Individual(PROBLEM_SIZE, MAX_GRADE)
    alpha = np.random.rand()
    for i in range(PROBLEM_SIZE):
        offspring.chromosome[i] = alpha*a.chromosome[i] + (1-alpha)*b.chromosome[i]
    return offspring