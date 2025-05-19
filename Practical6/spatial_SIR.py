import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Initialize population
population = np.zeros((100, 100))  # 0: Susceptible, 1: Infected, 2: Recovered
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
print("Initial infected position:", outbreak)

# Parameters
beta = 0.3  # Infection probability
gamma = 0.05  # Recovery probability
cmap = ListedColormap(['purple', 'yellow', 'green'])  # Custom colors

# Simulation loop
for t in range(100):
    # Find all infected individuals
    infected_indices = np.where(population == 1)
    for i in range(len(infected_indices[0])):
        x, y = infected_indices[0][i], infected_indices[1][i]
        
        # Infect neighbors
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # Skip self
                neighbor_x, neighbor_y = x + dx, y + dy
                if 0 <= neighbor_x < 100 and 0 <= neighbor_y < 100:
                    if population[neighbor_x, neighbor_y] == 0:  # Susceptible
                        if np.random.rand() < beta:
                            population[neighbor_x, neighbor_y] = 1
        
        # Attempt recovery
        if np.random.rand() < gamma:
            population[x, y] = 2

    # Plot at specific time steps
    if t in [0, 10, 50, 99]:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap=cmap, interpolation='nearest', vmin=0, vmax=2)
        plt.title(f'Time Step {t}')
        plt.colorbar(ticks=[0, 1, 2], label='State: 0=S, 1=I, 2=R')
        plt.show()