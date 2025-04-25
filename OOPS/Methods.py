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