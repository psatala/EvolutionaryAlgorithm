import numpy as np


def linear(problem):
    if problem.size == 0:
        return 0
    if problem.size == 1:
        return 1
    
    leftpass = np.ones(problem.size, int)
    rightpass = np.ones(problem.size, int)
    for i in range(1, problem.size):
        if problem[i] > problem[i-1]:
            rightpass[i] = rightpass[i-1] + 1
    for i in range(problem.size-1, 0, -1):
        if problem[i-1] > problem[i]:
            leftpass[i-1] = leftpass[i] + 1

    solution = np.maximum(leftpass, rightpass)
    return sum(solution), solution   



def validate(problem, solution, optimalSolution):
    if problem.size == 0:
        return optimalSolution == 0 and solution.empty
    if problem.size == 1:
        return optimalSolution == 1 and solution.size == 1 and solution[0] == 1

    if solution.size != problem.size:
        return False

    if optimalSolution != sum(solution):
        return False

    if problem[0] > problem[1]:
        if solution[0] != solution[1] + 1:
            return False
    else:
        if solution[0] != 1:
            return False

    if problem[-1] > problem[-2]:
        if solution[-1] != solution[-2] + 1:
            return False
    else:
        if solution[-1] != 1:
            return False
    
    for i in range(1, solution.size-1):
        if problem[i] > problem[i-1] and problem[i] > problem[i+1]:
            if solution[i] != np.maximum(solution[i-1], solution[i+1]) + 1:
                return False
        if problem[i] > problem[i-1] and problem[i] <= problem[i+1]:
            if solution[i] != solution[i-1] + 1:
                return False
        if problem[i] <= problem[i-1] and problem[i] > problem[i+1]:
            if solution[i] != solution[i+1] + 1:
                return False
        if problem[i] <= problem[i-1] and problem[i] <= problem[i+1]:
            if solution[i] != 1:
                return False
    
    return True
        
        