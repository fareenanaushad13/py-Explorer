# f = open("FileInputOutput/demo.txt","w" ) #overwrite a data
# f = open("FileInputOutput/demo.txt","a" ) #append at the end

# f = open("FileInputOutput/demo.txt","r+" ) #for reading writing..the dtram is position at beginning of the file
# f = open("FileInputOutput/demo.txt","w+" ) #truncate
# print(f.read())
# f.write("\ni want to ")
# f.close()

# with syntax
with open("FileInputOutput/demo.txt","r") as f:
    data = f.read()
    print(data)

# with open("FileInputOutput/demo.txt","w") as f:
#    f.write("new data")
    
    