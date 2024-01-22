import random

def display(myroom):
    print(myroom)

myroom=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],]
print("My room is dirty")
display(myroom)

a=0
b=0
while a<4:
    while b<4:
        myroom[a][b]=random.choice([0,1])
        b+=1
    a+=1
    b=0

print("Dirt detected from my room")
display(myroom)
a=0
b=0
c=0
while a<4:
    while b<4:
        if myroom[a][b]==1:
            print("Location of vaccum:",a,b)
            myroom[a][b]=0
            print("My room is cleaned",a,b)
            c+=1
        b+=1
    a+=1
    b=0
    
performance=(100-((c/16)*100))
print("My room is clean finally,Thank You:")
display(myroom)
print("performance= ",performance,'%')