# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:37:13 2020

@author: shahid
"""

import pandas as pd
import numpy as np


#our own date parser
mydateparser = lambda x: pd.to_datetime(x, format='%Y-%m-%d %H:%M')

#Required Columns

Columns=["Date","Country","RegionCode","RegionName","ProvinceCode","ProvinceName","TotalPositiveCases"]

#Read and parse the dates as index
covid_italy=pd.read_csv("covid19_italy_province.csv",
                        usecols=Columns,
                         index_col='Date', parse_dates=True,date_parser=mydateparser)

#Remove the time from index column
covid_italy.index = covid_italy.index.date

#groupby date total cases
covid_italy_by_date =pd.DataFrame(covid_italy.groupby(covid_italy.index)
["TotalPositiveCases"].sum())


#Create a new column with each day increase
covid_italy_by_date['new_cases']= (covid_italy_by_date['TotalPositiveCases']- covid_italy_by_date['TotalPositiveCases'].shift
                   (1)).fillna(covid_italy_by_date['TotalPositiveCases'])




covid_region = covid_italy.drop(["Country","RegionCode","ProvinceCode",
                                 "ProvinceName"],axis=1).reset_index().rename(columns={'index': 'date'}).set_index(['RegionName']).sort_index()
#groupby date total cases by region
covid_region_by_date=covid_region.groupby([covid_region.index,'date']).sum()

#create a new column with new cases but they are some problems due to multiple regions
covid_region_by_date['new_cases']= (covid_region_by_date['TotalPositiveCases']-
                    covid_region_by_date['TotalPositiveCases'].shift(1)).fillna(covid_region_by_date['TotalPositiveCases'])

#Need dae for comparison so remove it from index
covid_region_by_date.reset_index(level=1, drop=False,inplace= True)

#create a new column to check if date in increasing so when it decreases we are in different region data
covid_region_by_date["diff"] = covid_region_by_date["date"].diff(1).dt.days < 0

#based on mask created make 0 as it is first day
covid_region_by_date['new_cases'] = np.where(covid_region_by_date['diff']==False, 
                    covid_region_by_date['new_cases'], covid_region_by_date['TotalPositiveCases'])
covid_region_by_date.drop(["diff"],axis=1,inplace=True)



covid_province = covid_italy.drop(["Country","RegionCode","ProvinceCode",
                                 "RegionName"],
axis=1).reset_index().rename(columns={'index': 'date'}).set_index(['ProvinceName']).sort_index()

#groupby date total cases by province
covid_province_by_date=covid_region.groupby([covid_region.index,'date']).sum()

#create a new column with new cases but they are some problems due to multiple provinces
covid_province_by_date['new_cases']= (covid_province_by_date['TotalPositiveCases']- 
                      covid_province_by_date['TotalPositiveCases'].shift(1)).fillna(covid_province_by_date['TotalPositiveCases'])

#Need dae for comparison so remove it from index
covid_province_by_date.reset_index(level=1, drop=False,inplace= True)

#create a new column to check if date in increasing so when it decreases we are in different provinces data
covid_province_by_date["diff"] = covid_province_by_date["date"].diff(1).dt.days < 0

#based on mask created make 0 as it is first day
covid_province_by_date['new_cases'] = np.where(covid_province_by_date['diff']==False,
                      covid_province_by_date['new_cases'], covid_province_by_date['TotalPositiveCases'])
covid_province_by_date.drop(["diff"],axis=1,inplace=True)









