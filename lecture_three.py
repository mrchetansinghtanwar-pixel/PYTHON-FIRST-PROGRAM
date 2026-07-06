#list
marks = [90, 80, 70, 60, 50]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))
student = ["shejal", 98, 90.5]
print(student[0])
student[0] = "chetan"
print(student)
print(student[0:2])
print(student[1:2])
#Adding an element to a list
list1 = [1, 2, 3]
print(list1.append(4))
print(list1)
list = [1, 2, 3, 4]
list.append(6)
print(list)
#sorting a list
list = [2, 5, 9, 1, 3, 5, 4, 9, 5 ,7, 8, 0 ,5]
list.sort()
print(list)
#reverse sorting
LIST = [2, 5, 9, 1, 3, 5, 4, 9, 5 ,7, 8, 0 ,5]
LIST.sort(reverse=True)
print(LIST)
#reversing a list
list = [1, 2, 3, 4, 5]
list.reverse()      
print(list)
#inserting an element at a specific position
list = [1, 2, 3, 4, 5]
list.insert(2, 10)
print(list)
list = [1, 2, 3, 4, 5]
list.insert(4, 9)
print(list)

movie = []

movie.append(input("enter movie name: "))
movie.append(input("enter movie name: "))
movie.append(input("enter movie name: "))
print(movie)

list1 = [1,2,5]

mov = list1.copy()
mov.reverse()
if(list1 == mov):
    print("list is palindrome") 
else:   
    print("list is not palindrome")

GRADE = ("A", "A", "B", "C", "A", "B", "C", "D")

print(GRADE.count("A"))

s = ["A", "B", "A", "C","A", "B", "C", "D"]
s.sort()
print(s)
