
import pandas as pd

df = pd.read_csv("data/ola_raw.csv")

# Clean column names
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
      .str.replace("&", "and")
)

#Fix date format
df['date'] = pd.to_datetime(df['date'], errors='coerce')

#Handle missing values
df = df.fillna({
    'driver_ratings': 0,
    'customer_rating': 0,
    'payment_method': 'Unknown'
})

#Save Cleaned Version
df.to_csv("data/ola_cleaned.csv", index=False)
print("Cleaned dataset saved successfully.")