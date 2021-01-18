# Importing necessary libraries
from .raw_dhsdata import DHSData
import pandas as pd

class MergeDHSData(DHSData):

    def merged_dhs(cls):
        # Get DHS survey and gps datasets
        gps_data = cls.gps_df()
        survey_data = cls.survey_df()

        # Prepare survey dataset for merging with gps dataset
        survey_data['Wealth Asset Index'] = survey_data['Wealth Asset Index'].map({'poorest':1, 'poorer':2, 'middle':3, 'richer':4, 'richest':5})
        survey_data['Wealth Asset Index'] = survey_data['Wealth Asset Index'].astype('int64')
        survey_data['Cluster Number'] = survey_data['Cluster Number'].astype('float64')
        survey_data = survey_data.groupby('Cluster Number')['Wealth Asset Index'].median().reset_index()

        # Merge gps and survey datasets
        dhs_data = pd.merge(gps_data, survey_data, on='Cluster Number')
        return dhs_data
