import pandas as pd

# Load the dataset
df = pd.read_csv("marketing_campaign.csv", sep="\t")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display dataset size
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)
print("\nMissing Values:")
print(df.isnull().sum())
# Fill missing values in Income with the median
df["Income"] = df["Income"].fillna(df["Income"].median())

# Check missing values again
print("\nMissing Values After Filling:")
print(df.isnull().sum())

# Check duplicate records
print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())
# Rename column headers
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Display updated column names
print("\nUpdated Column Names:")
print(df.columns)
# Convert dt_customer to datetime format
df["dt_customer"] = pd.to_datetime(df["dt_customer"], dayfirst=True)

# Check the data type
print("\nData Type of dt_customer:")
print(df["dt_customer"].dtype)
print("\nData Type of dt_customer:")
print(df["dt_customer"].dtype)
print("\nData Types:")
print(df.dtypes)

# Save the cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nData cleaning completed successfully!")