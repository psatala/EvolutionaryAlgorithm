import numpy as np

class Individual:
    def __init__(self, n, maxGrade, minGrade = 1):
        self.fitness = 10 ** 10
        self.feasible = False
        self.chromosome = np.random.randint(low = minGrade, high = maxGrade + 1, size = n)

    def calculateFitness(self, problem):
        self.fitness = 10 ** 10 #TODO
