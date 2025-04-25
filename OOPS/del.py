# del keyword- -->
# used to delete objects properties or object itself
# del s1.name

class Student:
    def __init__(self,name):
        self.name = name
s1 = Student("farrrrroo")
print(s1.name)
del s1.name
print(s1.name) 

# Private(like) Attributes and Methods ---->
# conceptual Implementation in python
# private Attributes and Methods are meant to be used only within the class and are not accessible from outside the class

class Account:
    def __init__(self,acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #private __
    def reset_pass(self):
        print(self.__acc_pass)  

acc1 = Account("12345","abcde")    
print(acc1.acc_no)   
print(acc1.reset_pass()) 

class Person:
    __name = "anonymous"
    
    def __Hello(self):
        print("hello persom!!")

    def welcome(self):
        self.__Hello()  
p1 = Person()  
print(p1.welcome())        
    
