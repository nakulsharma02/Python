import matplotlib.pyplot as plt
import pandas as pd
# x = [10,20,30]
# y = [1000,2000,3000]
# plt.plot(x,y)# (10,1000),(20,2000),(30,3000)
# plt.grid()
# plt.show()
df = pd.DataFrame({
    "Name": ["Nakul","User1","User2","User3","User4","User5"],
    "Age": [23,34,22,33,45,27],
    "Salary" : [25000,45000,40000,56000,50000,560000]
})
print(df)
# plt.plot(df["Name"],df["Salary"],color='Yellow',marker="o",linestyle="--",linewidth=2)
# plt.hist(df["Salary"],bins=4)
# plt.boxplot(df["Salary"])
# plt.grid()
# plt.show()
df["Dept"]=["HR","HR","IT","IT","IT","Director"]
print(df)
count = pd.value_counts(df["Dept"])
# print(count)
# plt.pie(count,labels= count.index,autopct="%1.3f",explode=[0,0.2,0.2])
# plt.axis("equal")
# plt.show()

# Count Plot 
# plt.bar(count.index,count,color=["Purple","Yellow","Green"])
# plt.show()

# Univariate Analysis = for single column data
# Bivariate Analysis = for two columns

# for numerical-numerical column : Scatter Plot
# df["Age"] = [23,34,56,34,23,22]
# plt.scatter(df["Age"],df["Salary"],color="Orange",label="Age vs Salary")
# plt.xlabel("Age")
# plt.ylabel("Salary")
# plt.grid(True) 
# plt.show()

# Box Plot
# It is useful for showing outliers
# hr_sal = df[df["Dept"]=="HR"]["Salary"]
# it_sal = df[df["Dept"]=="IT"]["Salary"]
# dir_sal = df[df["Dept"]=="Director"]["Salary"]
# plt.boxplot([hr_sal,it_sal,dir_sal],labels=['HR','IT','Director'])
# plt.show()

# Pie Chart
salary_by_dept = df.groupby("Dept")["Salary"].sum()
print(salary_by_dept)
# plt.pie(salary_by_dept,labels=salary_by_dept.index,autopct="%1.2f")
# plt.show()

# Multivariate Analysis : 3 numerical columns
df["Experience"] = [1,2,1.5,3,3.5,2]
# Bubble plot
plt.scatter(df['Age'],df['Salary'],s=df["Experience"]*20,color="orange")
plt.show()

# Two Numerical and one categorical Column
