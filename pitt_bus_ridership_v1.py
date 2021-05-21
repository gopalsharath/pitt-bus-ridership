import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.style.use('ggplot')
pa_df=pd.read_csv('Port_Authority_ridership_3_2021.csv') #read in Port Authority data as csv file
pa_df1=pa_df.drop('ridership_route_code',axis=1) #drop 'ridership_route_code' column as it is a repeat
pa_df2=pa_df1.loc[pa_df1.loc[:,'route']!='MNT1',:] #drop rows with bus routes labeled 'MNT1' as data is sparse and sporadic, could #be incorrect
pa_df2_b=pa_df2.loc[pa_df2.loc[:,'mode']=='Bus',:] #select Bus data
pa_df2_b_wk=pa_df2_b.loc[pa_df2_b.loc[:,'day_type']=='WEEKDAY',:]#select day_type as 'Weekday' to create week day ridership table
pa_df2_b_wk_1=pa_df2_b_wk.loc[pa_df2_b_wk.loc[:,'route']=='1',:] #select data for bus route 1
srs_b_wk_1=pa_df2_b_wk_1.set_index('year_month').loc[:,'avg_riders'] #extract 'avg_riders' column as a series and set its index as #'year_month'
srs_b_wk_1.index=pd.Series(list(map(lambda x: str(x), srs_b_wk_1.index))) #convert index to a string series vector
srs_b_wk_1.plot.line(y='avg_riders') #plot average ridership over time for bus 1

tmp20=pa_df2_b_wk
tmp20 = tmp20.loc[tmp20.loc[:,'route']!='68',:]
tmp20 = tmp20.loc[tmp20.loc[:,'route']!='78',:]
tmp21 = pd.DataFrame()
for i in sorted(set(tmp20['route'])):
    add_df=tmp20.loc[tmp20.loc[:,'route']==i,:]
    add_srs=add_df.set_index('year_month').loc[:,'avg_riders']
    tmp21=pd.concat([tmp21,add_srs],axis=1)
tmp21.columns=sorted(set(tmp20['route']))
tmp21.index=pd.Series(list(map(lambda x: str(x), tmp21.index)))
tmp21.plot.line(y='61D')