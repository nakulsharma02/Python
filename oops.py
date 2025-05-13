#class is a blueprint of creating object
#object is used to solve problem statement
# class Employee:
# #class Attribute
#     language="Py"
#     salary=12000
#     def getInfo(self):#methods
#         print(f'The language is {self.language},The salary is {self.salary}')
#     def greet(self):
#         print("Good Morning!")
# #object     
# run = Employee()
# run.name="Rohan"#Instance Attribute:takes preference ovver class attributes
# run.language='Javascript'
# print(run.language,run.salary,run.name)
# run.greet()
# run.getInfo()
# class Table:
#     n=int(input("enter the value of n"))
#     def table(n):#method of class
#         for i in range(1,11):
#             print(f'{n}X{i}={i*n}')
#     table(n)
#static method does not need an any argument and does not need an object property
# class Employee:
# #class Attribute
#     language="Py"
#     salary=12000
#     def getInfo(self):#methods
#         print(f'The language is {self.language},The salary is {self.salary}')
#     @staticmethod
#     def greet():
#         print("Good Morning!")
# #object     
# run = Employee()
# run.name="Rohan"#Instance Attribute
# run.language='Javascript'
# print(run.language,run.salary,run.name)
# run.greet()
# run.getInfo()
#__init__(self)=It is a constructor,dunder method which is automatically called when an object is created
# class Employee:
# #class Attribute
#     language="Py"
#     salary=12000
#     def __init__(self):
#         print("I am creating an Object")
#     def getInfo(self):#methods
#         print(f'The language is {self.language},The salary is {self.salary}')
    # @staticmethod
    # def greet():
    #     print("Good Morning!")
# #object     
# run = Employee()
# run.name="Rohan"#Instance Attribute
# run.language='Javascript'
# print(run.language,run.salary,run.name)
# run.greet()
# run.getInfo()