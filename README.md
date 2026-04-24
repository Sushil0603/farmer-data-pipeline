🌾 Farmer Crop Price & Rainfall Data Pipeline

An end-to-end data engineering mini project that ingests agricultural crop price and rainfall data, stores it in a database, generates analytical charts, and exports reports to Excel.
The project also includes a simple Flask-based web dashboard to visualize insights.

📌 Project Overview

This project demonstrates how raw agricultural data can be transformed into meaningful insights using a data pipeline.

Key Capabilities

Ingest CSV datasets (crop prices & rainfall)

Store structured data in SQLite

Perform data analysis using SQL

Generate charts using Matplotlib

Export analytical reports to Excel

Display charts on a web dashboard using Flask

🏗️ Architecture (High Level)
CSV Files
(crop_prices.csv, rainfall.csv)
        ↓
Data Ingestion (Python + Pandas)
        ↓
SQLite Database
        ↓
Data Processing (SQL Queries)
        ↓
Charts & Excel Reports
        ↓
Web Dashboard (Flask + HTML)

📁 Project Structure
farmer-data-pipeline/
│
├── data/
│   ├── crop_prices.csv
│   └── rainfall.csv
│
├── database/
│   └── farmer_data.db
│
├── scripts/
│   ├── extract.py
│   ├── load.py
│   ├── charts.py
│   ├── export_excel.py
│   └── run_pipeline.py
│
├── static/
│   └── charts/
│       ├── avg_crop_price.png
│       └── total_rainfall.png
│
├── templates/
│   └── index.html
│
├── reports/
│   └── farmer_reports.xlsx
│
├── app.py
├── requirements.txt
└── README.md

📊 Datasets Used
1️⃣ Crop Prices (crop_prices.csv)
date,market,crop,price_per_kg
2024-01-01,Pune,Onion,18
2024-01-02,Pune,Onion,20
...

2️⃣ Rainfall (rainfall.csv)
date,market,rainfall_mm
2024-01-01,Pune,12
2024-01-02,Pune,0
...

⚙️ Technologies Used

Python

Pandas

SQLite

SQL

Matplotlib

Flask

OpenPyXL (Excel export)

🚀 How to Run the Project (Step-by-Step)
1️⃣ Create & Activate Virtual Environment (macOS)
python3 -m venv venv
source venv/bin/activate


You should see (venv) in the terminal.

2️⃣ Install Dependencies
pip install -r requirements.txt


If requirements.txt is not present:

pip install pandas matplotlib flask openpyxl

3️⃣ Run the Data Pipeline
python scripts/run_pipeline.py


This will:

Load CSV data into SQLite

Generate charts

4️⃣ Export Excel Reports
python scripts/export_excel.py


Output file:

reports/farmer_reports.xlsx

5️⃣ Run Web Dashboard
python app.py


Open in browser:

http://127.0.0.1:5000

📈 Reports Generated
📊 Charts

Average Crop Price by Crop

Total Rainfall by Market

📑 Excel Sheets

Avg_Price_By_Crop

Avg_Price_By_Market

Avg_Rainfall_By_Market

🧠 How This Project Helps

Helps farmers understand price trends

Supports market-based decision making

Can be extended for price prediction

Ready for dashboard or API integration

🧪 Common Issues & Fixes
Issue	Fix
no such table	Run run_pipeline.py first
no such column	Check CSV headers vs SQL
openpyxl not found	pip install openpyxl
(venv) not showing	source venv/bin/activate
🧑‍🏫 One-Line Explanation (For Mentor / Interview)

“This project is an end-to-end data pipeline that ingests agricultural crop price and rainfall data, processes it using SQL, generates insights through charts and Excel reports, and visualizes them on a web dashboard.”

🔮 Future Enhancements

Live data from government APIs

Price prediction using Machine Learning

Interactive charts using Chart.js / React

Farmer-friendly mobile dashboard

Cloud deployment

👨‍💻 Author

Sushil Yogesh Pednekar
Web Development & Data Engineering Enthusiast