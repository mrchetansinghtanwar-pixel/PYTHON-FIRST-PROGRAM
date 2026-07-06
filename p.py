student = {
    "a": 25,
    "b":50
    
    
}

print(type(student))
print(student)
print(student["a"])

i = 1
while i <= 1000:
    print("join")
    i += 1


i = 1
while i <= 50:
    print(i, "chetan singh")
    i += 1
    
    
nums = (1,4,9,26,25,36,49,64,25,81,100)
x = 64
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx, ",i)
    else:
        print("finding..",i)
        
    i += 1
    
    
n = int(input("enter number"))
i = 1
while i < 11:
    print(n*i)
    i += 1
 
#i = 0   
#while True:
#    print("hello words", i)
 #   i += 1
    
marks = {}
x = marks.update({"phy" :50})
y = marks.update({"english" : 50})
print(marks)

def breakj():
    print("hello words")
    
output = breakj()


output = breakj()
print(type(output))


f = open(r"C:\Users\mrche\Dropbox\Ecommerce Sales\Customers.csv","xt")
data = f.read
print(data)

def sum(a,b):
    print(a+b)
    
sum(500,400)