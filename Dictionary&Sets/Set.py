# set is the collection of the unordered item
# Each element in the set must be unique and immutable

collection = {1,2,3,4,"hello", "world", 2} # repeated value print only once--> 2 will print only once
print(collection)
print(type(collection))
print(len(collection)) #total number of items

collection = set() #empty set
print(type(collection))

#method in sets

#set.add(el) --> adds an element
collection.add(5)
collection.add(6)
collection.add(5)
collection.add("farrr")
print(collection)

#set.remove(el) --> remove an element
collection.remove(5)
# collection.remove(7) #error
print(collection)

# set.clear() --> empties the sets
collection.clear()
print(len(collection))

# set.pop() --> remove a random value
set = {"hello", "far","farru","coding","developer"}
print(set.pop())

# set.union(set2) --> combines both set values and return new
set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2)) # 1,2,3,4
print(set1)
print(set2) # return original value--> 2,3,4

# set.intersection(set2) --> combines common values & return new
print(set1.intersection(set2)) # 2,3