import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb

IceCreamData = {
"flavor":["chocolate","vanila","stawberry","mint"],
"votes":[40,20,30,10]
}

IceCreamDF = pd.DataFrame(IceCreamData)

# barplot
plt.figure(figsize=(8,5))
sb.barplot(x="flavor", y="votes", data=IceCreamDF, palette="bright")
plt.xlabel("flavor")
plt.ylabel("votes")
plt.title("IceCream Data")
plt.show()

# linear plot
plt.figure(figsize=(8,5))
sb.lineplot(data=IceCreamDF,x="flavor",y="votes")
plt.xlabel("flavor")
plt.ylabel("votes")
plt.title("IceCream Data")
plt.show()

# pie plot
plt.figure(figsize=(8,5))
plt.pie(IceCreamDF["votes"], labels=IceCreamDF["flavor"], autopct='%1.1f%%',colors=sb.color_palette("bright"))
plt.xlabel("flavor")
plt.ylabel("votes")
plt.title("IceCream Data")
plt.show()