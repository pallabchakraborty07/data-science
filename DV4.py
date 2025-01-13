import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# date = [10,20,20,30,40,50,60,70,80,90]

# plt.hist(date,color="red")
# plt.title("histogram")
# plt.show()

Blood_Sugar_Men = [120,110,135, 125, 111, 112,115,111,135,125,111,112] #12 Value
Blood_Sugar_WoMen = [90,95,98, 100, 105,78,88,90,80,99,100,110]

type = [Blood_Sugar_Men,Blood_Sugar_Women]
color = ['r','g']
label = ["Men", "Women"]
bins = [70,80,90, 100, 110, 120, 130, 140, 150]

plt.xlabel("Blood Sugar Range")
plt.ylabel("Total Number of Patient")
plt.hist (type,bins-bins, color-color, width=0.95,label=label,)

plt.show()