# Importing necessary libraries
from geopandas import read_file
import pandas as pd

# Create a class to acquire DHS survey and GPS datasets
class GetDHSData():
    # Instatantiating this class will read the raw gps and survey dataframes
    def __init__(self, gps_path, survey_path):
        self.shapefile_df = read_file(gps_path)
        self.dta_df = pd.read_stata(survey_path)

    # Creating a function to get GPS data
    def gps_df(self):
        self.location_df = self.shapefile_df[['DHSCLUST', 'LATNUM', 'LONGNUM']].rename(columns={'DHSCLUST': 'Cluster Number', 'LATNUM': 'Latitude', 'LONGNUM':'Longitude'})
        return self.location_df

    # Reading the survey (.dta/stata) file to get the wealth asset data
    def survey_df(self):
        self.survey_df = self.dta_df[['hv001', 'hv271']].rename(columns={'hv001': 'Cluster Number', 'hv271':'Wealth Score'})
        return self.survey_df
