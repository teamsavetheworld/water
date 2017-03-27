import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import netCDF4
import pandas as pd
import xarray as xr

# Temperature & rainfall data from https://www.esrl.noaa.gov/psd/data/gridded/data.UDel_AirT_Precip.html

# Load in temperature and rainfall data
air_data_file = xr.open_dataset('data/temp.nc',
                                 decode_times=True)
rain_data_file = xr.open_dataset('data/precipitation.nc,
                                 decode_times=True)
df_t = air_data_file.to_dataframe()
df_r = rain_data_file.to_dataframe()

# Reformat data into nice columns
df_t.reset_index(inplace=True)
df_r.reset_index(inplace=True)

# Define monthly timespan
start_date = pd.tslib.Timestamp('2014-01-01 00:00:00')
end_date = pd.tslib.Timestamp('2014-12-01 00:00:00')

# Get mean monthly temperatures for only 2014
df_t = df_t[(df_t.time >= start_date) & (df_t.time <= end_date)]

# Get mean monthly rainfalls for only 2014
df_r = df_r[(df_r.time >= start_date) & (df_r.time <= end_date)]

# TODO: combine dataframes and set some sort of conditions for filtering by humidity
