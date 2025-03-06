import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

num_sample = 500
sample_size = 5

avg = []

for value in range(num_sample):
    sample = np.random.randint(1,6,sample_size)
    avg.append(np.mean(sample)) 

plt.hist(avg,bins=25,color="skyblue",density=True)
plt.xlabel("sample mean")
plt.ylabel("frequence")
plt.title("CLT of sample size 500")
plt.show()