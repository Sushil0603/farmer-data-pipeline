import pandas as pd
import sqlite3
import os

def export_reports():
    conn = sqlite3.connect("database/farmer_data.db")

    # 1️⃣ Average price per crop
    avg_price_crop = pd.read_sql("""
        SELECT crop, AVG(price_per_kg) AS avg_price
        FROM crop_prices
        GROUP BY crop
    """, conn)

    # 2️⃣ Average price per market
    avg_price_market = pd.read_sql("""
        SELECT market, AVG(price_per_kg) AS avg_price
        FROM crop_prices
        GROUP BY market
    """, conn)

    # 3️⃣ Average rainfall per market (✅ FIXED)
    avg_rainfall = pd.read_sql("""
        SELECT market, AVG(rainfall_mm) AS avg_rainfall
        FROM rainfall
        GROUP BY market
    """, conn)

    conn.close()

    os.makedirs("reports", exist_ok=True)

    with pd.ExcelWriter("reports/farmer_reports.xlsx", engine="openpyxl") as writer:
        avg_price_crop.to_excel(writer, sheet_name="Avg_Price_By_Crop", index=False)
        avg_price_market.to_excel(writer, sheet_name="Avg_Price_By_Market", index=False)
        avg_rainfall.to_excel(writer, sheet_name="Avg_Rainfall_By_Market", index=False)

    print("✅ Excel report generated successfully!")

if __name__ == "__main__":
    export_reports()
