# Importing necessary libraries
from .nightlight_features import read_raster, get_nighttime_features
import pandas as pd


def merge_dhs(gps_data, survey_data):

    # Prepare survey dataset for merging with gps dataset
    survey_data['Wealth Score'] = survey_data['Wealth Score']/100000
    survey_data['Cluster Number'] = survey_data['Cluster Number'].astype('float64')
    survey_data = survey_data.groupby('Cluster Number')['Wealth Score'].mean().reset_index()

    # Merge gps and survey datasets
    dhs_df = pd.merge(gps_data, survey_data, on='Cluster Number')
    return dhs_df

def merge_night_dhs(dhs_df, tiff_path):
    raster_data = read_raster(tiff_path)
    dhs_nightlight_df = dhs_df.apply(lambda x: get_nighttime_features(raster_data, [x['Cluster Number'], x['Latitude'], x['Longitude'], x['Wealth Score']]), axis=1)
    return dhs_nightlight_df
