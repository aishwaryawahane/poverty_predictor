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
        self.survey_df = dta_file[['hv001', 'hv271', 'hv270']].rename(columns={'hv001': 'DHSCLUST', 'hv270':'wealth_asset_index', 'hv271': 'Average Wealth'})
        return self.survey_df
