import pandas as pd
import matplotlib.pyplot as plt

# Load the student data CSV file
file_path = "student_data.csv"
df = pd.read_csv(file_path)

# Count students per major
major_counts = df["Major"].value_counts()

# Display the count
print("Major-wise Student Count:\n", major_counts)

# Plot the pie chart
plt.figure(figsize=(8, 6))
plt.pie(major_counts, labels=major_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title("Major-wise Student Distribution")
plt.axis('equal')

plt.show()
