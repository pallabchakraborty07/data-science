import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
covidDF = pd.read_csv(url)

country = "India"
covid_India = covidDF[covidDF["location"]==country]

covid_India = covid_India[["date","new_cases","new_deaths"]]
covid_India["date"] = pd.to_datetime(covid_India["date"])

plt.figure(figsize=(8,6))
plt.plot(covid_India["date"],covid_India["new_cases"],label="new cases",color="red")
plt.plot(covid_India["date"],covid_India["new_deaths"],label="new deaths",color="blue")
plt.xlabel("date")
plt.ylabel("count")
plt.grid(True)
plt.legend()
plt.show()