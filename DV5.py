import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

data ={
    "X":[1,2,3,4,5],
    "Y":[4,7,9,0,5]
}

# plt.figure(figsize=(8,6))
# plt.title("my data using scatter plot")
# plt.xlabel("X-Lable")
# plt.ylabel("Y-Lable")
# plt.scatter(data["X"],data["Y"])
# plt.show()

DiamondDF = sb.load_dataset("diamonds")

# print(DiamondDF.head())

plt.figure(figsize=(8,6))
sb.scatterplot(data=DiamondDF,x="cut",y="price",color="red")
plt.title("Diamond price Traker")
plt.xlabel("cut")
plt.ylabel("price")
plt.show()