# Analysis of poverty data using nighttime satellite imagery

Inspired by the project - [Combining satellite imagery and machine learning to predict poverty](http://sustain.stanford.edu/predicting-poverty)

## Project domain
An attempt to tackle global issues through Geospatial domain & Data Science
- UN’s one of the topmost goals is to reduce poverty by 2030.
- This project is an attempt to help them achieve this goal. 
- Through analysis of geospatial data/satellite imagery, we could infer whether satellite imagery could be used to predict poverty.

## The Problem
- Most countries don’t collect much data.
- Scaling up traditional survey based data collection methods are expensive.

## Step 1: Understanding the problem
- Firstly, I had to clearly define the question I am attempting to answer - Could satellite imagery be used to predict poverty?
- The next step was to decide the data source for analysis. Which countries could be considered for the analysis? I chose Rwanda since the country has consistently surveyed datasets.
- Also, among measures like Average wealth index, expenditure data, etc., which measure should be used to predict poverty? Most reliable sources of measure are scores from LSMS data or DHS data. I chose the wealth index factor score from DHS Surveys for each cluster, which are the smallest regions in Rwanda whose co-ordinates are provided by the public datasets.

## Step 2: Data Collection
- I applied to DHS [official site](https://dhsprogram.com/Data/) and downloaded household and GPS datasets for the year 2010. The best part about DHS datasets is that they provide files in various formats to make analysis easier.
- Now that I had access to the 'ground truth', the next step was to download nighttime satellite imagery. The reason we require nighttime images - they could be used as a proxy for determining wealth score of a region based on the development of the region in terms of electricity and availability of power. The brighter the region at night, the richer it might be.
- I obtained the nightlight imagery corresponding to the DHS surveyed years through Earth Observation Group, NOAA/NCEI database on their [website](https://eogdata.mines.edu/dmsp/downloadV4composites.html).

## Step 3: Data preprocessing/cleaning
- This is an essential step for getting reliable results to our analysis. Also, we're producing certain features, such as nighttime luminosity to help solidify our analysis.
- DHS data - after merging the survey and GPS datasets into one, with the columns - cluster number, location co-ordinates and wealth index factor score, I conducted a basic analysis using [Pandas attributes & methods](https://pandas.pydata.org/docs/user_guide/index.html).
- Nighttime imagery - I built a script to find the average nighttime intensity for each cluster using the DHS shapefile (GPS data) and rasterio python library.

## The final step
- Finally, I conducted a basic analysis through data visualization and pandas profile to know if there exists a correlation between the average nighttime intensity of each cluster and their respective wealth index factor score.

<p float="left">
  <img src="https://github.com/aishwaryawahane/poverty_predictor/blob/main/graphs/Rwanda/Correlation.png" width="400" />
  <img src="https://github.com/aishwaryawahane/poverty_predictor/blob/main/graphs/Rwanda/wealthscore_luminosity.png" width="500" />
</p>
