import matplotlib.pyplot as plt
import numpy as np

# year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]

# emp_rate = [2.3,4.5,6.7,1.4,4.5,9.0,8.1,0.1,9.9,0.5,9.1]


# plt.plot(year, emp_rate,color="red",marker="o")
# plt.title("Employment Ratio Per Year")
# plt.xlabel("Year")
# plt.ylabel("Employment Ratio")
# plt.grid(True)
# plt.show()

year = [2000, 2001, 2002, 2003, 2004, 2005]

oil_price = [55,65,75,85,95,105]

Economy = [2.3,3.4,5.6,1.4,6.7,7.6]


plt.plot(oil_price, year, color='green')
plt.plot(oil_price, Economy,color='blue')
plt.show()
