# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:31:52 2024

@author: User
"""

import cdsapi

client = cdsapi.Client()
  
dataset = 'reanalysis-era5-pressure-levels'

request = {
      'product_type': ['reanalysis'],
      'variable': ['geopotential'],
      'year': [str(year) for year in range (1994, 2021)],
      'month': [str(month) for month in range(1,13)],
      'day': [str(day) for day in range(1,32)],
      'time': ['12:00'],
      'pressure_level': ['500'], #hPa
      'area': [90, -180, 0, 180], #hémisphèrenord
      'data_format': 'netcdf',
  }

target = 'geopotential_data_1950-2024.nc'

client.retrieve(dataset, request, target)
