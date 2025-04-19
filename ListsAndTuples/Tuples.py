# Tuples ---> A built-in data type that lets us create immutable sequence of values

tuple = (4,7,8)
print(tuple)
print(type(tuple))
print(tuple[0])
print(tuple[2])

#slicing
print(tuple[1:2])

# Methods In Tuple

#tup.index(el) --> returns index of first occurence
tup = (1,4,6,7,7)
print(tup.index(4))

# tup.count(el)--> counts total occurence
print(tup.count(7))