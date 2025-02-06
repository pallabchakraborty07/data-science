import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


np.random.speed(42)
df = pd.DataFrame({
    "Catrgroy":np.random.choice(['A','B','c'],50),
    "score":np.random.randint(50,100,50)
})

print(df)

group_stat = df.groupby('catrgroy')["Score"].agg(['man','std','count'])

print(group_stat)