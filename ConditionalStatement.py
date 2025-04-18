# if-elif-else(syntax)

light = "green"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")    

print("end of code")  

age = 22
if(age >= 18):
    print("can vote") #indentation --> spaces of 4
else:
    print("cannot vote")

#marks
marks = int(input("Enter marks of student:"))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"
print("grade of the student->", grade)

#nesting
age = 34

if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")        