import os
os.environ['KAGGLE_CONFIG_DIR'] = r"C:\Users\vaish\code\mysql_project"

import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()


df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df['Ship Mode'].unique()
print(df)

# #rename columns names ..make them lower case and replace space with underscore
df.rename(columns={'Order Id':'order_id', 'City':'city'})
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')

# print("Columns in the DataFrame:")
# print(df.columns)

# # Print the first few rows to inspect the data
# print("First few rows of the DataFrame:")
# print(df.head())

# # Update these variables with the correct column names based on the inspection
list_price_column = 'list_price'  # Replace with the correct column name
discount_percent_column = 'discount_percent'  # Replace with the correct column name


# # Check if the columns exist in the DataFrame
if list_price_column in df.columns and discount_percent_column in df.columns:
    # Calculate the discount
    df['discount'] = df[list_price_column] * df[discount_percent_column] * 0.01
    # Print the first few rows to verify
    print("First few rows with discount calculated:")
    print(df.head())
else:
    print(f"Columns '{list_price_column}' and/or '{discount_percent_column}' do not exist in the DataFrame.")
