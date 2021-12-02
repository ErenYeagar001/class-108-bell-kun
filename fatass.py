import pandas as pd
import plotly.figure_factory as ff
import csv


data_file = pd.read_csv("data.csv")
fig = ff.create_distplot([data_file["Weight(Pounds)"].tolist()],["Weight"], show_hist=True)
fig.show()

