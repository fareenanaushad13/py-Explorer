# Constructor---->
# __init__ function --->
# all classes have a function called __init__(), which is always executed when the class is being initiated
# The self parameter is a reference to the current instance of the class,and is used to access a variable that belongs to the class

#default constructor
class Student():
    def __init__(self):
        pass


    name = "far"
    def __init__(self):
        print("adding a new student in a database....")
s1 = Student()  

#parametirized constructor
class Student:
    def __init__(self, fullname,marks):
        self.name = fullname
        self.marks = marks
s1 = Student("farru",97)
print(s1.name,s1.marks) 
  

s2 = Student("far",99)
print(s2.name,s1.marks)