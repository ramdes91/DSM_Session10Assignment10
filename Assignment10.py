
# coding: utf-8

# In[57]:


#We have the min and max temperatures in a city In India for each months of the year.We would like to find a function to describe this and show it graphically. Data: Max = 39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25, Min = 21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18#
import numpy as np

temp_max = np.array([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])
temp_min = np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])

import matplotlib.pyplot as plt
months = np.arange(12)
plt.plot(months, temp_max, 'go')
plt.plot(months, temp_min, 'co')
plt.xlabel('Month')
plt.ylabel('Min and max temperature')


# In[70]:


#1.fitting it to the periodic function#
from scipy import optimize
def yearly_temps(times, avg, ampl, time_offset):
    return (avg
            + ampl * np.cos((times + time_offset) * 1.8 * np.pi / times.max()))

res_max, cov_max = optimize.curve_fit(yearly_temps, months,
                                      temp_max, [40, 20, 0])
res_min, cov_min = optimize.curve_fit(yearly_temps, months,
                                      temp_min, [-40, 20, 0])


# In[71]:


#2.plot the fit#
days = np.linspace(0, 12, num=365)

plt.figure()
plt.plot(months, temp_max, 'go')
plt.plot(days, yearly_temps(days, *res_max), 'm-')
plt.plot(months, temp_min, 'co')
plt.plot(days, yearly_temps(days, *res_min), 'y-')
plt.xlabel('Month')
plt.ylabel('Temperature ($^\circ$C)')

plt.show()


# In[58]:


#This assignment is for visualization using matplotlib:data to use:url=https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')

filename = 'https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic_df = pd.read_csv('https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv')
titanic_df.head()


# In[59]:


titanic_df.info()


# In[60]:


#1.pie chart presenting the male/female proportion#
def draw_plot(titanic_df):
    proportions = []
    sum_instances = titanic_df['sex'].value_counts()
    length = len(titanic_df['sex'])
    proportions = list(sum_instances)
    labels = ['Males','Females']
    explode = (0,0.1)
    sizes = proportions
    fig, ax1 = plt.subplots(figsize = (6,6))
    ax1.pie(sizes, explode = explode, labels = labels, shadow = True, startangle=90)
    ax1.axis('equal')
    ax1.set_title("Sex Proportions")
    return plt.show()
draw_plot(titanic_df)


# In[61]:


#2.scatter plot with the Fare paid and the Age, differ the plot color by gender#
plt.scatter(titanic_df['age'], titanic_df['fare'], alpha=0.5, c=pd.factorize(titanic_df['sex'])[0])

