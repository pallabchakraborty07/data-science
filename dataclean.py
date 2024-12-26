import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


EmployeeData = {
"ID": [1,2,3,4,5,6,6],
"Name": ["Adib", "Pallab", "Omor", "Rahul", np.nan, "Sourav", np.nan], 
"Salary":[np.nan, "20000", np.nan, "30000","40000", "60000", "80000"],
"Age": [20,np.nan,24,25,35,27,29],
}

EmpDF = pd.DataFrame (EmployeeData)

# print("Original DataFrame")
# print(EmpDF)

EmpDF ["Name"] = EmpDF["Name"].fillna("Unknown")
# print(EmpDF)

avg_age = EmpDF['Age'].mean()
EmpDF['Age']=EmpDF["Age"].fillna(avg_age)

EmpDF["Age"]= abs(EmpDF["Age"])
# print(EmpDF)

EmpDF["Salary"]=pd.to_numeric(EmpDF["Salary"])
EmpDF['Salary'] = np.nan_to_num(EmpDF["Salary"])
avg_salary = EmpDF["Salary"].mean()
EmpDF['Salary'] = EmpDF ["Salary"].fillna(avg_salary)
print(EmpDF)
