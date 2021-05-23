import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.style.use('ggplot')
import seaborn as sns
pa_df=pd.read_csv('Port_Authority_ridership_3_2021.csv') #read in Port Authority data as csv file
pa_df1=pa_df.drop('ridership_route_code',axis=1) #drop 'ridership_route_code' column as it is a repeat
pa_df2=pa_df1.loc[pa_df1.loc[:,'route']!='MNT1',:] #drop rows with bus routes labeled 'MNT1' as data is sparse and sporadic, could #be incorrect
pa_df2_b=pa_df2.loc[pa_df2.loc[:,'mode']=='Bus',:] #select Bus data
pa_df2_b_wk=pa_df2_b.loc[pa_df2_b.loc[:,'day_type']=='WEEKDAY',:]#select day_type as 'Weekday' to create week day ridership #table
#pa_df2_b_wk_1=pa_df2_b_wk.loc[pa_df2_b_wk.loc[:,'route']=='1',:] #select data for bus route 1
#srs_b_wk_1=pa_df2_b_wk_1.set_index('year_month').loc[:,'avg_riders'] #extract 'avg_riders' column as a series and set its index #as #'year_month'
#srs_b_wk_1.index=pd.Series(list(map(lambda x: str(x), srs_b_wk_1.index))) #convert index to a string series vector
#srs_b_wk_1.plot.line(y='avg_riders') #plot average ridership over time for bus 1

tmp20=pa_df2_b_wk
tmp20 = tmp20.loc[tmp20.loc[:,'route']!='68',:]# remove bus route 68 as it has only 30 weeks data
tmp20 = tmp20.loc[tmp20.loc[:,'route']!='78',:]# remove bus route 78 as it has only 9 weeks data
tmp21 = pd.DataFrame()
for i in sorted(set(tmp20['route'])): # this for loop creates a table of 'avg_riders' columns, one for each bus route
    add_df=tmp20.loc[tmp20.loc[:,'route']==i,:]
    add_srs=add_df.set_index('year_month').loc[:,'avg_riders']# the index of the table is set as the column 'year_month'
    tmp21=pd.concat([tmp21,add_srs],axis=1)
tmp21.columns=sorted(set(tmp20['route']))
tmp21.index=pd.Series(list(map(lambda x: str(x), tmp21.index)))# the index is coverted to a string to make it equally spaced
tmp21.plot.line(y='61D') # for graphing

tmp31 = pd.DataFrame()
tmp32 = pd.DataFrame()
for i in tmp21.columns: #this for loop calculates percentage changes in the 'avg_riders' column across time using the average
    col_ave=np.mean(tmp21.loc['201901':'201912',i]) # of the values in 2019 as the baseline
    diff = tmp21.loc[:,i]-col_ave
    pc_diff=round(diff/col_ave*100,1)
    tmp31=pd.concat([tmp31,diff],axis=1)
    tmp32=pd.concat([tmp32,pc_diff],axis=1)

tmp31.columns=tmp21.columns
tmp31.index=tmp21.index
tmp32.columns=tmp21.columns
tmp32.index=tmp21.index
