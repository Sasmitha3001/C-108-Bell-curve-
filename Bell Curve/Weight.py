import pandas as pd
import plotly.figure_factory as ff

data=pd.read_csv('data.csv')
figure=ff.create_distplot([data['Weight(Pounds)']],["Weight of 18 year olds"],show_hist=False)
figure.show()
