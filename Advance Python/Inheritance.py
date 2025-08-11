class Human:
    def __init__(self, human):
        self.human = "human"
        print(f"I am a {self.human}, this is a {human} class")
class human1(Human):
    def __init__(self,name):
        Human.__init__("human1")
        self.name = name
        print(f"My name is {self.name}")
    def age(self, age):
        self.age = age
        print(f"My age is {self.age}")
class human2(Human):
    def __init__(self,name):
        Human.__init__("human2")   
        self.name = name
        print(f"My name is {self.name}")
    def age(self, age):
        self.age = age
        print(f"My age is {self.age}")
Human = Human("Human")
ramesh = human1("Ramesh")
ramesh.age(25)
suresh = human2("Suresh")
suresh.age(30)
# Output:
# I am a human
# My name is Ramesh
# My age is 25
# I am a human
# My name is Suresh
# My age is 30