import numpy as np
from constants import PENALTY_CONSTANT



class Individual:
    def __init__(self, n, maxGrade, minGrade = 1):
        self.fitness = 10 ** 10
        self.feasible = False
        self.chromosome = np.random.randint(low = minGrade, high = maxGrade + 1, size = n)


    def calculateFitness(self, problem):
        self.isFeasible(problem)
        self.fitness = sum(self.chromosome) + PENALTY_CONSTANT * self.penalty(self.chromosome)
        return self.fitness

        
    def isFeasible(self, problem):
        if self.chromosome.size != problem.size:
            self.feasible = False
            return self.feasible

        if problem.size == 1:
            self.feasible = self.chromosome[0] >= 1
            return self.feasible
            
        if problem[0] > problem[1]:
            if self.chromosome[0] <= self.chromosome[1]:
                self.feasible = False
                return self.feasible

        if problem[-1] > problem[-2]:
            if self.chromosome[-1] <= self.chromosome[-2]:
                self.feasible = False
                return self.feasible

        for i in range(1, self.chromosome.size-1):
            if problem[i] > problem[i-1]:
                if self.chromosome[i] <= self.chromosome[i-1]:
                    self.feasible = False
                    return self.feasible
            if problem[i] > problem[i+1]:
                if self.chromosome[i] <= self.chromosome[i+1]:
                    self.feasible = False
                    return self.feasible
        
        self.feasible = True
        return self.feasible


    def penalty(self, problem):
        if self.chromosome.size != problem.size:
            self.feasible = False
            return 0

        if problem.size == 1:
            self.feasible = self.chromosome[0] >= 1
            return 0
            
        pVal = 0

        if problem[0] > problem[1]:
            if self.chromosome[0] <= self.chromosome[1]:
                pVal += self.chromosome[1] - self.chromosome[0] + 1

        if problem[-1] > problem[-2]:
            if self.chromosome[-1] <= self.chromosome[-2]:
                pVal += self.chromosome[-2] - self.chromosome[-1] + 1

        for i in range(1, self.chromosome.size-1):
            if problem[i] > problem[i-1]:
                if self.chromosome[i] <= self.chromosome[i-1]:
                    pVal += self.chromosome[i-1] - self.chromosome[i] + 1
            if problem[i] > problem[i+1]:
                if self.chromosome[i] <= self.chromosome[i+1]:
                    pVal += self.chromosome[i+1] - self.chromosome[i] + 1
        
        return pVal



    def makeFeasible(self, problem):

        for i in range(1, self.chromosome.size):

            if problem[i-1] < problem[i] and self.chromosome[i-1] >= self.chromosome[i]:
                self.chromosome[i] = self.chromosome[i-1] + 1
            
            elif problem[i-1] > problem[i] and self.chromosome[i-1] <= self.chromosome[i]:
                self.chromosome[i] = self.chromosome[i-1] - 1
        
                #backtracking
                if self.chromosome[i] == 0:
                    current = i
                    self.chromosome[current] = 1
                    while current > 0 and problem[current-1] > problem[current]:
                        self.chromosome[current-1] = self.chromosome[current] + 1
                        current -= 1
                    if current > 0 and problem[current-1] < problem[current]:
                        self.chromosome[current] = max(self.chromosome[current], self.chromosome[current-1]+1)

