import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("plott.csv")

# Display the dataset
print(df)

# Plot a graph
plt.plot(df["Student"], df["Python"], marker="o")

# Add title and labels
plt.title("Student Python Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

# Display grid
plt.grid(True)

# Display the graph
plt.show()