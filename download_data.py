# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 17:34:47 2017

This script downloads the files from the ftp endpoint.

@author: louis.schamroth-gree
"""
from urllib.request import urlretrieve



precipitation_path = "ftp://ftp.cdc.noaa.gov/Datasets/udel.airt.precip/precip.mon.total.v401.nc"
temperature_path = "ftp://ftp.cdc.noaa.gov/Datasets/udel.airt.precip/air.mon.mean.v401.nc"

#%%

urlretrieve(precipitation_path,filename = 'data/precipitation.nc')
urlretrieve(temperature_path,filename = 'data/temp.nc')
