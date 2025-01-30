import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Titanic = pd.read_csv("Titanic Dataset.csv")
# primt(Titanic.info())

total_passemger = Titanic.shape[0]
# primt(total_passemger)

people_survived = Titanic["Survived"].value_counts()
# print(people_survived)
# sb.countplot(x="Survived",data=Titanic)

# plt.show()


# print(round(Titanic["Age"].mean()))

# Fare = Titanic["Fare"].mean()
# print(Fare)

# plt.figure(figsize=(8,6))
# sb.countplot(data=Titanic,x="Pclass",palette=["gold","silver","brown"])
# plt.show()

youngest = Titanic["Age"].min()
oldest = Titanic["Age"].max()
print(youngest)
print(oldest)