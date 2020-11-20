#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:23:22 2020

@author: shivam
"""

import pandas as pd
import geopandas as gpd
import geopy
import reverse_geocoder as rg
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
locator = Nominatim(user_agent="myGeocoder")
input_dict={
    "coordinates": "28.5310976,77.217792"
    }

coordinates =str(input_dict['coordinates'])
print(type(coordinates))
location = locator.reverse(coordinates)
loc_dict=location.raw
state=(loc_dict.get('address').get('state'))
#print(state)
state_code=0

if state=="Andhra Pradesh":
    state_code=1
elif state=="Arunachal Pradesh":
    state_code=2 
elif state=="Assam":
    state_code=3 
elif state=="Bihar":
    state_code=4 
elif state=="Chhatisgarh":
    state_code=5 
elif state=="Goa":
    state_code=6 
elif state=="Gujrat":
    state_code=7 
elif state=="Haryana":
    state_code=8 
elif state=="Himachal Pradesh":
    state_code=9 
elif state=="Jharkhand":
    state_code=10
elif state=="Karnataka":
    state_code=11 
elif state=="Kerela":
    state_code=12
elif state=="Madhya Pradesh":
    state_code=13
elif state=="Maharashtra":
    state_code=14
elif state=="Manipur":
    state_code=15
elif state=="Meghalaya":
    state_code=16
elif state=="Mizoram":
    state_code=17
elif state=="Nagaland":
    state_code=18 
elif state=="Odisha":
    state_code=19 
elif state=="Punjab":
    state_code=20
elif state=="Rajasthan":
    state_code=21
elif state=="Sikkim":
    state_code=22 
elif state=="Tamil Nadu":
    state_code=23 
elif state=="Telangana":
    state_code=24 
elif state=="Tripura":
    state_code=25 
elif state=="Uttar Pradesh":
    state_code=26 
elif state=="Uttarakhand":
    state_code=27 
elif state=="West Bengal":
    state_code=28 
elif state=="Andaman and Nicobar Island":
    state_code=29 
elif state=="Dadra Nagar Haveli and Daman and Diu":
    state_code=30 
elif state=="Chandigarh":
    state_code=31 
elif state=="Delhi":
    state_code=32 
elif state=="Jammu and Kashmir":
    state_code=33 
elif state=="Lakshadweep":
    state_code=34 
elif state=="Pudducherry":
    state_code=35 
elif state=="Ladakh":
    state_code=36
print(state_code)


 