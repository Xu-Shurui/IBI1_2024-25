# Load the required libraries
import numpy as np
import matplotlib.pyplot as plt
# Define the SIR model
beta = 0.3
gamma = 0.05
vaccination_rate = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
N = 10000
plt.figure()
for rate in vaccination_rate:
    S = N * (1 - rate) - 1
    I = 1
    R = 0
    V = rate * N
    # Define the lists to store the results
    susceptible = [S]
    infected = [I]
    recovered = [R]
# Run the SIR model
    for t in range(1000):
        if S <= 0:
            break
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

    plt.plot(infected, label=f'{int(rate*100)}%')
plt.xlabel('Time')
plt.ylabel('Number of Infected People')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.show()
