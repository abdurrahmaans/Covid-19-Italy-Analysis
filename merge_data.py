# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:58:27 2020

@author: shahi
"""
from code_italy import covid_italy_by_date,covid_region_by_date
from covid_total_test import covid_tests_italy_by_date,covid_tests_region_by_date

covid_tests_italy_by_date=covid_tests_italy_by_date.add_suffix('_t')
covid_tests_region_by_date=covid_tests_region_by_date.add_suffix('_t')



covid_italy_by_date["TotalPositiveCases_t"] = covid_tests_italy_by_date["TotalPositiveCases_t"]
covid_italy_by_date["TestsPerformed_t"] = covid_tests_italy_by_date["TestsPerformed_t"]
covid_italy_by_date["new_test_t"] = covid_tests_italy_by_date["new_test_t"]


covid_italy_by_date["diff"]=covid_italy_by_date["TotalPositiveCases_t"] == covid_italy_by_date["TotalPositiveCases"]

indexNames = covid_italy_by_date[ (covid_italy_by_date['diff'] != True) ].index
covid_italy_by_date.drop(indexNames , inplace=True)





covid_region_by_date["TotalPositiveCases_t"] = covid_tests_region_by_date["TotalPositiveCases_t"]
covid_region_by_date["TestsPerformed_t"] = covid_tests_region_by_date["TestsPerformed_t"]
covid_region_by_date["new_tests_t"] = covid_tests_region_by_date["new_tests_t"]


covid_region_by_date["diff"]=covid_region_by_date["TotalPositiveCases_t"] == covid_region_by_date["TotalPositiveCases"]

covid_region_by_date=covid_region_by_date[covid_region_by_date["diff"]== True]
covid_region_by_date= covid_region_by_date[covid_region_by_date["new_tests_t"] >= 0]


covid_italy_final=covid_italy_by_date.drop(["TotalPositiveCases_t","diff"],axis=1)
covid_region_final=covid_region_by_date.drop(["TotalPositiveCases_t","diff"],axis=1)


covid_italy_final["per_day_total_rate"]=covid_italy_final["TotalPositiveCases"]/covid_italy_final["TestsPerformed_t"]
covid_italy_final["per_day_rate"]=covid_italy_final["new_cases"]/covid_italy_final["new_test_t"]



