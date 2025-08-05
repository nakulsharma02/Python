class ClassesAndObjects:
    def __init__(self, name, age): # Constructor
        self.name = name # Class Attributes
        self.age = age
    def studentsMarks (self, marks): # Method to set marks
        self.marks = marks 
        return f"Student {self.name} has marks {self.marks}."
    def greet(self):
        return f"Hello, Students name is {self.name} and I am {self.age} years old."
Ram = ClassesAndObjects("Ram", 20)
marks = Ram.studentsMarks(90)
Ram.father = "Ramesh"# Adding a new attribute to the instance
print(f'Ram"s father is {Ram.father}')  # Accessing the new attribute
print(Ram.greet())
print(marks)
Shyam = ClassesAndObjects("Shyam", 22)
marks = Shyam.studentsMarks(85)
print(Shyam.greet())
print(marks)