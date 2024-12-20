import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

WeatherDF = pd.read_csv("weatherHistory.csv")
WeatherDF ["Formatted Date"] = pd.to_datetime(WeatherDF ["Formatted Date"], utc=True)
sb.set_theme(style="darkgrid", palette="muted")

#Data Visualization 1
plt.figure(figsize=(14,8))
WeatherDF["Hour"] = WeatherDF ["Formatted Date"].dt.hour
WeatherDF ["Day"] = WeatherDF ["Formatted Date"].dt.day

heatmap_data = WeatherDF.pivot_table(index="Hour", columns="Day", aggfunc='mean', values="Temperature (C)")
sb.heatmap(heatmap_data,cmap="coolwarm",linewidths=0.5)

plt.title("Hourly Temparature Heatmap")
plt.xlabel("Day")
plt.ylabel("Hour of the Day")
plt.tight_layout()
plt.show()

#Data Visualization 2
plt.figure(figsize=(14,8))
sb.scatterplot(data=WeatherDF, x="Temperature (C)",y="Humidity", alpha=0.6,color="purple")
plt.title("Hourly Temparature Heatmap")
plt.xlabel("Day")
plt.ylabel("Hour of the Day")
plt.tight_layout()
plt.show()