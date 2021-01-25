# Analysis of poverty data using satellite imagery

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

## Data Sourcing
- Measure of poverty - Average wealth index of each cluster.
- “Ground truth” - DHS Survey datasets.
- Nighttime Satellite imagery - NOAA

## High level overview of the steps
- Firstly, we must determine what should be the measure of poverty for the analysis. Among measures like Average wealth index, expenditure data, etc., I chose wealth index factor score from DHS Surveys as the measure of poverty. For access to the datasets, I applied to DHS [official site](https://dhsprogram.com/Data/) and downloaded household and GPS datasets.
- The two datasets are provided in many formats to make it easier for analysis. I chose .dta for survey dataset and .shp for GPS dataset.
- After merging the two datasets into one, I ran through basic analysis with pandas methods & attributes, and pandas profiling.
