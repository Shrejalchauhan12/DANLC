import pandas as pd
import matplotlib.pyplot as plt

# Load the customer data CSV file
file_path = "customer_data.csv"
df = pd.read_csv(file_path)

# Count customers per marital status
marital_counts = df["Marital_status"].value_counts()

# Display the count
print("Marital Status-wise Customer Count:\n", marital_counts)

# Plot the bar chart
plt.figure(figsize=(8, 5))
plt.bar(marital_counts.index, marital_counts.values, color=['blue', 'orange', 'green'])
plt.xlabel("Marital Status")
plt.ylabel("Customer Count")
plt.title("Marital Status-wise Customer Distribution")
plt.xticks(rotation=0)

plt.show()
