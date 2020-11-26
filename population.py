from individual import *
from constants import *



def printPop(pop):
    for x in pop.individuals:
        print(x.chromosome, end=' ')
        print(x.fitness, end='\t')
    print()

def bestFitness(pop):
    bestFit = 1e9
    for x in pop.individuals:
        if x.fitness < bestFit:
            bestFit = x.fitness
    print(bestFit)


class Population:
    def __init__(self, populationSize = POPULATION_SIZE, problemSize = PROBLEM_SIZE, maxGrade = MAX_GRADE):
        self.individuals = [Individual(problemSize, maxGrade) for i in range(populationSize)]

    def calculateFitness(self, problem, feasibilityMethod):
        for individual in self.individuals:
            individual.calculateFitness(problem, feasibilityMethod)