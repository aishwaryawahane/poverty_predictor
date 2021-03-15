# Importing necessary libraries
from .nightlight_features import create_square, nightlight_intensity_calc
import pandas as pd


def merge_dhs(gps_data, survey_data):

    # Prepare survey dataset for merging with gps dataset
    survey_data = survey_data[['hv001', 'hv271']].rename(columns={'hv001': 'Cluster Number', 'hv271':'Wealth Score'})
    survey_data['Wealth Score'] = survey_data['Wealth Score']/100000
    survey_data['Cluster Number'] = survey_data['Cluster Number'].astype('float64')

    # Prepare gps dataset for merging with survey dataset
    gps_data = gps_data[['DHSCLUST', 'LATNUM', 'LONGNUM']].rename(columns={'DHSCLUST': 'Cluster Number', 'LATNUM': 'Latitude', 'LONGNUM':'Longitude'})

    # Merging the two dataframes
    dhs_df = pd.merge(gps_data, survey_data, on='Cluster Number')
    dhs_df = dhs_df.groupby(["Cluster Number", "Latitude", "Longitude"])['Wealth Score'].mean().reset_index()
    return dhs_df

def merge_night_dhs(dhs_df, tiff_path):
    dhs_nightlight_df = dhs_df.apply(lambda x: nightlight_intensity_calc(tiff_path, [x['Cluster Number'], x['Latitude'], x['Longitude'], x['Wealth Score']]), axis=1)
    return dhs_nightlight_df
