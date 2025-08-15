import pandas as pd
import os
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Import necessary libraries use os for configration
import os
os.environ['KAGGLE_CONFIG_DIR'] = r"C:\Users\vaish\code\mysql_project"

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

print("✅ Kaggle API authenticated successfully!")

# Read CSV
df = pd.read_csv('orders.csv', na_values=['Not Available', 'unknown'])
print(df['Ship Mode'].unique())

# MySQL connection
username = 'root'
password = quote_plus('root')
host = 'localhost'
port = '3306'
database = 'orders'

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")
conn = engine.connect()

# Load data into MySQL
df.to_sql('df_orders', con=conn, index=False, if_exists='append')

print("✅ Data loaded into MySQL successfully!")
df.rename(columns={'Order Id':'order_id', 'City':'city'})
df.columns=df.columns.str.lower()
# df.columns=df.columns.str.replace(' ','_')
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')


# Drop rows where ship_mode is null
df = df.dropna(['ship_mode', 'segment'])
# # Replace with the correct column name if different

# # Print the columns to check their names
# print("Columns in the DataFrame:")
# print(df.columns)

# print("First few rows of the DataFrame:")
# print(df.head())

# Update these variables with the correct column names based on the inspection

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

# #drop cost price list price and discount percent columns
df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)
print("droped column")
print(df)

#convert order date from object data type to datetime
df['order_date']=  pd.to_datetime(df['order_date'],format="%Y-%m-%d")

# conn.execute("DELETE FROM df_orders WHERE ship_mode IS NULL;")