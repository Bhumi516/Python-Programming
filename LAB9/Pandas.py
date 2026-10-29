import pandas as pd

data = pd.read_csv("students.csv")

print("CSV Data:")
print(data)

print("\nSeries:")
print(data["Name"])

print("\nDataFrame:")
print(data)