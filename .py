class Student:


    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def static():
        print("hello")
        
    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name,"your avg score is:", sum/3)

s1 = Student("affan",[44,33,22])
s1.avg()
s1.static()
