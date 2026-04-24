import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pickle
import os
import numpy as np

def train_model():
    # Connect to the database
    db_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'farmer_data.db')
    conn = sqlite3.connect(db_path)
    
    # Load data
    df_prices = pd.read_sql_query("SELECT * FROM crop_prices", conn)
    df_rainfall = pd.read_sql_query("SELECT * FROM rainfall", conn)
    
    conn.close()
    
    # Merge data on date and market
    df = pd.merge(df_prices, df_rainfall, on=['date', 'market'])
    
    if df.empty:
        print("No data found for training.")
        return

    # Generate synthetic temperature data
    np.random.seed(42)
    df['temperature'] = np.random.randint(20, 36, size=len(df))
    
    # Encode 'crop' category
    le = LabelEncoder()
    df['crop_encoded'] = le.fit_transform(df['crop'])
    
    # Store the label encoder
    encoder_path = os.path.join(os.path.dirname(__file__), '..', 'label_encoder.pkl')
    with open(encoder_path, 'wb') as f:
        pickle.dump(le, f)
    
    # Select features and target
    # features: rainfall, temperature, crop_encoded
    X = df[['rainfall_mm', 'temperature', 'crop_encoded']]
    y = df['price_per_kg']
    
    # Train Linear Regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Save the model
    model_path = os.path.join(os.path.dirname(__file__), '..', 'model.pkl')
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    
    print(f"Model trained with {len(df)} rows.")
    print(f"Crops covered: {list(le.classes_)}")
    print(f"Model saved to {model_path}")
    print(f"Encoder saved to {encoder_path}")

if __name__ == "__main__":
    train_model()
