# Importing necessary libraries
from geopandas import read_file
import pandas as pd

# Create a class to acquire DHS survey and GPS datasets
class GetDHSData():
    def __init__(self, gps_path, survey_path):
        self.gps_path = gps_path
        self.survey_path = survey_path

    # Creating a function to get GPS data
    def gps_df(self):
        shapefile_df = read_file(self.gps_path)
        self.location_df = shapefile_df[['DHSCLUST', 'LATNUM', 'LONGNUM']]
        return self.location_df

    # Reading the survey (.dta/stata) file to get the wealth asset data
    def survey_df(self):
        dta_file = pd.read_stata(self.survey_path)
        survey_df = dta_file[['hv001', 'hv271', 'hv270']].rename(columns={'hv001': 'DHSCLUST', 'hv270':'wealth_asset_index', 'hv271': 'Average Wealth'})
        survey_df['Average Wealth'] = survey_df['Average Wealth']/100000
        survey_df['wealth_asset_index'] = survey_df['wealth_asset_index'].map({'poorest':1, 'poorer':2, 'middle':3, 'richer':4, 'richest':5})
        survey_df['wealth_asset_index'] = survey_df['wealth_asset_index'].astype('int16')
        self.survey_df = survey_df.groupby('DHSCLUST')[['Average Wealth','wealth_asset_index']].median().reset_index()
        return self.survey_df

    # Merging location_df and survey_df to get wealth_df
    def merged_wealth(self):
        wealth_df = pd.merge(self.location_df, self.survey_df, on = 'DHSCLUST')
        wealth_df = wealth_df.rename(columns={'DHSCLUST':'Cluster Number', 'LATNUM':'Latitude', 'LONGNUM':'Longitude','wealth_asset_index':'Asset Index'})
        return wealth_df
