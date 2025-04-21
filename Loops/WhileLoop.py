count = 1
while count <= 5:
    print("hello World!!")
    count += 1

i = 5
while i >= 1: 
    print(i) 
    i -= 1 
print("loop ended")

# multipplication of a number n

n = int(input("Enter a Number: "))
i = 1
while i <= 10:
    print(n*i)
    i += 1

# element of lists using loop
nums = [1,2,4,9,16,25,36,49,64,81,100] 

idx = 0
while idx < len(nums):
    print(nums[idx]) #nums[0], nums[1]
    idx += 1

# search for a number x in this tuple using loop
nums = [1,2,4,9,16,25,36,49,64,81,100] 
x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at index:", i)
    i += 1
