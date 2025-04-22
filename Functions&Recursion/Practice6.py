# Q1) write a function to print length of a list(list is the patameter)
cities = ["Bangalore", "Delhi", "Mumbai", "Chennai", "Kolkata"]
heroes = ["Ironman", "Thor", "Hulk", "Captain America"]

def print_len(list):
    print(len(list))
print(len(cities))
print_len(heroes)   

# Q2) write a function to print a list in a single line
heroes = ["Ironman", "Thor", "Hulk", "Captain America"]

def print_list(list):
    for item in list:
        print(item, end= " ")
print_list(heroes)
print()

# Q3) wrtie a functio to print a factotrial of n( n is the parameter)
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print(fact)
cal_fact(6)    

# Q4) write a function to print a fabonacci series 
def cal_fab(n):
    a = 0
    b = 1
    print(a,b , end = " ")
    for i in range(2, n):
        c = a + b
        print(c, end = " ")
        a = b
        b = c
cal_fab(10)
print()

# Q5) write a function to convert USD to INR
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")
converter(100)    

# Recursion

# Q6) write a recursive function to calculate the sum of n natural numbers
def cal_sum(n):
    if n == 0:
        return 0
    return cal_sum(n - 1) + n
print(cal_sum(10))   

# Q7) write a recursive function to print all elements in a list
def print_list(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx]) 
    print_list(list, idx + 1) 
fruits = ["apple","banana", "pineapple", "grapes","litchi" ]
print_list(fruits)  

# Q8) write a recursive function to print prime number from 1 to n
def is_prime(n, i = 2):
    if n<= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i +1)
print(is_prime(4))