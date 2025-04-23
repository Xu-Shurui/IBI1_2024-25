import matplotlib.pyplot as plt

# 数据
genotypes = ['Q/Q', 'Q/R', 'R/R']
counts = [25, 23, 1]  # Q/Q: 25人, Q/R: 23人, R/R: 1人
colors = ['#66b3ff', '#99ff99', '#ff9999']

# 创建饼状图
plt.figure(figsize=(6, 6))
plt.pie(counts, labels=genotypes, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Distribution of PON1 Q192R Genotypes')
plt.show()