# class Student:
#     name = "suii"

# s1 = Student()
# print(s1.name)

class Friends:
    college_name = "anjuman"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

s1 = Friends("siuu",99)
s2 = Friends("suuii",99.6)
print(s1.name,s1.marks)
print(s2.name,s2.marks)
print(s2.college_name)