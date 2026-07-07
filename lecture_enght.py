class Student:
    name = "chetan"
    def __init__(self):
        print(self)
        print("adding new student in  databbase")
        
    
    
s1 = Student()
print(s1.name)
print(s1)

s2 = Student()
print(s2.name)

class car:
    color = "blue"
    brand = "mercedes"
    
s6 = car()
print(s6.color)
print(s6.brand)

class Studen:
    college_name = "abc"
    #default constructor
    def __init__(self):
        pass
    
    #parameterized constructor
    def __init__(self, fullname, maarks):
        self.name = fullname
        self.marks = maarks
        print("adding new student in  databbase")

s7 = Studen("chetan singh", 85  )
print(s7.name, s7.marks)    

s1 = Studen("arjun", 94)
print(s1.name, s1.marks)

s9 = Studen.college_name
print(s9)

    

