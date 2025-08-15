#import libraries


#kaggle datasets download ankitbansal06/retail-orders -f orders.csv
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import os

os.environ['KAGGLE_CONFIG_DIR'] = r"C:\Users\vaish\code\mysql_project"


import csv
import pandas as pd
import zipfile

#load the data into sql server using replace option
import sqlalchemy as sal
from sqlalchemy import create_engine
from  urllib.parse  import quote_plus


# Authenticate the API
# api = KaggleApi()
# api.authenticate()
# # Specify the file path
# file_path = 'C:\\Users\\vaish\\code\\mysql_project\\orders.csv'

# # Check if the file is a ZIP file
# if file_path.endswith('.zip'):
#     with zipfile.ZipFile(file_path, 'r') as zip_ref:
#         zip_ref.extractall('.')

# with open(file_path, 'r', newline='') as csvfile:
#     # Create a CSV reader object
#     csv_reader = csv.reader(csvfile)

df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df['Ship Mode'].unique()
print(df)

# #rename columns names ..make them lower case and replace space with underscore
# df.rename(columns={'Order Id':'order_id', 'City':'city'})
# df.columns=df.columns.str.lower()
# df.columns=df.columns.str.replace(' ','_')

# # Assuming the actual column names are 'actual_list_price_column_name' and 'actual_discount_percent_column_name'
# # Replace with the correct column name if different

# # Print the columns to check their names
# print("Columns in the DataFrame:")
# print(df.columns)

# # Print the first few rows to inspect the data
# print("First few rows of the DataFrame:")
# print(df.head())

# # Update these variables with the correct column names based on the inspection
# list_price_column = 'list_price'  # Replace with the correct column name
# discount_percent_column = 'discount_percent'  # Replace with the correct column name

# # Check if the columns exist in the DataFrame
# if list_price_column in df.columns and discount_percent_column in df.columns:
#     # Calculate the discount
#     df['discount'] = df[list_price_column] * df[discount_percent_column] * 0.01
#     # Print the first few rows to verify
#     print("First few rows with discount calculated:")
#     print(df.head())
# else:
#     print(f"Columns '{list_price_column}' and/or '{discount_percent_column}' do not exist in the DataFrame.")

# #drop cost price list price and discount percent columns
# df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)
# print("droped column")
# print(df)
# #convert order date from object data type to datetime
# df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")
# df

'''----------------------------------------------------------------------------'''
#sql:- connection

username = 'root'
password = quote_plus('root')
host = 'localhost'
port = '3306'  # Default MySQL port is 3306
database = 'orders'

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

conn=engine.connect()

#load the data into sql server using append option
df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')
