veggies = ["carrot", "broccoli","spinach","potato", "brinjal"]

for val in veggies:
    print(val)

str = "farru"

for char in str:
    print(char)

# for loop with else
str = "farru"
for char in str:
    if(char == "f"):
        print("Found f")
        break
    print(char)  
else:
        print("END")  

# search for a number in a tuple using loop
nums = (1,4,6,7,8,9,3,6,1,3)
x = 3
idx = 0
for el in nums:
    if el == x:
        print("fount at index", idx)
        break
    idx += 1 


# range function # range(start, stop, step)
for i in range(10): #range(stop)
    print(i)  

for i in range(2,10):  #range(start, stop)
    print(i) 

for i in range(2,10,2):  #range(start, stop, step) --> 2,4,6,8-->step of 2
    print(i)    

#Pass --> pass ia a null statemenr, used to to indicate that nothing is to be done

for i in range(5):
    pass
print("some useful work")    