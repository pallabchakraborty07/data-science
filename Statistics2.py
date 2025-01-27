import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

movieData = pd.read_csv("IMDB Dataset.csv")
# print(movieData.info())
# Histogram

# plt.hist(movieData["Runtime"])
# plt.xlabel("Run Time")
# plt.ylabel("Movies")

# plt.plot(movieData["Released_Year"])

movieData["IMBD_Rating"].unique()
bin_rating = np.arange(8,10,0,2)
plt.hist(movieData['IMBD_Rating'],edgcolor="black",bins=bin_rating,color="g")
plt.ylabel("count of movies")
plt.xlabel("IMBD_Rating")

plt.show()
