import os 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

os.chdir(r'c:/Users/21507/Desktop/生物信息学/IBI1/notes/IBI_12024-2025/IBI1_2024-25/Practical10')
dalys_data = pd.read_csv('dalys-rate-from-all-causes.csv')
dalys_data.head(5)
dalys_data.info()
dalys_data.describe()
dalys_data.iloc[0, 3]
dalys_data.iloc[2, 0:5]
dalys_data.iloc[0:2, :]
dalys_data.iloc[0:10:2, 0:5]
dalys_data.iloc[0:10, 2]
dalys_data.loc[2:4, "Year"]
dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"]
uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs", "Year"]]  # Corrected this line
plt.plot(uk.Year, uk.DALYs, marker = "o", color = "blue")
plt.title("DALYs in the UK (1990-2019)")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.show()
uk_mean = uk.DALYs.mean()
france = dalys_data.loc[dalys_data["Entity"] == "France", ["DALYs", "Year"]]
france_mean = france.DALYs.mean()
uk_mean, france_mean
dalys_1990 = dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"]
plt.boxplot(dalys_1990)
plt.ylabel("DALYs")
plt.title("Distribution of DALYs in 1990")
plt.show()
results = f"UK mean DALYs: {uk_mean:.2f}, France mean DALYs: {france_mean:.2f}"
with open("results.txt", "w") as f:
    f.write(results)
china = dalys_data.loc[dalys_data["Entity"] == "China", ["DALYs", "Year"]]
plt.plot(china.Year, china.DALYs, "b+", label = "China")
plt.plot(uk.Year, uk.DALYs, "ro", label = "UK")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs in China and the UK (1990-2019)")
plt.legend()
plt.show()