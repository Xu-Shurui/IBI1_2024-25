programming_languages = {'JavaScipt':62.3, 'HTML':52.9, 'Python':51.0, 'SQL':51.0, 'TypeScript':38.5}#dictionary of programming languages and their popularity percentage
print("Programming Languages Popularity Dictionary:")#printing the dictionary
print(programming_languages)#printing the dictionary
import matplotlib.pyplot as plt#importing the matplotlib library
languages=list(programming_languages.keys())#list of programming languages
percentage=list(programming_languages.values())#list of popularity percentage
plt.bar(languages,percentage)#plotting the bar graph
plt.title('Programming Languages Popularity')#title of the graph
plt.xlabel('Programming Languages')#x-axis label
plt.ylabel('Popularity Percentage')#y-axis label
plt.xticks(fontsize=8, rotation=45)#setting the font size and rotation of x-axis labels
plt.yticks(fontsize=8)#setting the font size of y-axis labels
plt.show()
