import sqlite3
from extract import extract_data
from transform import transform_data

# To Run this code first we have to check the command is open in venv (not then perform this following steps)
## Task	Command
## Activate venv -->	 source venv/bin/activate
## Deactivate venv--> deactivate
def load_data():
    crop_df, rain_df = extract_data()
    crop_df, rain_df = transform_data(crop_df, rain_df)

    conn = sqlite3.connect("database/farmer_data.db")

    crop_df.to_sql("crop_prices", conn, if_exists="replace", index=False)
    rain_df.to_sql("rainfall", conn, if_exists="replace", index=False)

    conn.close()
    print("Data loaded successfully!")

if __name__ == "__main__":
    load_data()
