# -*- coding: utf-8 -*-
"""
Created on Tue September 6th, 2017

@author: Daniel.Kuzjak
"""

import requests
from lxml import objectify


parameter = 'tavg'
state_id = 44
climate_division = 0
num_months = 8
num_periods = 6
year = '2016'
template_base = 'http://www.ncdc.noaa.gov/temp-and-precip/climatological-'
template_base = template_base + 'rankings/download.xml?parameter=%s&state=%s&div=%s'
template_add = template_base + '&month=%s&periods[]=%s&year=%s'
insert_these = (parameter, state_id, climate_division,num_months,num_periods,year)
template_add = template_add % insert_these
final_url = template_add

response = requests.get(final_url).content
root = objectify.fromstring(response)


my_wm_username = 'dpkuzjak'

print my_wm_username
print root['data']["value"]
print root['data']["twentiethCenturyMean"]
print root['data']["lowRank"]
print root['data']["highRank"]