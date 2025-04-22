# Recursion is when a function calls itself repeatedly

# prints n to 1 backward
def show(n):
    # if n == 0: # 5,4,3,2,1
    if n == -1: # 5,4,3,2,1,0   
        return
    print(n)
    show(n - 1)
show(5)    

# print factorial of a number
def fact(n):
    if(n == 0 or n == 1):
        return 1
    return n * fact(n - 1)
print(fact(5))    
