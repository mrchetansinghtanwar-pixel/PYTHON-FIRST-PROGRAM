a = 5
b= 10

sum = a + b
print(sum)

a = 2
a = 10
sum = a + b 
print(sum)

a = 12
b = 17
sum = a + b
print(sum)

def calc_sum(a, b):
    sum = a + b
    print(sum)
    return sum

calc_sum(50,50)
calc_sum(500,52)

def chetan(a,b):
    sum = a - b 
    print(sum)
    return sum

chetan(50,20)


#function definition
def calc_sumz(a,b):#parameters
    return a + b 

cal = calc_sumz(50000,5046)#function call; arguments
print(cal)

pm = calc_sumz(500,200)
print(pm)

def calc_avg(a,b,c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg


calc_avg (50,95,85)

cities = ["delhi", "gurgaon","noida","pune","mumbai","chennai"]
heroes = ["thor", "ironman", "captain amrica","shakiman"]

print(heroes[0], end=" ")
print(heroes[1], end=" ")


def print_len(list):
    print(len(list))
    
print_len(cities)
print_len(heroes)

def print_list(list):
    for item in list:
        print(item,end="\n")

print_list(cities)
print_list(heroes)

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    
    
cal_fact(5)

n = int(input("enter number"))
print(n*83)

def cal_s(a):
    print(a *83)

cal_s(5000)

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USA =", inr_val, "INR")


converter(int(input("enter number")))

#Recursion
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    
    
def fact(n):
    if(n == 0 or n == 1):
        return 1
    return fact(n-1) * n

print(fact(5,))

def calc_sum(n):
    if(n == 0):
        return
    print(n)
    calc_sum(n-1)
    
calc_sum(5)


def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
    
frults = ["mango", "litchi","apple", "banana"]

print_list(frults)


        
    