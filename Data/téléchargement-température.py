# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 10:49:03 2025

@author: User
"""

import cdsapi


dataset = "reanalysis-era5-land"
request = {
    "variable": ["2m_temperature"],
    "year": [str(year) for year in range (1991,2001)],
    "month": [str(month) for month in range(1,13)],
    "day": [str(day) for day in range(1,32)],
    "time": ["12:00"],
    "data_format": "netcdf",
    "download_format": "unarchived",
    "area": [90, -180, 0, 180]
}

client = cdsapi.Client()


target = 'temperature_2m_data.nc'

client.retrieve(dataset, request, target)
