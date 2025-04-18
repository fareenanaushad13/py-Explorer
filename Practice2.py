#1) input user first name and print its length 
name = input("Enter Your Name:")
print("length of name is:", len(name))

#2) find the occurence of '$' in a string
str = "Hi, $iam the $symbol $99.8"
print(str.count("$"))

#3) check if the number enter by the user is even or odd
num = int(input("Enter a Number:"))

# rem = num % 2 

# if(rem == 0):
#     print("EVEN number")
# else:
#     print("ODD number")

if(num % 2 == 0):
    print("EVEN number")
else:
    print("ODD number")

#4) greatest of three umber enter by the user
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if(a >= b and a >= c):
    print("first number is greatest", a)
elif(b >= c):
    print("second number is greatest", b)
else:
    print("third number is greatest", c)

#5) check if a number is multiple of 7 or not
x = int(input("Enter a number:"))

if(x % 7 ==0):
    print("multiple of 7")
else:
    print("not a multiple of 7")



