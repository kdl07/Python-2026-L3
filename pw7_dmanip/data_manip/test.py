import pandas as pd

df = pd.read_csv('students.csv')
# Load dataset
print('=== Loading dataset === \n')
print(df)
print()

# Display first 5 rows
print('=== Loading first 5 rows === \n')
print(df.head(5))
print()

# Find number of rows and columns
print('=== Showing number of rows and columns === \n')
print(df.info()) # 30 entries (rows) and 5 columns
print()

# Select name and GPA
print('=== Loading name and GPA === \n')
name_and_GPA = df[["name", "GPA"]]
print(name_and_GPA)
print()

# GPA >= 3.5
print('=== Loading students with GPA >= 3.5 === \n')
excellent = df["GPA"] >= 3.5
print(excellent)
print()

# Sort by GPA
print('=== Sorting students by GPA === \n')
GPA_sort = df.sort_values(by=["GPA"], ascending=False)
print(GPA_sort)
print()

# Average GPA by major
print('=== Calculating GPA by major === \n')
avg_GPA_by_major = df.groupby('major')["GPA"].mean()
print(avg_GPA_by_major)
print()