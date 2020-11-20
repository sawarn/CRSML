#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 01:09:35 2020

@author: shivam
"""

import pandas as pd
import Reverse_Geocoding
state=Reverse_Geocoding.state_code

df=pd.read_csv("/home/shivam/Downloads/Cat_Crop.csv")
ground_water=df.loc[df["States"]==state , 'Ground Water']
ground_water=float(ground_water.unique())
#print(ground_water))