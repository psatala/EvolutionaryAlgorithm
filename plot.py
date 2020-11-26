import matplotlib.pyplot as plt
from constants import *
from datetime import datetime


def createSummary(minFitness, avgFitness, maxFitness, optimalSolution, selectionMethod, crossoverMethod, mutationMethod, successionMethod, feasibilityMethod):
    filename = "results/"+datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + '.png'
    file = open(filename[:-3]+"txt","w")
    file.write("Plot: "+str(filename)+'\n')
    file.write("Optimal solution:\t")
    for i in range(N_RUNS):
        file.write(str(optimalSolution[i])+"\t")
    file.write('\n')
    file.write("Final best fitness:\t")
    for i in range(N_RUNS):
        file.write(str(minFitness[i][N_EPOCHS-1])+"\t")
    file.write('\n')
    file.write("Final average fitness:\t")
    for i in range(N_RUNS):
        file.write(str(avgFitness[i][N_EPOCHS-1])+"\t")
    file.write('\n')
    file.write("Final worst fitness:\t")
    for i in range(N_RUNS):
        file.write(str(maxFitness[i][N_EPOCHS-1])+"\t")
    file.write('\n')
    file.write('Penalty: '+str(PENALTY_CONSTANT)+'\n')
    file.close()

    suptitle = ''
    if selectionMethod == SELECTION_ROULETTE:
        suptitle += 'Roulette selection, '
    else:
        suptitle += 'Tournament selection, '
    if crossoverMethod == CROSSOVER_SINGLE_POINT:
        suptitle += 'Single point crossover ('+str(CROSSOVER_PROBABILITY)+'), '
    elif crossoverMethod == CROSSOVER_UNIFORM:
        suptitle += 'Uniform crossover ('+str(CROSSOVER_PROBABILITY)+'), '
    elif crossoverMethod == CROSSOVER_ARITHMETIC:
        suptitle += 'Arithmetic crossover ('+str(CROSSOVER_PROBABILITY)+'), '
    else:
        suptitle += 'No crossover, '
    if mutationMethod == MUTATION_GAUSS:
        suptitle += 'Gaussian mutation ('+str(MUTATION_PROBABILITY)+'), '
    else:
        suptitle += 'Random mutation ('+str(MUTATION_PROBABILITY)+'), '
    if successionMethod == SUCCESSION_GENERATIONAL:
        suptitle += 'Generational succession, '
    else:
        suptitle += 'Elite succession ('+str(ELITE_SIZE)+'), '
    if feasibilityMethod == FEASIBLE_ONLY:
        suptitle += 'Feasible only'
    else:
        suptitle += 'Infeasible allowed ('+str(PENALTY_CONSTANT)+')'
    plotSummary(minFitness, avgFitness, maxFitness, optimalSolution, suptitle, filename)



def plotSingleRun(runId, min, avg, max, optimal, suptitle, filename):
    x = range(N_EPOCHS)
    opt = [optimal[runId] for i in range(N_EPOCHS)]
    plt.plot(x, min[runId], label = "Best fitness")  
    plt.plot(x, avg[runId], label = "Average fitness") 
    plt.plot(x, max[runId], label = "Worst fitness") 
    plt.plot(x, opt, label = "Optimal solution") 
    
    plt.xlabel('Epoch')
    plt.ylim(0, 500)
    plt.ylabel('Fitness') 
    plt.title('Run no.'+str(runId)) 
    plt.legend()
    savePlot(plt, filename) 
    plt.show()



def plotSummary(min, avgg, max, optimal, suptitle, filename):
    x = range(N_EPOCHS)
    opt = [1 for i in range(N_EPOCHS)]

    #normalize
    for i in range(N_RUNS):
        for j in range(N_EPOCHS):
            min[i][j] /= optimal[i]
            avgg[i][j] /= optimal[i]
            max[i][j] /= optimal[i]


    minVal = avgColumns(min)
    avgVal = avgColumns(avgg)
    maxVal = avgColumns(max)
    plt.plot(x, minVal, label = "Best fitness")  
    plt.plot(x, avgVal, label = "Average fitness") 
    plt.plot(x, maxVal, label = "Worst fitness") 
    plt.plot(x, opt, label = "Optimal solution") 

    plt.xlabel('Epoch')
    plt.ylim(0.8, 5)
    plt.ylabel('Fitness') 
    plt.title('Average of '+str(N_RUNS)+' runs with a population of '+str(POPULATION_SIZE)+' individuals')
    plt.suptitle(suptitle)
    plt.legend()
    savePlot(plt, filename)
    plt.show()


def avgColumns(x):
    output = []
    a = len(x)
    b = len(x[0])
    for i in range(b):
        sum = 0
        for j in range(a):
            sum += x[j][i]
        output.append(sum/a)
    return output

def savePlot(plt, filename):
    figure = plt.gcf() # get current figure
    figure.set_size_inches(10.8, 7.2)
    plt.savefig(filename, bbox_inches='tight', dpi=120)
