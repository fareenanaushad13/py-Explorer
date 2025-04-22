# Functions is a block of code that performs a specific task. It is reusable and can be called multiple times in a program.
# functions are defined using the def keyword folowed by the function name and parentheses.

def cal_sum(a,b): # function definition #parameter
    sum = a + b
    print("The sum of", a, "and", b, "is:", sum) 
    return sum #return statement
cal_sum(5,10) #function call  
cal_sum(361,361)
cal_sum(234,788) #argument

def print_hellow():
    print("hello world!")
print_hellow()

def print_hello():
    print("Hello!!!")
output = print_hello()
print(output) # None    

#calculate average of three numbers

def cal_average(a,b,c):
    sum = a+b+c
    average = sum/3
    print(average)
    return average
cal_average(34,78,45)    

#types of functions
# -->Build-in function
# --> User-defined function

# built-in function are the functions that are alrady defined in python

print("farru", end=" ") # end is used to print the next statement in the same line .. end = "\n"
print("far")

# user-defined function are the functions that are defined by the user

def add_num(x,y): 
    sum = x + y
    return sum

num1 = 10
num2 = 20
print(add_num(num1, num2))

# defalut arguments

def cal_prod(a = 10, b= 20):
    print(a * b)
    return (a * b)
cal_prod()    