# Q1) Enter names of three movies and & store them in a list
movies = []
mov1 = input("Enter 1st movie:")
mov2 = input("Enter 2nd movie:")
mov3 = input("Enter 3rd movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

#Q2) lists contain palindrome or not
# list = ['m','a','a','m']
list = [3,6,1]

copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("Palindrome")
else:
    print("Not Palindrome")    

# Q3) count the number of students with the "A" grade in the followinh tuple
grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))

# Q4) Stores the above value in the list & sort them from "A" to "D"
grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)