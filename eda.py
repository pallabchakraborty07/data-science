import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Titanic = pd.read_csv("Titanic Dataset.csv")
# print(Titanic.info())

# Q1. How many people Survival

# Survived = Titanic["Survived"].value_counts()
# plt.figure(figsize=(8,6))
# sb.barplot(x=Survived.index, y= Survived.values, palette=["red", "green"])
# plt.xticks ([0,1], ["Dead", "Survived"])
# plt.ylabel("Number of People")
# plt.title("Survival Counts in Titanic")
# plt.show()

# Q2. How many males and Female

# Gender = Titanic["Gender"].value_counts()
# plt.figure(figsize=(8,6))
# print(Gender.values)
# sb.barplot(x=Gender.index, y= Gender.values, palette=["red", "green"])
# plt.show()

# How many people died in 1st class

Death1=len(Titanic[(Titanic["Pclass"]==1) & (Titanic["Survived"]==0)])
Death2=len(Titanic[(Titanic["Pclass"]==2) & (Titanic["Survived"]==0)])
Death3=len(Titanic[(Titanic["Pclass"]==3) & (Titanic["Survived"]==0)])

# print(Death1,Death2,Death3)

plt.figure(figsize=(8,6))
sb.barplot(x=["1st class" , "2nd class" , "3rd class"] , y=[23,19,86],palette=["blue","red"])
plt.show()