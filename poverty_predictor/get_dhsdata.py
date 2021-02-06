# Importing necessary libraries
from geopandas import read_file
import pandas as pd
import os
import glob

# Create a class to acquire raw DHS survey and GPS datasets
class GetDHSData():

    def __init__(self):
        directory = os.path.dirname(__file__)
        csv_path = os.path.join(directory, '..', 'data', 'Malawi_15')
        self.gps_path = os.path.join(csv_path, 'GPS', '*.shp')
        self.survey_path = os.path.join(csv_path, 'Survey', '*.DTA')

    def gps_df(self):
        gps_files = glob.glob(self.gps_path)
        location_df = read_file(gps_files[0])
        return location_df

    def survey_df(self):
        survey_files = glob.glob(self.survey_path)
        survey_df = pd.read_stata(survey_files[0])
        return survey_df
