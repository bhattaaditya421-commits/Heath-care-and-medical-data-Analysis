#1 import libraries 
import numpy as np 
import pandas as pd 

#2 load healthcare csv dataset
df=pd.read_csv('healthcare_dataset.csv')

# Create messy data for demonstration

# 1. Add extra spaces in patient name
df.loc[0, 'Name'] = '  john smith  '

# 2. Change gender format
df.loc[1, 'Gender'] = 'm'
df.loc[2, 'Gender'] = 'FEMALE'

# 3. Add missing age
df.loc[3, 'Age'] = np.nan

# 4. Add invalid age
df.loc[4, 'Age'] = 150

# 5. Add negative billing amount
df.loc[5, 'Billing Amount'] = -5000

# 6. Add missing billing amount
df.loc[6, 'Billing Amount'] = np.nan

print("\nMessy Dataset Before Cleaning:")
print(df.head(10))



# 4. Remove Duplicate Records
df = df.drop_duplicates()

# 5. Clean Patient Names
df['Name'] = df['Name'].astype(str).str.strip().str.title()

# 6. Clean Gender
df['Gender'] = df['Gender'].astype(str).str.strip().str.title()

# 7. Clean Blood Type
df['Blood Type'] = df['Blood Type'].astype(str).str.strip().str.upper()

# 8. Clean Medical Condition
df['Medical Condition'] = df['Medical Condition'].astype(str).str.strip().str.title()

# 9. Handle Missing Values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Billing Amount'] = df['Billing Amount'].fillna(df['Billing Amount'].median())

# 10. Clean Date Columns
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'], errors='coerce')
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'], errors='coerce')

# 11. Check Final Dataset
print("\nCleaned Healthcare Dataset:")
print(df.head(10))

print("\nMissing Values:")
print(df.isnull().sum())

# 12. Save Cleaned Dataset
df.to_csv('cleaned_healthcare_dataset.csv', index=False)

print("\nData Cleaning Completed Successfully!") 