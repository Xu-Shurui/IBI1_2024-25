UK_countries = [57.11, 3.13, 1.91, 5.45]#list of UK countries populations in millions
UK_countries_sorted = sorted(UK_countries)#sorted list of UK countries populations
print("sorted UK contriespopulations (millions):")#printing the sorted list of UK countries populations
print (UK_countries_sorted)#printing the sorted list of UK countries populations
Zhejiang_neighboring = [65.77, 41.88, 45.28, 61.27, 85.15]#list of Zhejiang neighboring countries populations in millions
Zhejiang_neighboring_sorted = sorted(Zhejiang_neighboring)#sorted list of Zhejiang neighboring countries populations
print("sorted Zhejiang neighboring countries populations (millions):")#printing the sorted list of Zhejiang neighboring countries populations
print (Zhejiang_neighboring_sorted)#printing the sorted list of Zhejiang neighboring countries populations
import matplotlib.pyplot as plt#importing the matplotlib library
plt .figure(figsize=(10,5))#setting the figure size
plt .pie(UK_countries, labels = ['England', 'Wales', 'Northern Ireland', 'Scotland'], autopct='%1.1f%%')#plotting the pie chart
plt .title('UK Countries Populations')#title of the graph
#plt .show()

plt .figure(figsize=(10,5))#setting the figure size
plt .pie(Zhejiang_neighboring, labels = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu', ], autopct='%1.1f%%')#plotting the pie chart
plt .title('Zhejiang Neighboring Countries Populations')#title of the graph
plt .axis('equal')#setting the aspect ratio of the pie chart to be equal
plt .show()#displaying the pie chart