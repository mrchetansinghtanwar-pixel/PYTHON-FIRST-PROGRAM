from numpy import number


f = open("demo.txt","r+")
#data = f.read(5)
#print(data)
#print(type(data))

#j = f.readline()
#print(j)


#lline2 = f.readline()
#print(lline2)

#line3  = f.readline()
#print(line3)


#line4 = f.readline()
#print(line4)

f.write("I want to javascript tomorrow. 123")

f.write("\nI want to javascript tomorrow. 123")







u = open("sample.txt","r+")
d = u.write("abcd")
u.seek(0)  # Move the file pointer to the beginning 
print(u.read())




u.close()

with open ("c_demo.txt", "r") as g:
    data = g.read()
    print(data)
    
with open ("c_demo.txt", "w") as g:
    g.write("I want to learn python tomorrow. 1")


word = "learning"

with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Word found!")
    else:
        print("Word not found!")
    
    

new_data = data.replace("java","python")
print(new_data)

            

def check_word_in_file():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
    if(data.find(word) != -1):
        print("Word found!")
    else:
        print("Word not found!")
        
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return
            line_no += 1
            
    return -1

check_for_line()
count = 0
with open("simple.txt", "r") as i:
    data = i.read()
    print(data)
    
    num = ""
    for j in range(len(data)):
        if(data[j] == ","):
            print(num)
            num = ""
        else:
            num += data[j]
            
    number = data.split(",")
    for val in number:
         if(int(val) % 2 == 0):
                count += 1
                
print("Total even numbers are: ", count)

            
            
            
