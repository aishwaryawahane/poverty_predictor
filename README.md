# Predicting poverty through satellite imagery

Inspired by the project - [Combining satellite imagery and machine learning to predict poverty](http://sustain.stanford.edu/predicting-poverty)

## Project domain
An attempt to tackle global issues through Geospatial domain & Machine learning
- UN’s one of the topmost goals is to reduce poverty by 2030.
- This project is an attempt to help them achieve this goal. 
- Using Machine learning & analysis of geospatial data/satellite imagery, we could predict poverty.

## The Problem
- Most countries don’t collect much data.
- Scaling up traditional survey based data collection methods are expensive.

## The Solution
Predicting poverty through data sources like satellite imagery is reliable and inexpensive. 
- Upload the satellite imagery to the site.
- The model will analyse the imagery for features.
- The model outputs wealth scores of the analysed region.

# Step 1: Analysis of poverty data using satellite imagery
The first step to creating a model was to collect and analyse the data.

## High level overview of analysis
- Firstly, I had to decide which countries could be considered for training the model. I chose Malawi since the country has consistently surveyed datasets.
- Next, among measures like Average wealth index, expenditure data, etc., I chose wealth index factor score from DHS Surveys as the measure of poverty, for each cluster (smallest region, whose co-ordinates are provided by the public datasets). For the access to these datasets, I applied to DHS [official site](https://dhsprogram.com/Data/) and downloaded household and GPS datasets for the year 2015.
- The best part about DHS datasets is that they provide files in various formats to make analysis easier.
- After merging the survey and GPS datasets into one, with the columns - cluster number, location co-ordinates and wealth index factor score, I conducted a basic analysis using [Pandas attributes & methods](https://pandas.pydata.org/docs/user_guide/index.html).
- Now that I had the 'ground truth' to compare my predictions to (that I'd work on in the near future), the next step was to download the nighttime and daytime satellite imagery. The reason we require both - standard ML techniques to interpret imagery are reliable only when we have lots of labeled images. However, in this case daytime imagery are difficult to be categorized as rich/poor. Therefore, we will use nightlight satellite imagery to help us find features in the daytime satellite imagery that correlate with poverty measure.
- I obtained the nightlight imagery corresponding to the DHS surveyed years through Earth Observation Group, NOAA/NCEI database on their [website](https://eogdata.mines.edu/dmsp/downloadV4composites.html).
