import matplotlib.pyplot as plt

income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140, colors=['Blue', 'green', 'red', 'purple', 'orange'])
plt.title("Monthly Income Distribution")
plt.show()
