#import the required libraries
import numpy as np
import matplotlib.pyplot as plt
#make array of all suspectible people
population = np.zeros((100, 100))#create a 100x100 matrix
#find the initial infected person
outbreak = np.random.choice(range(100), 2)#find the initial infected person
population[outbreak[0], outbreak[1]] = 1# Define the parameters of the model
print("Initial infected position:", outbreak)#print the initial infected position
beta = 0.3
gamma = 0.05
# Run the model
for t in range(100):# Find infected people
    infected_people = np.where(population==1)
    print(f"Time step {t}, infected positions:",list(zip(infected_people[0], infected_people[1])))
    for i in range(len(infected_people[0])):
        x = infected_people[0][i]# Find the infected person
        y = infected_people[1][i]
# Find the neighbours of the infected person
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:# Skip the current position
                    continue
                neighbor_x, neighbor_y = x + dx, y + dy# Check if the neighbour is within the population
                if 0 <= x + dx < 100 and 0 <= y + dy < 100:
                    if population[neighbor_x, neighbor_y] == 0:#
                        if np.random.rand() < beta:
                            population[neighbor_x, neighbor_y] = 1
        if np.random.rand() < gamma:# Recover people
            population[x, y] = 2
# Recover people
    if t in [0, 10, 50, 99]:  # Plot the results          
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time Step {t}')
        plt.show()