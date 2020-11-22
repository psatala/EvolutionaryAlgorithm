from population import *



def selectionRoulette(stablePopulation):
    selectedPopulation = Population(populationSize=0)

    #calculate total fitness
    fitnessVals = []
    for i in range(len(stablePopulation.individuals)):
        fitnessVals.append(stablePopulation.individuals[i].fitness)
    
    maxFitness = max(fitnessVals)
    minFitness = min(fitnessVals)
    for i in range(len(fitnessVals)):
        fitnessVals[i] = maxFitness - fitnessVals[i] + minFitness
    sumFitness = sum(fitnessVals)

    #calculate probabilities
    probabilities = np.zeros(len(stablePopulation.individuals))
    for i in range(len(stablePopulation.individuals)):
        probabilities[i] = fitnessVals[i] / sumFitness

    #select
    chosenOnes = np.random.choice(a=stablePopulation.individuals, size=len(stablePopulation.individuals), replace=True, p=probabilities).tolist()
    selectedPopulation.individuals += chosenOnes

    return selectedPopulation



def selectionTournament(stablePopulation):
    selectedPopulation = Population(populationSize=0)

    for i in range(len(stablePopulation.individuals)):
        #play tournament
        candidates = np.random.choice(a=stablePopulation.individuals, size=2, replace=True)
        if(candidates[0].fitness <= candidates[1].fitness):
            selectedPopulation.individuals.append(candidates[0])
        else:
            selectedPopulation.individuals.append(candidates[1])

    
    return selectedPopulation
