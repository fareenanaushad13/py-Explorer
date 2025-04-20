# Dictionary are used to store data values in key:value pairs.
# They are unordered, mutable(changeable) & do not allow duplicate keys

info = {
    "key" :  "value",
    "name" : "Farru",
    "class" : "MCA",
    "sem" : 35,
    "learning" : "coding",
    "is_adult" : True,
    "marks" : 92,
    88.99 : 99.87
}

print(info)

dict = {
    "name" : "far",
    "subject" : ["JAVA", "Python","DBMS"], #lists
    "topics" : ("dict", "set")
}
print(dict)
print(type(dict))
print(dict["name"])
print(dict["subject"])

null_dict = {}
print(null_dict)

# nested Dictionary
student = {
    "name" : "farru",
    "subjects" : {
        "phy" : 99,
        "chem" : 68,
        "math" : 77,
    }
}
print(student)
print(student["subjects"]["chem"])

#Methods In Dictionary
print(student.keys()) #---> returns all keys
print(list(student.keys())) #typecaste in list
print(len(student))

print(student.values()) #---> returns all values

#myDict.items -->retunrs all (key,values) pairs as tuples
print(student.items())
print(list(student.items()))
pair = list(student.items())
print(pair[1])

#myDict.get(key) --> returns the key acording to value
print(student.get("name")) #print name
print(student.get("name2")) #none

#mDict.update(newDict) --> insert a specific items to a Dictionary
student.update({"city" : "Bangalore"})
print(student)