# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 13:57:08 2020

@author: shahi
"""
from merge_data import covid_italy_final
import seaborn as sns
import matplotlib.pyplot as plt

#relationship with date and cases increase
plt.figure(1)
covid_italy_final.TotalPositiveCases.plot(figsize=(12, 5),color='green',
                                          linestyle='solid',
                                          linewidth=5)
plt.title('Total Cases Increase',size=20)
plt.xlabel('date')
plt.ylabel('Total Cases ()')
plt.xticks(rotation=45)


plt.figure(2)
covid_italy_final.new_cases.plot(figsize=(12, 5),color='green',
                                         linestyle='dotted',
                                          linewidth=5)
plt.title('Cases increase rate',size=15)
plt.xlabel('date')
plt.ylabel('case increase per day')
plt.xticks(rotation=45)


#Direct corellation between increasing cases and increase in tests can be seen

plt.figure(3)
plt.figure(figsize=(10, 6))
ax = sns.scatterplot(x="TotalPositiveCases", y="TestsPerformed_t", data=covid_italy_final)
ax.set_title("Relationship b/w Total Cases and Tests Done",size=20)
ax.set(xlabel='Total cases', ylabel='Total Tests')
plt.show()

plt.figure(4)
plt.figure(figsize=(10, 6))
ax = sns.scatterplot(x="new_cases", y="new_test_t", data=covid_italy_final)
ax.set_title("Relationship b/w new Total Cases and new Tests Done",size=20)
ax.set(xlabel='Increase in cases', ylabel='Increase in Tests')
plt.show()

