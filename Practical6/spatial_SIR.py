# spatial_SIR.py
# 2D Stochastic SIR Model - Practical 6 Submission
# [Your Name], [Student ID] - IBI1 2024/25

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# =============================================
# Parameters (as specified in the guide)
# =============================================
GRID_SIZE = 100        # 100x100 grid (as per guide)
BETA = 0.3             # Infection probability
GAMMA = 0.05           # Recovery probability
TIMESTEPS = 100        # Simulation duration

# =============================================
# Initialize Grid
# =============================================
# State encoding: 
# 0 = Susceptible (S), 1 = Infected (I), 2 = Recovered (R)
population = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

# Set exactly one random infected individual (as required)
outbreak_pos = np.random.choice(GRID_SIZE, size=2)
population[outbreak_pos[0], outbreak_pos[1]] = 1

# =============================================
# Simulation Loop
# =============================================
for t in range(TIMESTEPS):
    # Create copy for synchronous updates
    new_pop = population.copy()
    
    # Get all infected cells
    infected_idx = np.argwhere(population == 1)
    
    for (x,y) in infected_idx:
        # Recovery process
        if np.random.random() < GAMMA:
            new_pop[x,y] = 2
            continue
        
        # Infect neighboring cells (8-directional)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # Skip self
                
                nx, ny = x+dx, y+dy
                
                # Check grid boundaries
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                    # Only infect susceptible neighbors
                    if population[nx,ny] == 0 and np.random.random() < BETA:
                        new_pop[nx,ny] = 1
    
    population = new_pop

# =============================================
# Final Visualization (as per guide)
# =============================================
plt.figure(figsize=(6,4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title('Spatial SIR Model - Final State')
plt.colorbar(ticks=[0,1,2], label='State: 0=S, 1=I, 2=R')
plt.savefig("spatial_SIR_result.png", dpi=150)
plt.show()