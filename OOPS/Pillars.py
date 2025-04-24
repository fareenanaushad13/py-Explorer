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
