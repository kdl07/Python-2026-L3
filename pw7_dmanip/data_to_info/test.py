import pandas as pd
df_students = pd.read_csv('students.csv')
df_scores = pd.read_csv('scores.csv')

# Check missing value
print('===== Checking missing values ===== \n')
print('=== Students.csv === \n')
print(df_students.isnull().sum())
print()
print('=== Scores.csv === \n')
print(df_scores.isnull().sum())
print()

# Fill missing datas
df_students.fillna({"GPA": 3.0, "age": 18}, inplace=True)
df_scores.fillna({"python": 80, "math": 80, "database": 90}, inplace=True)

# Merge 2 data sets
print('===== Merged data set ===== \n')
df_merged = pd.merge(df_students, df_scores, on='student_id')
print(df_merged.head()) # Preview the first few rows
print()

# Calculate average score each student
print('===== Personal average score ===== \n')
score_columns = ['python', 'math', 'database']
df_merged['average_score'] = df_merged[score_columns].mean(axis=1)
print(df_merged)
print()

# Top 5 students
print('===== Top 5 Students ===== \n')
top_5_students = df_merged.sort_values(by='average_score', ascending=False).head(5)
print(top_5_students[['student_id', 'name', 'major', 'average_score']])
print()

# Average score by major
print('===== Average Score by Major ===== \n')
avg_by_major = df_merged.groupby('major')['average_score'].mean()
print(avg_by_major)
