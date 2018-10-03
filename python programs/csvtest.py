import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#b1 = pd.read_csv(r'C:\Users\SDC\Downloads\data\bikes.csv')

fixed_df = pd.read_csv(r'C:\Users\SDC\Downloads\data\bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')

#b2 = pd.read_csv(r'C:\Users\SDC\Downloads\data\weather_2012.csv', encoding='latin1', dayfirst=True,)

#print(fixed_df.index)
#print(fixed_df.index.day)
#print(fixed_df.index.weekday)

fixed_df.loc[:,'weekday'] = fixed_df.index.weekday
weekday_counts = fixed_df.groupby('weekday').aggregate(sum)
print(weekday_counts)

#berri_bikes = fixed_df[['Berri 1','Maisonneuve 1']].copy()
#print(berri_bikes[:5])
#print(fixed_df[:3])
#print(fixed_df['Berri 1'])
#print(fixed_df['Berri 1'].value_counts())
#print(fixed_df[['Berri 1','Maisonneuve 1','du Parc']][:5])
#plt.show(fixed_df['Berri 1'][3:10].plot(kind='bar'))
#plt.show(fixed_df[3:10].plot(kind='bar'))
#plt.show(fixed_df.plot(kind='bar'))
#plt.show(fixed_df.plot())

#plt.show(b2.plot())
#print(pd.Series([2, 3, 4]))
#print(np.array([[1,2,3],[2,3,4],[3,4,5]]))

