# Load the required libraries
import numpy as np
import matplotlib.pyplot as plt
# Define the SIR model
N = 10000
S = N - 1
I = 1
R = 0
beta = 0.3
gamma = 0.05
# Define the lists to store the results
susceptible = [S]
infected = [I]
recovered = [R]
# Run the SIR model
for t in range(1000):
    infection_probability = beta * I / N
    new_infections = np.random.binomial(S, infection_probability)
    new_recoveries = np.random.binomial(I, gamma)
    S -= new_infections
    I += new_infections - new_recoveries
    R += new_recoveries
    susceptible.append(S)
    infected.append(I)
    recovered.append(R)
# Plot the results
plt.figure()
plt.plot(susceptible, label='Susceptible')
plt.plot(infected, label='Infected')
plt.plot(recovered, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of individuals')
plt.legend()
plt.show()