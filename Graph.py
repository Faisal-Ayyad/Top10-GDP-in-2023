import matplotlib.pyplot as plt

countries = ['USA', 'China', 'Japan', 'Germany', 'UK', 'India', 'France', 'Italy', 'Brazil', 'Canada']
gdp = [23, 17.73, 4.94, 4, 3.19, 3.17, 2.94, 2.1, 1.87, 1.6]
colors = ['red', 'green', 'blue', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']

plt.figure(figsize=(10, 5))

plt.scatter(countries, gdp, c=colors)

plt.yticks(range(0, 25, 2))

plt.xlabel('Countries')
plt.ylabel('GDP (in trillions of US dollars)')
plt.title('Top 10 countries with the highest GDP in 2023')

plt.show()