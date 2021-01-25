# Predicting poverty through satellite imagery

Inspired by the project - [Combining satellite imagery and machine learning to predict poverty](http://sustain.stanford.edu/predicting-poverty)

## Project domain
An attempt to tackle global issues through Geospatial domain & Machine learning
- UN’s one of the topmost goals is to reduce poverty by 2030.
- This tool is an attempt to help them achieve this goal. 
- Using Machine learning & analysis of geospatial data, we could predict poverty through satellite imagery.

## The Problem
- Most countries don’t collect much data.
- Scaling up traditional survey based data collection methods are expensive.

## The Solution
Predicting poverty through data sources like satellite imagery is comparatively inexpensive. 
- Upload the satellite imagery to the site
- The model will analyse the image for nighttime luminosity features
- The model predicts the wealth index of the analysed region

# Step 1: Analysis of poverty data using satellite imagery
The first step to realizing a model to predict poverty over a region was to collect and analyse the data. And, these too consisted of several baby steps.

## High level overview of the steps
- Firstly, I had to decide which countries could be considered for training the model. I chose Malawi and Rwanda since they have nearly consistently surveyed datasets.
- Next, I had to determine what should be the measure of poverty for the analysis. Among measures like Average wealth index, expenditure data, etc., I chose wealth index factor score from DHS Surveys as the measure of poverty, for each cluster (smallest region provided by the public datasets). For access to the datasets, I applied to DHS [official site](https://dhsprogram.com/Data/) and downloaded household and GPS datasets.
- The two datasets are provided in many formats to make it easier for analysis. I chose .dta for survey dataset and .shp for GPS dataset.
- After merging the two datasets into one with the columns - cluster number, location co-ordinates and wealth index factor score, I ran through basic analysis with Pandas methods & attributes.
- Now that I had the 'ground truth' to compare my predictions with (that I'd work on in the near future), the next step was to download the nighttime and daytime satellite imagery. The reason we require both - standard ML techniques to interpret imagery are reliable only when we have lots of labeled images. However, in this caseBut only daytime imagery are difficult to be categorized as rich/poor. Therefore, we will use nightlight satellite imagery to help us find features in the daytime satellite imagery that correlate with poverty measure.
- I obtained the nightlight imagery corresponding to the DHS surveyed years through Earth Observation Group, NOAA/NCEI databsae on their website.
- After obtaining nightlight imagery, I built a script to find average nighttime intensity for each cluster using the DHS shapefile and rasterio python library.
- Finally I conducted a basic analysis through data visualization and pandas profile to know if there exists a correlation between the average nighttime intensity of each cluster and their respective wealth index factor score.
