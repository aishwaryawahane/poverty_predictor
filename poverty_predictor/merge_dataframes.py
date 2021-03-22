# Importing necessary libraries
from .nightlight_features import create_square, nightlight_intensity_calc
import pandas as pd


def merge_dhs(gps_data, survey_data):

    # Prepare survey dataset for merging with gps dataset
    survey_data = survey_data[['hv001', 'hv271']].rename(columns={'hv001': 'Cluster_Number', 'hv271':'Wealth_Score'})
    survey_data['Wealth_Score'] = survey_data['Wealth_Score']/100000
    survey_data['Cluster_Number'] = survey_data['Cluster_Number'].astype('float64')

    # Prepare gps dataset for merging with survey dataset
    gps_data = gps_data[['DHSCLUST', 'LATNUM', 'LONGNUM']].rename(columns={'DHSCLUST': 'Cluster_Number', 'LATNUM': 'Latitude', 'LONGNUM':'Longitude'})

    # Merging the two dataframes
    dhs_df = pd.merge(gps_data, survey_data, on='Cluster_Number')
    dhs_df = dhs_df.groupby(["Cluster_Number", "Latitude", "Longitude"])['Wealth_Score'].mean().reset_index()
    return dhs_df

def merge_night_dhs(dhs_df, tiff_path):
    dhs_nightlight_df = dhs_df.apply(lambda x: nightlight_intensity_calc(tiff_path, [x['Cluster_Number'], x['Latitude'], x['Longitude'], x['Wealth_Score']]), axis=1)
    return dhs_nightlight_df
