#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:29:02 2016

@author: Ho-Yuen Henry pang
"""

def ttests_real_estate():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    
    '''
    Code of convert_housing_data_to_quarters.py
    '''                                                 

    import pandas as pd
    import numpy as np
    from scipy import stats
    
    states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}
    
    city_all_house_df = pd.read_csv('HomesPrice.csv')
    
    city_all_house_df['State'].replace(states, inplace=True)
    
    columns_to_keep = ['State', 'RegionName', 
                       '2000-01', '2000-02', '2000-03', '2000-04',
                       '2000-05', '2000-06', '2000-07', '2000-08',
                       '2000-09', '2000-10', '2000-11', '2000-12',
                       
                       '2001-01', '2001-02', '2001-03', '2001-04',
                       '2001-05', '2001-06', '2001-07', '2001-08',
                       '2001-09', '2001-10', '2001-11', '2001-12',
                       
                       '2002-01', '2002-02', '2002-03', '2002-04',
                       '2002-05', '2002-06', '2002-07', '2002-08',
                       '2002-09', '2002-10', '2002-11', '2002-12',
                       
                       '2003-01', '2003-02', '2003-03', '2003-04',
                       '2003-05', '2003-06', '2003-07', '2003-08',
                       '2003-09', '2003-10', '2003-11', '2003-12',
                       
                       '2004-01', '2004-02', '2004-03', '2004-04',
                       '2004-05', '2004-06', '2004-07', '2004-08',
                       '2004-09', '2004-10', '2004-11', '2004-12',
                       
                       '2005-01', '2005-02', '2005-03', '2005-04',
                       '2005-05', '2005-06', '2005-07', '2005-08',
                       '2005-09', '2005-10', '2005-11', '2005-12',
                       
                       '2006-01', '2006-02', '2006-03', '2006-04',
                       '2006-05', '2006-06', '2006-07', '2006-08',
                       '2006-09', '2006-10', '2006-11', '2006-12',
                       
                       '2007-01', '2007-02', '2007-03', '2007-04',
                       '2007-05', '2007-06', '2007-07', '2007-08',
                       '2007-09', '2007-10', '2007-11', '2007-12',
                       
                       '2008-01', '2008-02', '2008-03', '2008-04',
                       '2008-05', '2008-06', '2008-07', '2008-08',
                       '2008-09', '2008-10', '2008-11', '2008-12',
                       
                       '2009-01', '2009-02', '2009-03', '2009-04',
                       '2009-05', '2009-06', '2009-07', '2009-08',
                       '2009-09', '2009-10', '2009-11', '2009-12',
                       
                       '2010-01', '2010-02', '2010-03', '2010-04',
                       '2010-05', '2010-06', '2010-07', '2010-08',
                       '2010-09', '2010-10', '2010-11', '2010-12',
                       
                       '2011-01', '2011-02', '2011-03', '2011-04',
                       '2011-05', '2011-06', '2011-07', '2011-08',
                       '2011-09', '2011-10', '2011-11', '2011-12',
                       
                       '2012-01', '2012-02', '2012-03', '2012-04',
                       '2012-05', '2012-06', '2012-07', '2012-08',
                       '2012-09', '2012-10', '2012-11', '2012-12',
                       
                       '2013-01', '2013-02', '2013-03', '2013-04',
                       '2013-05', '2013-06', '2013-07', '2013-08',
                       '2013-09', '2013-10', '2013-11', '2013-12',
                       
                       '2014-01', '2014-02', '2014-03', '2014-04',
                       '2014-05', '2014-06', '2014-07', '2014-08',
                       '2014-09', '2014-10', '2014-11', '2014-12',
                       
                       '2015-01', '2015-02', '2015-03', '2015-04',
                       '2015-05', '2015-06', '2015-07', '2015-08',
                       '2015-09', '2015-10', '2015-11', '2015-12',
                       
                       '2016-01', '2016-02', '2016-03', '2016-04',
                       '2016-05', '2016-06', '2016-07', '2016-08']
    
    city_all_house_df = city_all_house_df[columns_to_keep]  

                         
    """
    city_all_house_df['State, RegionName'] = city_all_house_df[['State', 'RegionName']].apply(lambda x: ', '.join(x), axis=1)
    """
    
    city_all_house_df['2000q1'] = city_all_house_df[['2000-01', '2000-02', '2000-03']].mean(axis=1)
    city_all_house_df['2000q2'] = city_all_house_df[['2000-04', '2000-05', '2000-06']].mean(axis=1)
    city_all_house_df['2000q3'] = city_all_house_df[['2000-07', '2000-08', '2000-09']].mean(axis=1)
    city_all_house_df['2000q4'] = city_all_house_df[['2000-10', '2000-11', '2000-12']].mean(axis=1)
    
    city_all_house_df['2001q1'] = city_all_house_df[['2001-01', '2001-02', '2001-03']].mean(axis=1)
    city_all_house_df['2001q2'] = city_all_house_df[['2001-04', '2001-05', '2001-06']].mean(axis=1)
    city_all_house_df['2001q3'] = city_all_house_df[['2001-07', '2001-08', '2001-09']].mean(axis=1)
    city_all_house_df['2001q4'] = city_all_house_df[['2001-10', '2001-11', '2001-12']].mean(axis=1)
    
    city_all_house_df['2002q1'] = city_all_house_df[['2002-01', '2002-02', '2002-03']].mean(axis=1)
    city_all_house_df['2002q2'] = city_all_house_df[['2002-04', '2002-05', '2002-06']].mean(axis=1)
    city_all_house_df['2002q3'] = city_all_house_df[['2002-07', '2002-08', '2002-09']].mean(axis=1)
    city_all_house_df['2002q4'] = city_all_house_df[['2002-10', '2002-11', '2002-12']].mean(axis=1)
    
    city_all_house_df['2003q1'] = city_all_house_df[['2003-01', '2003-02', '2003-03']].mean(axis=1)
    city_all_house_df['2003q2'] = city_all_house_df[['2003-04', '2003-05', '2003-06']].mean(axis=1)
    city_all_house_df['2003q3'] = city_all_house_df[['2003-07', '2003-08', '2003-09']].mean(axis=1)
    city_all_house_df['2003q4'] = city_all_house_df[['2003-10', '2003-11', '2003-12']].mean(axis=1)
    
    city_all_house_df['2004q1'] = city_all_house_df[['2004-01', '2004-02', '2004-03']].mean(axis=1)
    city_all_house_df['2004q2'] = city_all_house_df[['2004-04', '2004-05', '2004-06']].mean(axis=1)
    city_all_house_df['2004q3'] = city_all_house_df[['2004-07', '2004-08', '2004-09']].mean(axis=1)
    city_all_house_df['2004q4'] = city_all_house_df[['2004-10', '2004-11', '2004-12']].mean(axis=1)
    
    city_all_house_df['2005q1'] = city_all_house_df[['2005-01', '2005-02', '2005-03']].mean(axis=1)
    city_all_house_df['2005q2'] = city_all_house_df[['2005-04', '2005-05', '2005-06']].mean(axis=1)
    city_all_house_df['2005q3'] = city_all_house_df[['2005-07', '2005-08', '2005-09']].mean(axis=1)
    city_all_house_df['2005q4'] = city_all_house_df[['2005-10', '2005-11', '2005-12']].mean(axis=1)
    
    city_all_house_df['2006q1'] = city_all_house_df[['2006-01', '2006-02', '2006-03']].mean(axis=1)
    city_all_house_df['2006q2'] = city_all_house_df[['2006-04', '2006-05', '2006-06']].mean(axis=1)
    city_all_house_df['2006q3'] = city_all_house_df[['2006-07', '2006-08', '2006-09']].mean(axis=1)
    city_all_house_df['2006q4'] = city_all_house_df[['2006-10', '2006-11', '2006-12']].mean(axis=1)
    
    city_all_house_df['2007q1'] = city_all_house_df[['2007-01', '2007-02', '2007-03']].mean(axis=1)
    city_all_house_df['2007q2'] = city_all_house_df[['2007-04', '2007-05', '2007-06']].mean(axis=1)
    city_all_house_df['2007q3'] = city_all_house_df[['2007-07', '2007-08', '2007-09']].mean(axis=1)
    city_all_house_df['2007q4'] = city_all_house_df[['2007-10', '2007-11', '2007-12']].mean(axis=1)
    
    city_all_house_df['2008q1'] = city_all_house_df[['2008-01', '2008-02', '2008-03']].mean(axis=1)
    city_all_house_df['2008q2'] = city_all_house_df[['2008-04', '2008-05', '2008-06']].mean(axis=1)
    city_all_house_df['2008q3'] = city_all_house_df[['2008-07', '2008-08', '2008-09']].mean(axis=1)
    city_all_house_df['2008q4'] = city_all_house_df[['2008-10', '2008-11', '2008-12']].mean(axis=1)
    
    city_all_house_df['2009q1'] = city_all_house_df[['2009-01', '2009-02', '2009-03']].mean(axis=1)
    city_all_house_df['2009q2'] = city_all_house_df[['2009-04', '2009-05', '2009-06']].mean(axis=1)
    city_all_house_df['2009q3'] = city_all_house_df[['2009-07', '2009-08', '2009-09']].mean(axis=1)
    city_all_house_df['2009q4'] = city_all_house_df[['2009-10', '2009-11', '2009-12']].mean(axis=1)
    
    
    
    city_all_house_df['2010q1'] = city_all_house_df[['2010-01', '2010-02', '2010-03']].mean(axis=1)
    city_all_house_df['2010q2'] = city_all_house_df[['2010-04', '2010-05', '2010-06']].mean(axis=1)
    city_all_house_df['2010q3'] = city_all_house_df[['2010-07', '2010-08', '2010-09']].mean(axis=1)
    city_all_house_df['2010q4'] = city_all_house_df[['2010-10', '2010-11', '2010-12']].mean(axis=1)
    
    city_all_house_df['2011q1'] = city_all_house_df[['2011-01', '2011-02', '2011-03']].mean(axis=1)
    city_all_house_df['2011q2'] = city_all_house_df[['2011-04', '2011-05', '2011-06']].mean(axis=1)
    city_all_house_df['2011q3'] = city_all_house_df[['2011-07', '2011-08', '2011-09']].mean(axis=1)
    city_all_house_df['2011q4'] = city_all_house_df[['2011-10', '2011-11', '2011-12']].mean(axis=1)
    
    city_all_house_df['2012q1'] = city_all_house_df[['2012-01', '2012-02', '2012-03']].mean(axis=1)
    city_all_house_df['2012q2'] = city_all_house_df[['2012-04', '2012-05', '2012-06']].mean(axis=1)
    city_all_house_df['2012q3'] = city_all_house_df[['2012-07', '2012-08', '2012-09']].mean(axis=1)
    city_all_house_df['2012q4'] = city_all_house_df[['2012-10', '2012-11', '2012-12']].mean(axis=1)
    
    city_all_house_df['2013q1'] = city_all_house_df[['2013-01', '2013-02', '2013-03']].mean(axis=1)
    city_all_house_df['2013q2'] = city_all_house_df[['2013-04', '2013-05', '2013-06']].mean(axis=1)
    city_all_house_df['2013q3'] = city_all_house_df[['2013-07', '2013-08', '2013-09']].mean(axis=1)
    city_all_house_df['2013q4'] = city_all_house_df[['2013-10', '2013-11', '2013-12']].mean(axis=1)
    
    city_all_house_df['2014q1'] = city_all_house_df[['2014-01', '2014-02', '2014-03']].mean(axis=1)
    city_all_house_df['2014q2'] = city_all_house_df[['2014-04', '2014-05', '2014-06']].mean(axis=1)
    city_all_house_df['2014q3'] = city_all_house_df[['2014-07', '2014-08', '2014-09']].mean(axis=1)
    city_all_house_df['2014q4'] = city_all_house_df[['2014-10', '2014-11', '2014-12']].mean(axis=1)
    
    city_all_house_df['2015q1'] = city_all_house_df[['2015-01', '2015-02', '2015-03']].mean(axis=1)
    city_all_house_df['2015q2'] = city_all_house_df[['2015-04', '2015-05', '2015-06']].mean(axis=1)
    city_all_house_df['2015q3'] = city_all_house_df[['2015-07', '2015-08', '2015-09']].mean(axis=1)
    city_all_house_df['2015q4'] = city_all_house_df[['2015-10', '2015-11', '2015-12']].mean(axis=1)
    
    city_all_house_df['2016q1'] = city_all_house_df[['2016-01', '2016-02', '2016-03']].mean(axis=1)
    city_all_house_df['2016q2'] = city_all_house_df[['2016-04', '2016-05', '2016-06']].mean(axis=1)
    city_all_house_df['2016q3'] = city_all_house_df[['2016-07', '2016-08']].mean(axis=1)

    columns_to_keep = ['State', 'RegionName', 
                       '2000q1', '2000q2', '2000q3', '2000q4',
                       '2001q1', '2001q2', '2001q3', '2001q4',
                       '2002q1', '2002q2', '2002q3', '2002q4',
                       '2003q1', '2003q2', '2003q3', '2003q4',
                       '2004q1', '2004q2', '2004q3', '2004q4',
                       '2005q1', '2005q2', '2005q3', '2005q4',
                       '2006q1', '2006q2', '2006q3', '2006q4',
                       '2007q1', '2007q2', '2007q3', '2007q4',
                       '2008q1', '2008q2', '2008q3', '2008q4',
                       '2009q1', '2009q2', '2009q3', '2009q4',
    
                       '2010q1', '2010q2', '2010q3', '2010q4',
                       '2011q1', '2011q2', '2011q3', '2011q4',
                       '2012q1', '2012q2', '2012q3', '2012q4',
                       '2013q1', '2013q2', '2013q3', '2013q4',
                       '2014q1', '2014q2', '2014q3', '2014q4',
                       '2015q1', '2015q2', '2015q3', '2015q4',
                       '2016q1', '2016q2', '2016q3']
                       
    city_all_house_df = city_all_house_df[columns_to_keep]                                                        
    city_all_house_df = city_all_house_df.set_index(['State', 'RegionName'])

    '''
    Code of get_list_of_university_towns.py
    '''
    with open('towns.txt', encoding='utf-8') as file:
        lines = file.readlines()
  
    university_towns = []
    for line in lines:
        if 'edit' in line:
            line = line.replace('[edit]',"")
            state = line.rstrip('\n') 
            continue
        else:
            temp =  line.split(' (', 1)[0]
            region = temp.rstrip('\n')
        university_towns.append([state,region])

    university_towns_df=pd.DataFrame(university_towns)        
    university_towns_df.columns=['State', 'RegionName']
  
    '''
    Main program begin
    '''
    university_towns_df['boolean'] = True
    university_towns_df = university_towns_df.set_index(['State', 'RegionName'])
    university_towns_HP = pd.merge(city_all_house_df, university_towns_df, how='inner', left_index=True, right_index=True)
    non_university_towns_HP = pd.merge(city_all_house_df, university_towns_df, how='outer', left_index=True, right_index=True)
    non_university_towns_HP = non_university_towns_HP[non_university_towns_HP['boolean']!=True]

    columns_to_keep = ['2008q3', '2009q2']
    university_towns_HP = university_towns_HP[columns_to_keep]  
    non_university_towns_HP = non_university_towns_HP[columns_to_keep]     

    university_towns_HP = university_towns_HP.dropna()
    non_university_towns_HP = non_university_towns_HP.dropna()      

    university_towns_HP['Price Ratio'] = university_towns_HP.loc[:, '2008q3']/university_towns_HP.loc[:, '2009q2']
    non_university_towns_HP['Price Ratio'] = non_university_towns_HP.loc[:, '2008q3']/non_university_towns_HP.loc[:, '2009q2']

    t_test_result =  stats.ttest_ind(university_towns_HP['Price Ratio'], non_university_towns_HP['Price Ratio'])

    '''
    generate answer    
    '''
    difference = False
    
    if (t_test_result[1] < 0.01):
        difference = True
    else:
        difference = False
    
    p = t_test_result[1]
    
    if (university_towns_HP['Price Ratio'].mean() < non_university_towns_HP['Price Ratio'].mean()):
        better = 'university town'
    else:
        better = 'non-university town'
    
    return (difference, p, better)