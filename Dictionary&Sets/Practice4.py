# Q1)  store folllowing word meaning in python
 #table: "a piece of furniture", "lists of facts & figures"
 # cat : "a small animal"

dictionary = {
    "cat": "a small animal",
    "table": ["a piece of furniture", "lists of facts & figures"]
 }
print(dictionary)

# Q2) you r given a list of subjects for students, Assume one classroom is required for 1 subject. How many classrooms are needed for all subjects
subject = { 
    "python" , "java", "c++", "python", "java","c","javascript",
    "python", "java","c++", "c#"
}
print(subject)
print(len(subject))

# Q3) WAP to enter a marks of three sunjects from the user ans srore them in a dictionary. Start with an empty dictionary & add one by one.Use sunject name as key and marks as value
marks = {}

x = int(input("Enter phy: "))
marks.update({"phy": x})

x = int(input("Enter cs: "))
marks.update({"cs": x})

x = int(input("Enter maths: "))
marks.update({"maths": x})

x = int(input("Enter chem: "))
marks.update({"chem": x})

print(marks)

#Q4) Figure out the way to store 9 & 9.0 as values in the set
# note- 9 & 9.0 same in python but 9 & 9.8 are different

values = {9,"9.0"}
print(values)

#use built-in-data types for this ques
value = { # in the form of tuples
    ("int", 9),
    ("float", 9.0)
}
print(value)


