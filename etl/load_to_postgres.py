import pandas as pd
from sqlalchemy import create_engine

# UPDATE WITH YOUR PASSWORD
username = "postgres"
password = "chengappa28"
host = "localhost"
port = "5432"
database = "market360"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

# Load processed datasets
sales_summary = pd.read_csv("sales_summary.csv")
customer_summary = pd.read_csv("customer_summary.csv")
inventory_status = pd.read_csv("inventory_status.csv")

# Write to PostgreSQL
sales_summary.to_sql("sales_summary", engine, if_exists="replace", index=False)
customer_summary.to_sql("customer_summary", engine, if_exists="replace", index=False)
inventory_status.to_sql("inventory_status", engine, if_exists="replace", index=False)

print("✅ Data successfully loaded into PostgreSQL!")
