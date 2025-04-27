# Methods are functions that belongs to objects

class Student():
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
    def welcome(self):
        print("welcome Student", self.name) 
    def get_marks(self):
        return self.marks
s1 =  Student("far", 98)
s1.welcome()
print(s1.get_marks())    

#Static Methods
# methods that do not use the self parameter(work at class level)

#Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifuing it
 
class College:
    @staticmethod #decorator
    def college():
        print("DSPMU")
College.college()

# class Method -->
# A class method is bound to the class & recieves the class as an implicit first argument
#  Note - static method cannot access or modify the class state and generally for utility
class Person:
    name = "anonymous"

    # def changeName(obj, name):
    #     sel.__class__.name = "far"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("far farru")
print(p1.name)
print(Person.name)

#Property Method
# we use @property decorator on any method int the class to use the method property 

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/ 3) + "%"

stu1 = Student(89,98,67)
print(stu1.percentage) 

stu1.phy  = 77
print(stu1.percentage)
