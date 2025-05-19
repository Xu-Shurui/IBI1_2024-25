# Load the required libraries
import numpy as np
import matplotlib.pyplot as plt
# Define the SIR model
beta = 0.3
gamma = 0.05
vaccination_rate = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
N = 10000
plt.figure()# Create a new figure for plotting
# Loop through different vaccination rates
for rate in vaccination_rate:
    S = N * (1 - rate) - 1
    I = 1
    R = rate * N
    # Calculate the number of vaccinated individuals
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
        S -= new_infections# Update the number of susceptible individuals
        I += new_infections - new_recoveries#  Update the number of infected individuals
        R += new_recoveries# Update the number of recovered individuals
        susceptible.append(S)
        infected.append(I)
        recovered.append(R)
    # Plot the results

    plt.plot(infected, label=f'{int(rate*100)}%')# Plot the number of infected individuals
# Add labels and title
plt.xlabel('Time')
plt.ylabel('Number of Infected People')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.show()