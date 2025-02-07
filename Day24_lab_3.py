import matplotlib.pyplot as plt

segments = ['Product A', 'Product B', 'Services', 'Licensing']
revenue_percentages = [45, 25, 15, 15]

plt.pie(revenue_percentages, labels=segments, autopct='%1.1f%%', startangle=140, colors=['Red', 'Blue', 'yellow', 'gray'])
plt.title("Company Revenue Distribution")
plt.show()
