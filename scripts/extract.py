import pandas as pd

def extract_data():
    crop_df = pd.read_csv("data/crop_prices.csv")
    rain_df = pd.read_csv("data/rainfall.csv")
    return crop_df, rain_df

if __name__ == "__main__":
    crop, rain = extract_data()
    print(crop)
    print(rain)
