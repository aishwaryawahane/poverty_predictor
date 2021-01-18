# Importing necessary libraries
from geopandas import read_file
import pandas as pd

# Create a class to acquire DHS survey and GPS datasets
class DHSData():
    def __init__(self, gps_path, survey_path):
        self.gps_path = gps_path
        self.survey_path = survey_path

    # Creating a function to get GPS data
    def gps_df(self):
        shapefile_df = read_file(self.gps_path)
        self.location_df = shapefile_df[['DHSCLUST', 'LATNUM', 'LONGNUM']].rename(columns={'DHSCLUST': 'Cluster Number', 'LATNUM': 'Latitude', 'LONGNUM':'Longitude'})
        return self.location_df

    # Reading the survey (.dta/stata) file to get the wealth asset data
    def survey_df(self):
        dta_file = pd.read_stata(self.survey_path)
        self.survey_df = dta_file[['hv001', 'hv270']].rename(columns={'hv001': 'Cluster Number', 'hv270':'Wealth Asset Index'})
        return self.survey_df
