# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:04:53 2020

@author: shahi
"""

import pandas as pd
import numpy as np


mydateparser = lambda x: pd.to_datetime(x, format='%Y-%m-%d %H:%M')

#Required Columns

Columns=["Date","RegionName","TotalPositiveCases","TestsPerformed"]

#Read and parse the dates as index
covid_tests_italy=pd.read_csv("covid19_italy_region.csv",
                        usecols=Columns,
                         index_col='Date', parse_dates=True,date_parser=mydateparser)

covid_tests_italy.index = covid_tests_italy.index.date

#groupby date total cases
covid_tests_italy_by_date =pd.DataFrame(covid_tests_italy.groupby(covid_tests_italy.index)
["TotalPositiveCases","TestsPerformed"].sum())



#Create a new column with each day increase
covid_tests_italy_by_date['new_cases']= (covid_tests_italy_by_date['TotalPositiveCases']- covid_tests_italy_by_date['TotalPositiveCases'].shift
                   (1)).fillna(covid_tests_italy_by_date['TotalPositiveCases'])

covid_tests_italy_by_date['new_test']= (covid_tests_italy_by_date['TestsPerformed']- covid_tests_italy_by_date['TestsPerformed'].shift
                   (1)).fillna(covid_tests_italy_by_date['TestsPerformed'])



covid_tests_region = covid_tests_italy.reset_index().rename(columns={'index': 'date'}).set_index(['RegionName']).sort_index()
#groupby date total cases by region
covid_tests_region_by_date=covid_tests_region.groupby([covid_tests_region.index,'date']).sum()

#create a new column with new cases but they are some problems due to multiple regions
covid_tests_region_by_date['new_cases']= (covid_tests_region_by_date['TotalPositiveCases']-
                    covid_tests_region_by_date['TotalPositiveCases'].shift(1)).fillna(covid_tests_region_by_date['TestsPerformed'])
covid_tests_region_by_date['new_tests']= (covid_tests_region_by_date['TestsPerformed']-
                    covid_tests_region_by_date['TestsPerformed'].shift(1)).fillna(covid_tests_region_by_date['TestsPerformed'])
#Need dae for comparison so remove it from index
covid_tests_region_by_date.reset_index(level=1, drop=False,inplace= True)

#create a new column to check if date in increasing so when it decreases we are in different region data
covid_tests_region_by_date["diff"] = covid_tests_region_by_date["date"].diff(1).dt.days < 0

#based on mask created make 0 as it is first day
covid_tests_region_by_date['new_cases'] = np.where(covid_tests_region_by_date['diff']==False, 
                    covid_tests_region_by_date['new_cases'], covid_tests_region_by_date['TotalPositiveCases'])
covid_tests_region_by_date['new_tests'] = np.where(covid_tests_region_by_date['diff']==False, 
                    covid_tests_region_by_date['new_tests'], covid_tests_region_by_date['TestsPerformed'])

covid_tests_region_by_date.drop(["diff"],axis=1,inplace=True)


