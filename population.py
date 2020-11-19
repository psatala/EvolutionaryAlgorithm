from individual import *
from constants import *

class Population:
    def __init__(self, populationSize = POPULATION_SIZE, problemSize = PROBLEM_SIZE, maxGrade = MAX_GRADE):
        self.individuals = [Individual(problemSize, maxGrade) for i in range(populationSize)]

    def calculateFitness(self, problem):
        for individual in self.individuals:
            individual.calculateFitness(problem)