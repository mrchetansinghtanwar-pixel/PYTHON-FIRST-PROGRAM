str1 = "chetan"
str2 = "singh"
final_str = str1 + " " + str2
print(final_str)
print(len(final_str))
str = "chetan singh"
ch = str[0]
print(ch)
#slicing
str = "chetan singh"
print(str[0:6])
print(str[7:12])
print(str[0:12:2])
print(str[1 :4])
print(str[-5 : -2])
str1 = "i am studying python"
print(str1.endswith("python")) #returns true if string ends with substr
str1 = str1.capitalize()# capitalizes first letter of string
print(str1)
str1 = "i am studying python"
print(str1.replace("python", "java"))# replaces old substring with new substring
str1 = "i am studying python"
print(str1.find("python"))# returns index of first occurrence of substring
name = input("enter your name: ")
print(len(name))
str = "hi, $Ian the $symbol $ is used for string formatting"
print(str.count("$"))# returns number of occurrences of substring"
#conditional statements
age = 21
if(age >= 18):
    print("con vote & apply for driving license")
light = "pink"

if(light == "red"):
    print("stop")

elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("slow down")
else:
    print("light is not working")

age = 15
if(age >= 18):
    print("can vote)")#indentation is important in python, it defines the scope of the code block
else:
    print("cannot vote")

marks = int(input("enter your marks: "))
if(marks >= 90):
    print("grade A")
elif(marks >= 80 and marks < 90):
    print("grade B")
elif(marks >= 70 and marks < 80):
    print("grade C")
else:
    print("grade D")

print("grade of student is: ",end="grade")

age = 31
#nesting
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")


num = int(input("enter a number: "))
if(num % 2 == 0):
    print("even")
else:
    print("odd")

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
if(a > b and a > c):
    print("largest number is: ",a)
elif(b > a and b > c):
    print("largest number is: ",b)
else:
    print("largest number is: ",c)


a = int(input("first number"))
b = int(input("second number"))
c = int(input("third number"))
d = int(input("four number"))

if(a >= b and a >= c):
    print("first number is largest", a)
elif(a >= d):
    print("first number is largest", a)
elif(b >= c and b >= d):
    print("second number is largest", b)
elif(c >= d):  
    print("third number is largest", c)
else:
    print("four number is largest", d)

x = int(input("enter number :"))

if(x % 7 == 0):
    print("multiiple of 7")
else:
    print("Not a multipleP")
