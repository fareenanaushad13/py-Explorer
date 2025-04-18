#concatation
str1 = "farru"
#length of String
print(len(str1))

str2 = "far"
final_str = str1+ " " +str2
print(final_str)

string = "HI!!!! I am Farru\nMCA student"
print(string)

#indexing
name = "fareena naushad"
ch = name[0]
print(ch)
print(name[6])

#slicing
name = "farru"
print(name[0:3]) #start index included but wnding not included
print(name[:4]) #[0:4]
print(name[0:]) #[5:len(str)] #last index

#negative index
college = "DSPMU"
print(college[-3:-1]) #starting index from last -3,-2,-1

#string Function
str = "i am a Coder"
print(str.endswith("der")) #endwith -->return true if string ends with substr
print(str.capitalize()) #capitalize ->capitalize first character
print(str.replace("a", "m")) #replace ->replace a with m
print(str.replace("Coder", "developer")) #replace coder with developer
print(str.find("a")) #find --> find--> returns 1st index of 1st occurence
print(str.find("Coder")) #space also count
print(str.find("f")) #-1 --> not found
print(str.count("a")) #count --> countd the occurence of substr

