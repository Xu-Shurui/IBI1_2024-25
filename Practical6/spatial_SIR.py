# spatial_SIR.py
# 2D Stochastic SIR Model with Original Viridis Colors
# Generates four separate images for time points 0, 10, 50, 100

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import BoundaryNorm

# Parameters (as specified in the guide)
GRID_SIZE = 100        # 100x100 grid
BETA = 0.3             # Infection probability
GAMMA = 0.05           # Recovery probability
TIMESTEPS = 100        # Simulation duration
PLOT_TIMES = [0, 10, 50, 100]  # Required time points

# State codes
SUSCEPTIBLE = 0
INFECTED = 1
RECOVERED = 2

# Initialize grid with one infected individual
population = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
outbreak_pos = np.random.choice(GRID_SIZE, size=2)
population[outbreak_pos[0], outbreak_pos[1]] = INFECTED

# Store snapshots at required times
snapshots = {}

for t in range(TIMESTEPS + 1):
    if t in PLOT_TIMES:
        snapshots[t] = population.copy()
    
    # Synchronous updates
    new_population = population.copy()
    infected_cells = np.argwhere(population == INFECTED)
    
    for (x, y) in infected_cells:
        # Recovery
        if np.random.random() < GAMMA:
            new_population[x, y] = RECOVERED
            continue
        
        # Infect neighbors (8-directional)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if (0 <= nx < GRID_SIZE and 
                    0 <= ny < GRID_SIZE and 
                    population[nx, ny] == SUSCEPTIBLE):
                    if np.random.random() < BETA:
                        new_population[nx, ny] = INFECTED
    
    population = new_population

# Create discrete color mapping using original viridis
bounds = [0, 1, 2, 3]
norm = BoundaryNorm(bounds, cm.viridis.N)
cmap = cm.viridis

# Generate separate images
for t in PLOT_TIMES:
    plt.figure(figsize=(6, 5), dpi=150)
    
    # Plot with original viridis colors
    img = plt.imshow(snapshots[t], cmap=cmap, norm=norm, interpolation='nearest')
    
    # Create colorbar with original colors
    cbar = plt.colorbar(img, ticks=[0.5, 1.5, 2.5], shrink=0.8)
    cbar.ax.set_yticklabels(['Susceptible', 'Infected', 'Recovered'])
    cbar.set_label('Health State', rotation=270, labelpad=15)
    
    plt.title(f'2D SIR Model at Time = {t}\n(Initial Infection at {outbreak_pos})')
    plt.axis('off')
    plt.show()