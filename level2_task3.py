import pandas as pd

# Sample data for demonstration purposes
data = {
    'Restaurant Name': ['A', 'B', 'C'],
    'Address': ['123 Street', '456 Avenue', '789 Boulevard'],
    'Has Table booking': ['Yes', 'No', 'Yes'],
    'Has Online delivery': ['No', 'Yes', 'No'],
    # Add other columns here
}

df = pd.DataFrame(data)

# Extracting additional features
df['Name_Length'] = df['Restaurant Name'].apply(len)
df['Address_Length'] = df['Address'].apply(len)

# Encoding categorical variables
df['Has_Table_Booking'] = df['Has Table booking'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Has_Online_Delivery'] = df['Has Online delivery'].apply(lambda x: 1 if x == 'Yes' else 0)

# Dropping original categorical columns if needed
df.drop(['Has Table booking', 'Has Online delivery'], axis=1, inplace=True)

# Display the dataframe with new features
print(df)
