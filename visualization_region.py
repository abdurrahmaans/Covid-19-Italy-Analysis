# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:11:35 2020

@author: shahi
"""

from merge_data import covid_region_final
import seaborn as sns
import matplotlib.pyplot as plt



covid_region_final.reset_index(inplace= True)
Total_regions=covid_region_final.RegionName.unique().tolist()


plt.figure(1)
plt.figure(figsize=(14, 10))
ax = sns.lineplot(x="date",y="TotalPositiveCases",hue="RegionName",
             sizes=(1, 10),data=covid_region_final)
ax.set_title("Relationship b/w new Total Cases and date",size=20)
ax.set(xlabel='Increase in cases', ylabel='Dates')
plt.xticks(rotation=45)
plt.show()

i=1
for item in Total_regions:
    plt.figure(i)
    plt.figure(figsize=(10, 6))
    ax = sns.lineplot(x="date",y="TotalPositiveCases",
                      sizes=(1, 10),data=covid_region_final[covid_region_final["RegionName"]== item])
    ax = sns.lineplot(x="date",y="TestsPerformed_t",sizes=(1, 10),data=covid_region_final[covid_region_final["RegionName"]== item])
    ax.set_title("Relationship b/w new Total Cases Tests and date in "+ item,size=17)
    plt.xticks(rotation=45)
    plt.xlabel("Dates",fontsize=12)
    plt.ylabel("Increase in cases and test in" + item,fontsize=12)
    plt.show()
    i=i+1
    
g = sns.FacetGrid(covid_region_final, col="RegionName", hue="RegionName",col_wrap=3)
g.map(plt.plot, "date", "TotalPositiveCases", alpha=.7)
g.map(plt.plot, "date", "TestsPerformed_t", alpha=.7)
g.add_legend();     

g = sns.FacetGrid(covid_region_final, col="RegionName", hue="RegionName",col_wrap=3)
g.map(plt.scatter, "TotalPositiveCases", "TestsPerformed_t", alpha=.7)
g.add_legend();                                  
