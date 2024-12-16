import matplotilb
import matplotlib.pyplot as plt
import numpy as np

# XPoint = np.array([0,2,6,9,17,23])
# YPoint = np.array([0,5,9,15,21,26])

# plt.plot(XPoint,marker= "o",ms=10,mec="r")
# plt.plot(YPoint,marker= "o",ms=10,mec="g")
# plt.show()


names = np.array(["sumon", "Rahul", "Omor", "Pallab", "rohit"])
marks = np.array([80,85,93,95,89])

plt.plot(names, marks, marker='o', mec='g',ms=5)

plt.title("Student Name vs Marks")
plt.xlabel("student Names")
plt.ylabel("Student Marks")
plt.show()