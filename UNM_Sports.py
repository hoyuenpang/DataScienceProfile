#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 12:37:00 2017

@author: Ho-Yuen Henry Pang
"""

import pandas as pd
import matplotlib.pyplot as plt

'''
Idea of this class project:
    
Albuquerque is a small town. Only big sports teams are University of 
New Mexico Football team and Basketball team. Since UNM is a small school, 
low in academic and sports reputation, and lack of funding for sports. 
It cannot devote enough resource for recruiting both top high school football 
players and top high school basketball players. Funding issue also affects
recruting top football coaching staff and top basketball coaching staff.
Top prospects normally prefer top famous sports school or top academic 
college. 

My hypothesis is that if 
UNM builds a good football program, UNM basketball program will suffer. If 
UNM builds a good basketball  program, UNM football program will suffer.

This can be seen in a 10 year moving average plot for last 50 years

'''

'''
UNM Lobos Football season recorded is from 
http://www.sports-reference.com/cfb/schools/new-mexico/

UNM Lobos Baskerball season recorded is from 
http://www.sports-reference.com/cbb/schools/new-mexico/

'''


'''
Lobos Football 10 year moving average 
'''
df_Lobos_Football = pd.read_csv('LobosFootball.csv')
df_Lobos_Football = df_Lobos_Football.where(df_Lobos_Football['Year'] >= 1959).dropna()
df_Lobos_Football['Y_Index'] = df_Lobos_Football['Year']
df_Lobos_Football['Per_MA_10Y'] = df_Lobos_Football['MA_10Y']*100
df_Lobos_Football = df_Lobos_Football.set_index('Y_Index')
df_Lobos_Football = df_Lobos_Football.sort_index(ascending=True)
df_UNM_FB_copy = df_Lobos_Football.copy()
UNM_FB_MA_10Y = df_UNM_FB_copy.Per_MA_10Y

'''
Lobos Basketball 10 year moving average 
'''
df_Lobos_Basketball = pd.read_csv('LobosBasketball.csv')
df_Lobos_Basketball = df_Lobos_Basketball.where(df_Lobos_Basketball['Year'] >= 1959).dropna()
df_Lobos_Basketball['Y_Index'] = df_Lobos_Basketball['Year']
df_Lobos_Basketball['Per_MA_10Y'] = df_Lobos_Basketball['MA_10Y']*100
df_Lobos_Basketball = df_Lobos_Basketball.set_index('Y_Index')
df_Lobos_Basketball = df_Lobos_Basketball.sort_index(ascending=True)
df_UNM_BB_copy = df_Lobos_Basketball.copy()
UNM_BB_MA_10Y = df_UNM_BB_copy.Per_MA_10Y


'''
Set up the year marker on the x-label
'''
fig = plt.figure(figsize=(10,6))
pos = [2,12,22,32,42,52]
Mon = ['1960','1970','1980','1990','2000','2010']

plt.ylim([0,100])

plt.plot(UNM_FB_MA_10Y, '-', color='#EF9A9A', label='Lobos Football')
plt.plot(UNM_BB_MA_10Y, '-', color='#64B5F6', label='Lobos Basketball')


# add a label to the x axis
plt.xlabel('Season')
# add a label to the y axis
plt.ylabel('10 Year Moving Average Winning %')
# add a title
plt.title('University of New Mexico Sports Team Winning Percentage')
# add legend

plt.legend(loc=8, frameon=False, title='Legend')


'''
plt.show()
'''
fig.savefig('UNM_Sports.png')