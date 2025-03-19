UK_countries = [57.11, 3.13, 1.91, 5.45]
UK_countries_sorted = sorted(UK_countries)
print("sorted UK contriespopulations (millions):")
print (UK_countries_sorted)
Zhejiang_neighboring = [65.77, 41.88, 45.28, 61.27, 85.15]
Zhejiang_neighboring_sorted = sorted(Zhejiang_neighboring)
print("sorted Zhejiang neighboring countries populations (millions):")
print (Zhejiang_neighboring_sorted)
import matplotlib.pyplot as plt
plt .figure(figsize=(10,5))
plt .pie(UK_countries, labels = ['England', 'Wales', 'Northern Ireland', 'Scotland'], autopct='%1.1f%%')
plt .title('UK Countries Populations')
#plt .show()

plt .figure(figsize=(10,5))
plt .pie(Zhejiang_neighboring, labels = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu', ], autopct='%1.1f%%')
plt .title('Zhejiang Neighboring Countries Populations')
plt .axis('equal')
plt .show()