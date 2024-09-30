#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 11:53:48 2024

@author: magironza
"""

import pandas as pd
#from datetime import *
#import matplotlib.pyplot as plt
#import seaborn as sns
#matplotlib inline

Jan2023 = pd.read_csv("/Users/stephaniecardona/Documents/ALEJANDRO/Google_Capstone/Divvy_Tripdata/2023_01.csv")
Feb2023 = pd.read_csv("/Users/stephaniecardona/Documents/ALEJANDRO/Google_Capstone/Divvy_Tripdata/2023_02.csv")
Mar2023 = pd.read_csv("/Users/stephaniecardona/Documents/ALEJANDRO/Google_Capstone/Divvy_Tripdata/2023_03.csv")
Apr2023 = pd.read_csv("/Users/stephaniecardona/Documents/ALEJANDRO/Google_Capstone/Divvy_Tripdata/2023_04.csv")
May2023 = pd.read_csv("/Users/stephaniecardona/Documents/ALEJANDRO/Google_Capstone/Divvy_Tripdata/2023_05.csv")
Jun2023 = pd.read_csv("/Users/stephaniecardona/Documents/ALEJANDRO/Google_Capstone/Divvy_Tripdata/2023_06.csv")
Jul2023 = pd.read_csv("/Users/stephaniecardona/Documents/ALEJANDRO/Google_Capstone/Divvy_Tripdata/2023_07.csv")
Aug2023 = pd.read_csv("/Users/stephaniecardona/Documents/ALEJANDRO/Google_Capstone/Divvy_Tripdata/2023_08.csv")
Sep2023 = pd.read_csv("/Users/stephaniecardona/Documents/ALEJANDRO/Google_Capstone/Divvy_Tripdata/2023_09.csv")
Oct2023 = pd.read_csv("/Users/stephaniecardona/Documents/ALEJANDRO/Google_Capstone/Divvy_Tripdata/2023_10.csv")
#Nov2023 = pd.read_csv("/Users/stephaniecardona/Documents/ALEJANDRO/Google_Capstone/Divvy_Tripdata/2023_11.csv")
#Dec2023 = pd.read_csv("/Users/stephaniecardona/Documents/ALEJANDRO/Google_Capstone/Divvy_Tripdata/2023_12.csv")


#Checking if we read the information 
"""
print(Jan2023.columns)
print(Feb2023.columns)
print(Mar2023.columns)

print(Apr2023.columns)
print(May2023.columns)
print(Jun2023.columns)

"""

#Checked that all the data had the same columns and it was true for all
""" 

df = pd.DataFrame([Jan2023.columns, Feb2023.columns, Mar2023.columns, Apr2023.columns,
	May2023.columns, Jun2023.columns, Jul2023.columns, Aug2023.columns, Sep2023.columns,
	Oct2023.columns, Nov2023.columns, Dec2023.columns])
print(df.all(axis='columns'))

"""


new_data = pd.concat([Jan2023, Feb2023, Mar2023, 
                      Apr2023, May2023, Jun2023, \
					  Jul2023, Aug2023, Sep2023, Oct2023])
                      #Nov2023, Dec2023], axis=0)

#print(new_data['ended_at'].head(5))    

new_data['ended_at'] = pd.to_datetime(new_data['ended_at'], infer_datetime_format= True)
new_data['started_at'] = pd.to_datetime(new_data['started_at'], infer_datetime_format= True)


#print(new_data.describe())


new_data.columns = ['RideId', 'RideableType', 'StartedAt', 'EndedAt', 'StartStationName',
                    'StartStationId', 'EndStationName', 'EndStationId', 'StartLat', 
                    'StartLng', 'endLat', 'EndLng', 'MemberCasual']



#new_data['Month'] = new_data['EndedAt'].dt.strftime('%m')
#new_data['Day'] = new_data['EndedAt'].dt.strftime('%d')



#new_data.MemberCasual = new_data.MemberCasual.astype('category')
#new_data.Month = new_data.Month.astype('category')
#new_data.Day = new_data.Day.astype('category')
#new_data.info()

#print(new_data['Month'].tail(5))

#new_data['TimeTravel'] = new_data.EndedAt - new_data.StartedAt
#new_data.TimeTravel = new_data.TimeTravel.astype('integer')
#print(new_data.head(10))


#print(new_data.groupby(['MemberCasual']).count())
#print(new_data.describe())
new_data.info()

new_data.to_csv('file1.csv', index=False)

#vis1 = sns.distplot(new_data['Month'], bins=10)
#vis2 = sns.boxplot(data=new_data, x='Month', y='MemberCasual')


"""print(new_data.columns)
print(new_data.info)
print(len(new_data))
"""





