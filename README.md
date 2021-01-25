# Predicting poverty through satellite imagery

## Project domain
An attempt to tackle global issues through Geospatial domain & Machine learning
- UN’s one of the topmost goals is to reduce poverty by 2030.
- This tool is an attempt to help them achieve this goal. 
- Using Machine learning & analysis of geospatial data,    we could predict poverty through satellite imagery.

## The Problem
- Most countries don’t collect much data.
- Scaling up traditional survey based data collection methods are expensive.

## The Solution
Predicting poverty through data sources like satellite imagery is comparatively inexpensive. 
- Upload the satellite imagery to the site
- The model will analyse the image for nighttime luminosity features
- The model predicts the wealth index of the analysed region

# Step 1: Analysis of poverty data using satellite imagery
The first step to realizing a model to predict poverty over a region is to collect and analyse the data. And, these too consist of several baby steps.

## High level overview of the steps
- Firstly, I had to decide which countries can be considered for training the model. I chose Malawi and Rwanda since they have nearly consistently surveyed datasets.
- Next, I had to determine what should be the measure of poverty for the analysis. Among measures like Average wealth index, expenditure data, etc., I chose wealth index factor score from DHS Surveys as the measure of poverty. For access to the datasets, I applied to DHS [official site](https://dhsprogram.com/Data/) and downloaded household and GPS datasets.
- The two datasets are provided in many formats to make it easier for analysis. I chose .dta for survey dataset and .shp for GPS dataset.
- After merging the two datasets into one, I ran through basic analysis with pandas methods & attributes, and pandas profiling.
