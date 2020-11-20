#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:28:34 2020

@author: shivam
"""

date="2020-11-09 18:25:20.689092"
month=int(date[5:7])
#print(month)
#month=5
season=4
if month == 11 or month == 12 or month==1 or month==2:
    season=2
elif month==6 or month==7 or month==8 or month==9:
    season=1
elif month==3 or month==4:
    season=3
else:
     print("All season")
#print(season)
 