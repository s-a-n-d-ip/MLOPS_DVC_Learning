import os
import pandas as pd


# -----------------------------
# 1. Dummy dictionary
# -----------------------------
data = {
    "name": ["Sandeep", "Rahul", "Amit"],
    "age": [35, 28, 30],
    "city": ["Burdwan", "Delhi", "Mumbai"]
}


# -----------------------------
# 2. Create DataFrame
# -----------------------------
df = pd.DataFrame(data)


# -----------------------------
# 3. Check if data folder exists
#    If not, create it
# -----------------------------
data_folder = "data"

if not os.path.exists(data_folder):
    os.makedirs(data_folder)


# -----------------------------
# 4. Save DataFrame as CSV
# -----------------------------
file_path = os.path.join(data_folder, "data.csv")

df.to_csv(file_path, index=False)


print(f"Data saved successfully to: {file_path}")