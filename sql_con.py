from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = 'root'
password = quote_plus('root')
host = 'localhost'
port = '3306'
database = 'orders'

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")
with engine.connect() as conn:
    print("✅ Connection successful!")
