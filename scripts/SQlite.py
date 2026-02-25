import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("data/ola_cleaned.csv")

engine = create_engine("sqlite:///ola_rides.db")

df.to_sql("OLA_RIDES", engine, if_exists="replace", index=False)

print("SQLite database created successfully")