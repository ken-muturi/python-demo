#@title
import os
import pandas as pd
# import plotly.express as px
import matplotlib.pyplot as plt
os.environ['MPLCONFIGDIR'] = "/tmp/gitlist"


fmp = pd.read_csv("https://data.humdata.org/dataset/7fb6fbc6-69b7-4b90-ace1-ca04dc6d53ac/resource/2763cb1e-0410-42ad-a918-bd6a99e325db/download/wfp_food_median_prices_south-africa.csv")
fmp = fmp.drop(fmp.index[0])
fmp.index = pd.to_datetime(fmp['date'])
fmp['price'] = fmp['price'].apply(pd.to_numeric)

#@title

plt.rcParams['figure.figsize'] = [15, 8]

fmpitem = pd.pivot_table(fmp, index=fmp.index, columns='cmname', values='price')
fmpitem.plot(title="WFP food median prices: South Africa");
