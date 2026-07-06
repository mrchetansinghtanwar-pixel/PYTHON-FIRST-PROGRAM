count = 1
while count <= 5 :
 #   print("hello")
    count += 1

#print(count)

#i = 1
#while i <= 1000:
 #   print("join",i)
  #  i += 1 

i = 1
while i <= 5:
    print(i)
    i += 1

i = 5
while i >= 1:
    print(i)
    i -= 1

i = 1
while i <= 100:
    print(i)
    i += 1

i = 1
while i <= 10:
    print(3*i)
    i += 1

n = int(input("enter number"))
i = 1
while i <= 10:
    print(n*i)
    i += 1


nums = [1,4,9,26,25,36,49,64,81,100]

i = 0
while i < len(nums):
    print(nums[i])
    i += 1

nums = (1,4,9,26,25,36,49,64,81,100)
x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
       print("found at idx",i)
    i += 1

nums = (1,4,9,26,25,36,49,64,25,81,100)
x = 25
i = 0
while i < len(nums):
    if(nums== x):
        print("found at idx, ",i)
    else:
        print("finding..") 
    i += 1.
    
    


i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1

nums = (1,4,9,26,25,36,49,64,25,81,100)
x = 25
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx, ",i)
        break
    else:
        print("finding..") 
    i += 1

print(range(5))
seq = range(5)
print(seq[1])
print(seq[2])
print(seq[4])
print(seq[0])
print("end")

seq = range(10)

for i in seq:
    print(i)
print("end")

for i in range(10): #range(stop)
    print(i)
print("END")
for i in range(2,10): #range(start, stop)
    print(i)

for i in range(2, 10, 2):#range(start,stop,step)
    print(i)

for i in range(1,100):
    print(i)


for i in range(100,0,-1):
    print(i)


n = int(input('enter number :'))

for i in range(1, 11):
    print(n * i)
    

for i in range(5):
    pass # pass is a null statement

if i > 5:
    pass

n = 5

sum = 0
for i in range(1, n+1  ):

    sum += i

print("total sum ",sum)

n = 5
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1
print ("total sum", sum)

n = 5
fact = 1




