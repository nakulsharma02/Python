class Father:
    def __init__(self):
        self.father = "father"
        print(f"I am a {self.father} class")
    def skills(self):
        print("Father's Skills:")
        print("I have skills to do office work more efficiently.")
class mother:
    def __init__(self):
        self.mother = "mother"
        print(f"I am a {self.mother} class")
    print("Mother Skills:")
    def skills(self):
        print("Mother's Skills:")
        print("I have skills to manage household tasks efficiently.")
class Child(Father, mother):
    def __init__(self, name):
        self.name = name
        print(f"My name is {self.name}")
        print("Child Skills:")
        Father.skills(self)
        mother.skills(self)
Child = Child("Rohan")
Mother = mother()
Mother.skills()
Father = Father()
Father.skills()
