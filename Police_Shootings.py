#Using data from washington post shooting report since Jan 2015

import pandas as pd
import bokeh.charts
Shootings = pd.read_csv('data-police-shootings-master/fatal-police-shootings-data.csv')

AA_Deaths = Shootings[Shootings['race'] == 'B']
percent_AA_deaths = len(AA_Deaths.index)/len(Shootings.index)
#Percent comes out to about 25%
#Next, an interested political science friend asked for race and shooting combination

States_only = AA_Deaths['state']
#Bar chart of stats vs African Americans killed
AA_bar = bokeh.charts.Bar(States_only,label='state',values='state',agg='count',title = "African American Deaths per State since 2015",legend=False)

#Bar chart of states vs Caucasians Killed
White_Shootings = Shootings[Shootings['race']=='W']
White_States_Only = White_Shootings['state']

W_bar = bokeh.charts.Bar(White_States_Only,label='state',values='state',agg='count',title="White Shooting Deaths by State",legend=False)
W_bar.height=700
W_bar.width=800

