import matplotlib.pyplot as plt
from constants import *


def plotSingleRun(runId, min, avg, max, optimal):
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
    plt.show() 