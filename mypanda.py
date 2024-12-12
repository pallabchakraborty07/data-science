import pandas as pd

carsDS = {

   "Name": ["BMW","Audi" , "Mercedes", "RR", "Toyota", "Thar", "Safari"], 
   "Price":[6,9,8,37,9,3,6]

}

carDF = pd.DataFrame(carsDS,index=["car1","car2","car3","car4","car5","car6","car7"])

print(carDF)

print(carDF["Name"])
print(carDF["Price"])

carDF["color"] = ["white","red","blue","black","gray","red","black"]
mycar = carDF[carDF["Price"]<=8]
print(mycar)
print(carDF)

print(carDF.info())

import pandas as pd

mymovies = pd.read_csv('Movies.csv')

print(mymovies.info())