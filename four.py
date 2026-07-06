student = {
    "name": "John",
    "age": 21,
    "subjects" : {
        "math": 90,
        "english": 85,
        "physics": 95   
        


    }
}
print(student["name"])
print(type(student))
print(student["subjects"])
print(student["subjects"]["math"])
print(student.keys())#returns a view object that displays a list of all the keys in the dictionary.
print(list(student.keys()))#returns a list of all the keys in the dictionary.
print(len(list(student.keys())))#retur     ns the number of keys in the dictionary.
print(student.values())#returns a view object that displays a list of all the values in the dictionary.
print(list(student.values()))#returns a list of all the values in the dictionary.
print(student.items())#returns a view object that displays a list of all the key-value pairs in the dictionary as tuples.
print(list(student.items()))#returns a list of all the key-value pairs in the dictionary as tuples.
pairs = list(student.items())
print(pairs[0])#returns the first key-value pair as a tuple.
print(student.get("na5"))#returns the value associated with the key "name".
student.update({"city" :"delhi"})
print(student)

#set
collection = {1,5,6,6,1,1,"hello","hello"     }
print(collection)
print(type(collection))
print(len(collection))

p = set()
print(type(p))
p.add(1)
print(p)
p.add(5)
print(p)
p.add((1))
print(p)
p.add("chetan")
print(p)
p.clear()
print(p)

marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter phy : "))
marks.update({"py" : x})

x = int(input("enter phy : "))
marks.update({"p5y" : x})

print(marks)
