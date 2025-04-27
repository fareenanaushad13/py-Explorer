# Q1) Define a circle class to create a circle with radius r using the constructor. Define an Area() method of the class which calculates the area of the circle .Define perimeter() method of the class which allow you to create the perimeter of the circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7)  * self.radius

c1 = Circle(3)
print(c1.area())
print(c1.perimeter())  

#Q2)
class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role = " + self.role)
        print("dept = " + self.dept)
        print("salary = " + self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

Engg1= Engineer("Elon", 60)
Engg1.showDetails()   

#Q3)
class Order:
    def __init__(self,item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price> ord2.price

ord1 = Order("Coldrink", 40)
ord2 = Order("Biryani", 300)  

print(ord1 > ord2)

