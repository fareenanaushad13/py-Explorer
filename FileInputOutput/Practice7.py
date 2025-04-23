# with open("FileInputOutput/practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/O/n")
#     f.write("using java\ni like programming in java.") 

#Q2)  replace all occurences java with python in above file
# with open("FileInputOutput/practice.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("java", "Python")
# print(new_data)

# with open("FileInputOutput/practice.txt", "w") as f:
#     f.write(new_data)

#Q3) search if the learning exist in the file or not
def check_for_word():
    word = "learning"
    with open("FileInputOutput/practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not Found")    
check_for_word()

#Q4) find in which of the line of the file does the word "learning" occur at first.ptint -1 if word not found
def check_for_line():
    word = "programming"
    data = True
    line_no = 1
    with open("FileInputOutput/practice.txt", "r") as f:
        while(data):
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
        return -1 
check_for_line() 

# Q4) from a file containing number separated by comma, print the count of even numbers
count = 0
with open("FileInputOutput/practicee.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) %2 == 0):
            count += 1
print(count)        