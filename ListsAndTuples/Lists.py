#lists are mutable in python -->Changable
marks = [99.9,23,6,66,7,77,54,34,56]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[8])
print(len(marks))

#lists slicing
print(marks[1:4])
print(marks[:7])
print(marks[1:])
print(marks[:len(marks)])
#nagative index start from last index
print(marks[-1:-3])
print(marks[-3:-1])

student = ["farru", 9.5,"Bangalore"]
print(student[0])
print(student)
student[0] = "far"
print(student)

#Lists Methods
list = [3,6,1]
list1 = ['f', 'a','r','r','r']

#list.append()----> Add element at last index
list.append(7)
print(list)

# list.sort() ---> sorts in ascending order
list.sort()
print(list)

# list.sort(reverse = True) ---> sorts in Decsending order
list.sort(reverse = True)
print(list)

list1.sort()
print(list1)

# list.reverse()----> reverse lists
list1.reverse()
print(list1)

#list.insert(idx,el) --> insert element at index
list2 = [7,6,5,3]
list2.insert(2,1)
print(list2)

# list.remove(1)---> remove first occurence of element
list3 = [2,4,2,2,]
list3.remove(2)
print(list3)

# list.pop(idx)---> remove element from index
list2.remove(5)
print(list2)
