class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def ShowDetails(self):
        print(f"work is {self.role} and department is {self.dept} and salary will be {self.salary}")

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("accountant","finance", 60000)
e1 = Engineer("Affan",20)
e1.ShowDetails()