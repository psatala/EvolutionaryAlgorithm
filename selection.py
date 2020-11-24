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
        #fitnessVals[i] = 1 / fitnessVals[i] #another way to do roulette selection
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
        candidate0Id = np.random.randint(0, len(stablePopulation.individuals))
        candidate1Id = np.random.randint(0, len(stablePopulation.individuals))
        if(stablePopulation.individuals[candidate0Id].fitness <= stablePopulation.individuals[candidate1Id].fitness):
            selectedPopulation.individuals.append(stablePopulation.individuals[candidate0Id])
        else:
            selectedPopulation.individuals.append(stablePopulation.individuals[candidate1Id])

    
    return selectedPopulation
