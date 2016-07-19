import pandas as pd
DF = pd.read_csv('WDI_csv/WDI_data.csv',encoding='ISO-8859-1')
DF1 = DF[DF['Country Code'] == 'UZB']
#Tried to look up unemployment percentage in Uzbekistan, found NO data available
DF1[DF1['Indicator Code']=='SL.UEM.LTRM.ZS']

#Next to look up finland

DF_fIN = DF[DF['Country Name'] == 'Finland']

#Asked my friends what they would like to know about any country
#and its economic indicators
#The one who asked for Finland gave nothing special in particular.
#So I chose the first thing I saw, and that turned out to be the
#fact that in 1960 21.1% of finland's GDP was from exports
