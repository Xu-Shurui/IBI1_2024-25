# Practical 10: Working with Global Health Data
# IBI1 2024/25 - Portfolio Submission

import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Set working directory to script location
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

# 2. Verify directory and load data
print("Current directory:", os.getcwd())
print("Files present:", os.listdir())

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# 3. Initial data exploration
print("\nFirst 5 rows:")
print(dalys_data.head(5))

print("\nDataframe info:")
print(dalys_data.info())

# 4. Portfolio Required Tasks

# Task 1: Show years column for first 10 rows
print("\nTask 1: Year column for first 10 rows")
print(dalys_data.iloc[0:10, 2])
print("Note: The 10th year with DALYs data in Afghanistan is", dalys_data.iloc[9, 2])

# Task 2: Boolean indexing for 1990 data
print("\nTask 2: DALYs for all countries in 1990 (Boolean indexing)")
year_mask = dalys_data['Year'] == 1990  # Create Boolean mask
dalys_1990 = dalys_data.loc[year_mask, ['Entity', 'DALYs']]  # Apply mask
print(dalys_1990)

# Task 3: Compare UK and France means
print("\nTask 3: UK vs France comparison")
uk_data = dalys_data[dalys_data['Entity'] == 'United Kingdom']
fr_data = dalys_data[dalys_data['Entity'] == 'France']

uk_mean = uk_data['DALYs'].mean()
fr_mean = fr_data['DALYs'].mean()

print(f"UK mean DALYs: {uk_mean:.2f}")
print(f"France mean DALYs: {fr_mean:.2f}")
print(f"Conclusion: UK mean DALYs are {'higher' if uk_mean > fr_mean else 'lower'} than France's")

# Task 4: Plot UK DALYs over time
print("\nTask 4: Generating UK DALYs plot")
plt.figure(figsize=(10,5))
plt.plot(uk_data['Year'], uk_data['DALYs'], 'b+')
plt.xticks(uk_data['Year'], rotation=90)
plt.title('UK DALYs Over Time (1990-2019)')
plt.xlabel('Year')
plt.ylabel('DALYs per 100,000')
plt.grid(True)
plt.tight_layout()
plt.show()

# Task 5: Custom analysis (China vs UK comparison)
print("\nTask 5: Custom analysis - China vs UK comparison")
china_data = dalys_data[dalys_data['Entity'] == 'China']

plt.figure(figsize=(12,6))
plt.plot(uk_data['Year'], uk_data['DALYs'], 'b-', label='UK')
plt.plot(china_data['Year'], china_data['DALYs'], 'r-', label='China')
plt.xticks(uk_data['Year'], rotation=90)
plt.title('DALYs Comparison: UK vs China (1990-2019)')
plt.xlabel('Year')
plt.ylabel('DALYs per 100,000')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()