import geoio
import math
import pandas as pd
import numpy as np

def create_square(lat, lon, s=10):
    """Creates a s km x s km square centered on (lat, lon)"""
    v = (180/math.pi)*(500/6378137)*s
    return lat - v, lon - v, lat + v, lon + v

def nightlight_intensity_calc(tiff_path, dhs_row):
    clust_n, lat, lon, wealth_idx = dhs_row
    min_lat, min_lon, max_lat, max_lon = create_square(lat, lon)

    tiff = geoio.GeoImage(tiff_path)
    tiff_array = np.squeeze(tiff.get_data())

    xminPixel, ymaxPixel = tiff.proj_to_raster(min_lon, min_lat)
    xmaxPixel, yminPixel = tiff.proj_to_raster(max_lon, max_lat)
    xminPixel, yminPixel, xmaxPixel, ymaxPixel = int(xminPixel), int(yminPixel), int(xmaxPixel), int(ymaxPixel)
    intensity_mean = tiff_array[yminPixel:ymaxPixel,xminPixel:xmaxPixel].mean()

    return pd.Series({'Cluster Number': clust_n, 'Mean_nightlight': intensity_mean, 'Wealth Score': wealth_idx})
