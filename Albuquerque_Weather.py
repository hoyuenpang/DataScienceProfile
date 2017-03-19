#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 14:35:19 2017

@author: Ho-Yuen Henry Pang
"""
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import numpy as np


'''
Extract data
'''

df = pd.read_csv('c90b2d1a390d0c37060efd9692871c1da343f617720b7a6143831c7f.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month   
df['Day'] = df['Date'].dt.day

''' 
Calculating for 2005-2014 
'''
df_2005_2014 = df.copy()
df_2005_2014 = df_2005_2014[(df_2005_2014['Year']>=2005) & (df_2005_2014['Year']<2015)]
  
df_TMAX_copy = df_2005_2014.copy()
df_TMAX_copy = df_TMAX_copy[df_TMAX_copy['Element'] == 'TMAX' ]
df_TMAX_copy = df_TMAX_copy.groupby(['Month', 'Day']).agg({'Data_Value': np.max})
df_TMAX_copy['Data_Value'] = df_TMAX_copy['Data_Value']/10
df_TMAX_copy.reset_index(inplace=True)
df_TMAX_copy = df_TMAX_copy.drop(59)
df_TMAX_copy = df_TMAX_copy.groupby(['Month', 'Day']).agg({'Data_Value': np.max})
df_TMAX_copy.reset_index(inplace=True)
df_TMAX_copy['Number_of_Days'] = df_TMAX_copy.index
TMAX_2005_2014 = df_TMAX_copy.Data_Value
Day_Index = df_TMAX_copy.Number_of_Days
TMAX_2005_2014 = TMAX_2005_2014.tolist()
Day_Index = Day_Index.tolist()

df_TMIN_copy = df_2005_2014.copy()
df_TMIN_copy = df_TMIN_copy[df_TMIN_copy['Element'] == 'TMIN' ]
df_TMIN_copy = df_TMIN_copy.groupby(['Month', 'Day']).agg({'Data_Value': np.min})
df_TMIN_copy['Data_Value'] = df_TMIN_copy['Data_Value']/10
df_TMIN_copy.reset_index(inplace=True)
df_TMIN_copy = df_TMIN_copy.drop(59)            
df_TMIN_copy = df_TMIN_copy.groupby(['Month', 'Day']).agg({'Data_Value': np.min})
df_TMIN_copy.reset_index(inplace=True)
df_TMIN_copy['Number_of_Days'] = df_TMIN_copy.index
TMIN_2005_2014 = df_TMIN_copy.Data_Value
'''
Day_Index = df_TMAX_copy.Number_of_Days         
'''          
TMIN_2005_2014 = TMIN_2005_2014.tolist()





''' 
Calculating for 2015 
'''
df_2015 = df.copy()
df_2015 = df_2015[df_2015['Year']==2015]
  
df_2015_TMAX_copy = df_2015.copy()
df_2015_TMAX_copy = df_2015_TMAX_copy[df_2015_TMAX_copy['Element'] == 'TMAX' ]
df_2015_TMAX_copy = df_2015_TMAX_copy.groupby(['Month', 'Day']).agg({'Data_Value': np.max})
df_2015_TMAX_copy['Data_Value'] = df_2015_TMAX_copy['Data_Value']/10
df_2015_TMAX_copy.reset_index(inplace=True)
df_2015_TMAX_copy['Number_of_Days'] = df_2015_TMAX_copy.index
TMAX_2015 = df_2015_TMAX_copy.Data_Value
Day_Index = df_2015_TMAX_copy.Number_of_Days
TMAX_2015 = TMAX_2015.tolist()
Day_Index = Day_Index.tolist()

df_2015_TMIN_copy = df_2015.copy()
df_2015_TMIN_copy = df_2015_TMIN_copy[df_2015_TMIN_copy['Element'] == 'TMIN' ]
df_2015_TMIN_copy = df_2015_TMIN_copy.groupby(['Month', 'Day']).agg({'Data_Value': np.min})
df_2015_TMIN_copy['Data_Value'] = df_2015_TMIN_copy['Data_Value']/10
df_2015_TMIN_copy.reset_index(inplace=True)
df_2015_TMIN_copy['Number_of_Days'] = df_2015_TMIN_copy.index
TMIN_2015 = df_2015_TMIN_copy.Data_Value
'''
Day_Index = df_TMAX_copy.Number_of_Days         
'''          
TMIN_2015 = TMIN_2015.tolist()

'''
Find the breaking record of 2015
'''
TMAX_Record = []
TMAX_Record_Day =[]
for i in range(len(TMAX_2015)):
    if TMAX_2015[i] > TMAX_2005_2014[i]:
        TMAX_Record.append(TMAX_2015[i])
        TMAX_Record_Day.append(Day_Index[i])


        
TMIN_Record = []
TMIN_Record_Day =[]
for i in range(len(TMIN_2015)):
    if TMIN_2015[i] < TMIN_2005_2014[i]:
        TMIN_Record.append(TMIN_2015[i])
        TMIN_Record_Day.append(Day_Index[i])


'''
Set up the month marker on the x-label
'''
fig = plt.figure(figsize=(10,6))
pos = [1,32,60,91,121,152,182,213,244,274,305,335]
Mon = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

'''
Codes for plotting
'''

plt.plot(TMAX_2005_2014, '-', color='#EF9A9A', label='2005-2014 High')
plt.plot(TMIN_2005_2014, '-', color='#64B5F6', label='2005-2014 Low')

'''
Fill between two lines
'''
plt.gca().fill_between(range(len(TMAX_2005_2014)), 
                       TMAX_2005_2014, TMIN_2005_2014, 
                       facecolor='#E0E0E0', 
                       alpha=0.25)

'''
plt.plot(Day_Index, TMAX_2005_2014, '-r', Day_Index, TMIN_2005_2014, '-b')
'''
plt.scatter(TMAX_Record_Day, TMAX_Record, s=4, c='red', label='2015 Record High')
plt.scatter(TMIN_Record_Day, TMIN_Record, s=4, c='blue', label='2015 Record Low')
plt.xticks(pos,Mon,rotation=45,fontsize=10,color='black')

# add a label to the x axis
plt.xlabel('Month')
# add a label to the y axis
plt.ylabel('Temperature (C)')
# add a title
plt.title('Albuquerque Temperature 2005-2015')
# add legend

# plt.legend(['2005-2014 High', '2005-2014 Low', '2015 Record High', '2015 Record Low'],loc=8)
plt.legend(loc=8, frameon=False, title='Legend')

plt.show()

''' Save figure to png'''
fig.savefig('ABQ_Weather_2005-2015.png')