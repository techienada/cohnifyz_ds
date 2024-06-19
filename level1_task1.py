import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/workspaces/Dataset .csv'  # Replace with your dataset path
df = pd.read_csv(file_path)

# 1. Explore the dataset and identify the number of rows and columns
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")

# 2. Check for missing values in each column
missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)

# Handle missing values (simple strategy: fill with median for numerical columns and mode for categorical columns)
for column in df.columns:
    if df[column].isnull().sum() > 0:
        if df[column].dtype == 'object':
            df[column].fillna(df[column].mode()[0], inplace=True)
        else:
            df[column].fillna(df[column].median(), inplace=True)

# Verify that there are no missing values left
print("Missing values after handling:\n", df.isnull().sum())

# 3. Perform data type conversion if necessary
print("Data types before conversion:\n", df.dtypes)
# Example: Convert a column to a numeric type if it is not already
# df['some_column'] = pd.to_numeric(df['some_column'], errors='coerce')

# Check and convert data types if necessary
# df['column_name'] = df['column_name'].astype('desired_dtype')

# 4. Analyze the distribution of the target variable ("Aggregate rating")
plt.figure(figsize=(10, 6))
sns.countplot(df['Aggregate rating'])
plt.title('Distribution of Aggregate Rating')
plt.xlabel('Aggregate Rating')
plt.ylabel('Count')
plt.show()

# Identify class imbalances
aggregate_rating_counts = df['Aggregate rating'].value_counts()
print("Aggregate rating distribution:\n", aggregate_rating_counts)

# Optional: Handle class imbalance if necessary (e.g., using SMOTE, undersampling, or oversampling)

# Save the cleaned dataset
cleaned_file_path = 'cleaned_dataset.csv'
df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned dataset saved to {cleaned_file_path}")
