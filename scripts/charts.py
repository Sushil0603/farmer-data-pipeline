import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def generate_charts():
    conn = sqlite3.connect("database/farmer_data.db")

    # Average crop price
    price_df = pd.read_sql("""
        SELECT crop, AVG(price_per_kg) AS avg_price
        FROM crop_prices
        GROUP BY crop
    """, conn)

    # Total rainfall
    rain_df = pd.read_sql("""
        SELECT market, SUM(rainfall_mm) AS total_rainfall
        FROM rainfall
        GROUP BY market
    """, conn)

    conn.close()

    # Chart 1: Average Crop Price
    plt.figure(figsize=(10,10))
    plt.bar(price_df['crop'], price_df['avg_price'])
    plt.xlabel("Crop")
    plt.ylabel("Average Price (₹)")
    plt.title("Average Crop Price")
    plt.xticks(rotation=45)
    plt.savefig("static/charts/avg_crop_price.png")
    plt.close()


    # Chart 2: Total Rainfall
    plt.figure(figsize=(10,10))
    plt.bar(rain_df['market'], rain_df['total_rainfall'])
    plt.xlabel("Market")
    plt.ylabel("Rainfall (mm)")
    plt.title("Total Rainfall by Market")
    plt.xticks(rotation=45)
    plt.savefig("static/charts/total_rainfall.png")
    plt.close()

    print("Charts generated successfully!")

if __name__ == "__main__":
    generate_charts()
