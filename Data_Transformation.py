import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# A = [10,20,30,40,50,60,70]
# B = [value+10 for value in A]

# print(B) 

arr = np.array([1,2,3,4,5,6])
df = pd.DataFrame(arr)

def add1(list):
    new = []
    for item in list:
        new.append(item+1)
    return new

df["sqrt_Transformed"] = np.sqrt(arr)
df["Add One"] = add1(arr)

print(df)