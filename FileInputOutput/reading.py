f = open("FileInputOutput/demo.txt","r" )
# data = f.read() #read entire file
line = f.readline()  read one line at a time
print(line)
print(type(line))
f.close()