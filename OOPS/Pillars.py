# ABSTRACTION---->
# Hiding the implementation details of a class and only showing the essential features to the user
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("car Started!!") 
car1 = Car()
car1.start()           

# ENCAPSULATION--->
# Wrapping data and functions in a single unit(Object)
class Student:
    def __init__(self, name, age):
        self.name = name   
        self.age = age    

 
    def get_name(self):
        return self.name

 
    def get_age(self):
        return self.age

    def set_age(self, age):
        if age > 0:
            self.age = age
        else:
            print("Invalid age")

s1 = Student("farru", 20)

print(s1.get_name())  # farru
print(s1.get_age())   # 20

s1.set_age(21)        # Update age
print(s1.get_age())   # 21

s1.set_age(-5)        # Invalid age

# Inheritance -->
# when one class(Child or derived) drives the properties and methods of another class(parent/base)

#Single Inheritance
class Car:
    @staticmethod
    def start():
        print("car started!!")

    @staticmethod
    def stop():
        print("car stopped!!")  
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name   

Car1 =  ToyotaCar("fortuner") 
Car2 = ToyotaCar("prius")  

print(Car1.start())

#Multi-Level Inheritance
class Car:
    @staticmethod
    def start():
        print("car started!!")

    @staticmethod
    def stop():
        print("car stopped!!")  
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand 

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type 

Car1 = Fortuner("Diesel")
car1.start()

#Multiple Inheritance
class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B" 

class C(A,B):
    varC = "Welcome to class C" 

c1 = C()   
print(c1.varC)
print(c1.varB)
print(c1.varB)   

#Super Method---->
# super method is used to access methods from the parent class
class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car started!!")      

    @staticmethod
    def stop():
        print("car stopped!!")

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("prius","electric")
print(car1.type) 



