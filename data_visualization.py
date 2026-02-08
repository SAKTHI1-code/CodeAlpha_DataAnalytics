import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 24, 36, 18],
    'Year': [2020, 2021, 2022, 2023],
    'Sales': [100, 150, 200, 180],
    'Feature1': [1, 2, 3, 4],
    'Feature2': [2, 4, 5, 7]
})

# Bar chart
plt.bar(data['Category'], data['Value'])
plt.xlabel("Category")
plt.ylabel("Value")
plt.title("Category-wise Comparison")
plt.show()

# Line chart
plt.plot(data['Year'], data['Sales'])
plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Sales Trend")
plt.show()

# Scatter plot
plt.scatter(data['Feature1'], data['Feature2'])
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Feature Relationship")
plt.show()
