# Practical 10: Working with Global Health Data
# Import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set working directory to where the data file is stored
# Replace with your actual path
os.chdir("c:/Users/21507/Desktop/生物信息学/IBI1/notes/IBI_12024-2025/IBI1_2024-25/Practical10/")
# Ensure the directory change was successful  

# Load the dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Initial exploration of the data
print("\nFirst 5 rows of the dataset:")
print(dalys_data.head(5))

print("\nDataset information:")
print(dalys_data.info())

print("\nSummary statistics:")
print(dalys_data.describe())

# Accessing specific data using iloc
print("\nThird column (Year) for first 10 rows:")
print(dalys_data.iloc[0:10, 2])

# The 10th year with DALYs data recorded in Afghanistan is:
afghanistan_10th_year = dalys_data.iloc[9, 2]
print(f"\nThe 10th year with DALYs data in Afghanistan: {afghanistan_10th_year}")

# Boolean indexing to get DALYs for 1990
mask_1990 = dalys_data['Year'] == 1990
dalys_1990 = dalys_data.loc[mask_1990, "DALYs"]
print("\nDALYs for all countries in 1990:")
print(dalys_1990)

# Comparing UK and France data
uk = dalys_data.loc[dalys_data['Entity'] == 'United Kingdom', ['DALYs', 'Year']]
france = dalys_data.loc[dalys_data['Entity'] == 'France', ['DALYs', 'Year']]

# Calculate means
uk_mean = uk['DALYs'].mean()
france_mean = france['DALYs'].mean()

print(f"\nUK mean DALYs: {uk_mean:.2f}")
print(f"France mean DALYs: {france_mean:.2f}")

# Comment on comparison
if uk_mean > france_mean:
    comparison = "greater"
else:
    comparison = "less"
print(f"The mean DALYs in the UK is {comparison} than in France.")

# Plotting UK DALYs over time
plt.figure(figsize=(10, 6))
plt.plot(uk['Year'], uk['DALYs'], 'b+')
plt.xticks(uk['Year'], rotation=90)
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs in the United Kingdom Over Time')
plt.grid(True)
plt.tight_layout()
plt.show()

# Custom Question: How has the relationship between DALYs in China and the UK changed over time?
china = dalys_data.loc[dalys_data['Entity'] == 'China', ['DALYs', 'Year']]

# Plot both countries
plt.figure(figsize=(12, 6))
plt.plot(uk['Year'], uk['DALYs'], 'b-', label='United Kingdom')
plt.plot(china['Year'], china['DALYs'], 'r-', label='China')
plt.xticks(uk['Year'], rotation=90)
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('Comparison of DALYs: UK vs China Over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot the difference between China and UK DALYs
difference = china['DALYs'].values - uk['DALYs'].values
plt.figure(figsize=(12, 6))
plt.plot(uk['Year'], difference, 'g-')
plt.xticks(uk['Year'], rotation=90)
plt.xlabel('Year')
plt.ylabel('DALYs Difference (China - UK)')
plt.title('Difference in DALYs Between China and UK Over Time')
plt.grid(True)
plt.tight_layout()
plt.show()