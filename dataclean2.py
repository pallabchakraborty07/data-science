import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# CountryData = pd.read_csv("country_vaccinations.csv")

# VaccineDF = pd.DataFrame(CountryData)

# print(VaccineDF.dropna(how="all"))
# VaccineDF.fillna(0)

EmpDS ={

'name': ["Adib", "Adib", "Rahul"],

'ID': [000,000,110]

}

EmpDF = pd.DataFrame (EmpDS)

EmpDF.drop_duplicates(inplace=True)


print(EmpDF)