import pandas as pd

def transform_data(crop_df, rain_df):
    crop_df['date'] = pd.to_datetime(crop_df['date'])
    rain_df['date'] = pd.to_datetime(rain_df['date'])

    crop_df = crop_df.dropna()
    rain_df = rain_df.dropna()

    rain_df.rename(columns={'district': 'market'}, inplace=True)

    return crop_df, rain_df
