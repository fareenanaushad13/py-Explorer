#Q1) create a student class that takes names and marks of three subjects as arguments in constructor.Then create a method to print an average
class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your average your is:",sum/3)
s1 = Student("far",[99,98,97])
s1.get_avg()  

#Q2) create Account class with two attributes-- balance and account no.Create a method for debit, credit and printing the balance
class Account:
    def __init__(self,bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount, "was debited") 
        print("total balance=", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount, "was credited") 
        print("total balance=", self.get_balance())  

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(700)
acc1.credit(40000)
acc1.debit(10000)
