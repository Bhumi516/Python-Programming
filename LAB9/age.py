import pandas as pd
from datetime import date

# Read CSV file
df = pd.read_csv("data.csv")

# Get today's date from the device
today = date.today()

# Function to calculate age
def calculate_age(dob):
    dob = pd.to_datetime(dob).date()

    age = today.year - dob.year

    # Check whether birthday has occurred this year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    return age

# Calculate age
df["Age"] = df["Date_of_Birth"].apply(calculate_age)

# Display result
print("Student Details:")
print(df)