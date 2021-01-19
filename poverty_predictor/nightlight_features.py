import rasterio
import numpy as np
import pandas as pd

def read_raster(raster_file):
    raster_data = rasterio.open(raster_file)
    return raster_data

def get_nighttime_features(raster_data, dhs_sample):
    clust_n, lat, long, wealth_idx = dhs_sample
    lon_idx, lat_idx = raster_data.index(long, lat)

    # Getting data for all the raster bands
    bands_array = raster_data.read()
    n_bands, rows, columns = bands_array.shape

    # Generate 10*10 pixels - each pixel is roughly 1km & we need 10km*10km area
    left_idx = lon_idx - 5
    right_idx = lon_idx + 4
    up_idx = lat_idx - 5
    low_idx = lat_idx + 4

    luminosity_100 = []
    for i in range(left_idx, right_idx + 1):
        for j in range(up_idx, low_idx + 1):
            # Get the luminosity of this pixel
            luminosity = bands_array.T[j, i, 0]
            luminosity_100.append(luminosity)
    luminosity_100 = np.asarray(luminosity_100)
    mean_ = np.mean(luminosity_100)
    median_ = np.median(luminosity_100)
    return pd.Series({'Cluster Number': clust_n, 'Mean_nightlight': mean_, 'Median_nightlight': median_, 'Wealth Index': wealth_idx})
