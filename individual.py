import numpy as np

class Individual:
    def __init__(self, n):
        self.fitness = 10 ** 10
        self.feasible = False
        self.chromosome = np.zeros(n)
        print(self.chromosome)