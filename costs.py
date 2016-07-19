import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import bokeh.charts
Expend = pd.read_csv('Neighborhood_Council_Expenditures_for_Fiscal_Year_2014.csv', converters={'Expenditure': lambda s: s.replace('$','')})
names = pd.unique(Expend['Neighborhood Council'])
costs = []
print(Expend['Expenditure'])
Expend['Expenditure']= Expend['Expenditure'].apply(pd.to_numeric)
for name in names:
	costs.append((name,Expend.loc[Expend['Neighborhood Council'] == name, 'Expenditure'].sum()))

councils = list(zip(*costs))[0]
total_costs = list(zip(*costs))[1]
to_plot = pd.DataFrame({'x':councils,'y':total_costs})

to_plot = to_plot. dropna(axis = 0, how='any')

Bar_costs = bokeh.charts.Bar(to_plot,'x',values='y',title = "Council Costs")

