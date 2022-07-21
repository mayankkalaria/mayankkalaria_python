import random

#print(random.randint(1000,9999))
file=open("data.txt","w")
for i in range(10):
    num=random.randint(1,100)
    file.write(str(num)+",")
file.close()

file=open("data.txt","r")
odd=open("odd.txt","w")
even=open("even.txt","w")
l=file.read().split(",")[:-1]
for i in l:
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")

even.close()
odd.close()
file.close()

print("Data File Content")
data=open("data.txt","r")
print(data.read())
data.close()

print("Even File Content")
even=open("even.txt","r")
print(even.read())
even.close()

print("Odd File Content")
odd=open("odd.txt","r")
print(odd.read())
odd.close()

