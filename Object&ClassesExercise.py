class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name
emp1 = Employee(1, "coder")
print(emp1.id)  # Output: 1
print(emp1.name)  # Output: coder
emp2 = Employee(2, "coder1")
print(emp2.id)
print(emp2.name)  # Output: coder1
emp2.country = "India"
print(emp2.country)  # Output: India
emp1.country = "USA"
print(emp1.country)  # Output: AttributeError: 'Employee' object has no attribute 'country'
del emp1.id # Output: AttributeError: 'Employee' object has no attribute 'id'
del emp1
print(emp1.name)  # Output: NameError: name 'emp1' is not defined
