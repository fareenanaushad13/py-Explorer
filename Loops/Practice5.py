# Q1) print number from 1 to 100

for i in range(1,101):
    print(i)

# Q2) print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)    

# Q3) print a multiliacation of a number n

n = int(input("Enter a number:"))

for i in range(1,11):
    print(n,"*",i,"=", n*i)

# Q4) find the sum of first n numbers (using while)

n = 6
sum = 0
i = 1
while i<= n:
    sum += i
    i += 1

print("total sum:", sum)    

# @5) find the factorial of first n numbers (using for)

# n = 6
# fact = 1
# i = 1
# while i<= n:
#     fact *= i
#     i += 1
# print("Factorial of",n, "is", fact)    

n = 6
fact = 1

for i in range(1, n+1):
    fact = fact * i
print("Factorial of",n, "is", fact) 